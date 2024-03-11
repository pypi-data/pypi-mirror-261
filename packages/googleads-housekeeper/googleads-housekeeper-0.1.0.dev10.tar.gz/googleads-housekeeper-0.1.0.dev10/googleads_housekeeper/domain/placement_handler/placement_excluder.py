# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

import dataclasses
import functools
import logging
import operator
from collections import defaultdict
from collections.abc import Iterable
from copy import deepcopy

import gaarf
import proto
import tenacity
from google.ads import googleads
from google.api_core import exceptions

from googleads_housekeeper.domain.placement_handler import entities
from googleads_housekeeper.services import enums


@dataclasses.dataclass
class ExclusionResult:
    excluded_placements: gaarf.report.GaarfReport | None = None
    associated_with_list_placements: gaarf.report.GaarfReport | None = None


@dataclasses.dataclass
class ExclusionOperations:
    placement_exclusion_operations: dict
    shared_set_creation_operations: dict
    campaign_set_association_operations: dict
    excluded_placements: gaarf.report.GaarfReport
    attachable_placements: gaarf.report.GaarfReport


@dataclasses.dataclass
class PlacementOperation:
    customer_id: int
    exclusion_operation: proto.message.Message
    shared_set_resource_name: str | None = None
    is_attachable: bool = False


class PlacementExcluder:
    """Class for excluding placements based on a sequence of exclusion specifications."""

    associable_with_negative_lists = ('VIDEO',)
    attachable_to_negative_lists = ('DISPLAY', 'SEARCH')

    def __init__(self, client: gaarf.api_clients.GoogleAdsApiClient):
        self._client = client

    @property
    def client(self):
        return self._client.client

    def exclude_placements(
        self,
        to_be_excluded_placements: gaarf.report.GaarfReport,
        exclusion_level: enums.ExclusionLevelEnum = enums.ExclusionLevelEnum
        .AD_GROUP
    ) -> ExclusionResult:
        self._init_criterion_service_and_operation(exclusion_level)
        report_fetcher = gaarf.query_executor.AdsReportFetcher(self._client)
        customer_ids = list(
            set(to_be_excluded_placements['customer_id'].to_list(
                flatten=True, distinct=True)))
        placement_exclusion_lists = report_fetcher.fetch(
            entities.PlacementExclusionLists(), customer_ids)
        placement_exclusion_lists = placement_exclusion_lists.to_dict(
            key_column='name',
            value_column='resource_name',
            value_column_output='scalar')
        exclusion_operations = (
            self._create_exclusion_operations(to_be_excluded_placements,
                                              exclusion_level,
                                              placement_exclusion_lists))
        for customer_id, operations in (
                exclusion_operations.shared_set_creation_operations.items()):
            try:
                if operations:
                    self._add_placements_to_shared_set(customer_id, operations)
                    logging.info(
                        'Added %d placements to shared_set for %d account',
                        len(operations), customer_id)
            except Exception as e:
                logging.error(e)
        for customer_id, operations in (
                exclusion_operations.placement_exclusion_operations.items()):
            try:
                if operations:
                    self._exclude(customer_id, operations)
                    logging.info('Excluded %d placements from account %s',
                                 len(operations), customer_id)
            except Exception as e:
                logging.error(e)
        logging.info('%d placements was excluded',
                     len(exclusion_operations.excluded_placements))
        if exclusion_operations.campaign_set_association_operations:
            operations = self._create_campaign_set_operations(
                customer_id,
                exclusion_operations.campaign_set_association_operations)
            self._add_campaigns_to_shared_set(customer_id, operations)
        if excluded_placements := exclusion_operations.excluded_placements:
            excluded_placements = functools.reduce(
                operator.add, exclusion_operations.excluded_placements)
        if attachable_placements := exclusion_operations.attachable_placements:
            attachable_placements = functools.reduce(operator.add,
                                                     attachable_placements)
        return ExclusionResult(
            excluded_placements=excluded_placements,
            associated_with_list_placements=attachable_placements)

    def _init_criterion_service_and_operation(
            self, exclusion_level: enums.ExclusionLevelEnum) -> None:
        # Init services for ShareSets
        self.campaign_service = self.client.get_service('CampaignService')
        self.campaign_set_operation = self.client.get_type(
            'CampaignSharedSetOperation')
        self.shared_set_service = self.client.get_service('SharedSetService')
        self.shared_criterion_service = self.client.get_service(
            'SharedCriterionService')
        self.campaign_shared_set_service = self.client.get_service(
            'CampaignSharedSetService')
        self.shared_set_operation = self.client.get_type('SharedSetOperation')

        if exclusion_level == enums.ExclusionLevelEnum.CAMPAIGN:
            self.criterion_service = self.client.get_service(
                'CampaignCriterionService')
            self.criterion_operation = self.client.get_type(
                'CampaignCriterionOperation')
            self.entity_path_method = self.criterion_service.campaign_path
            self.mutate_operation = (
                self.criterion_service.mutate_campaign_criteria)
            self.entity_name = 'campaign_id'
        if exclusion_level == enums.ExclusionLevelEnum.AD_GROUP:
            self.criterion_service = self.client.get_service(
                'AdGroupCriterionService')
            self.criterion_operation = self.client.get_type(
                'AdGroupCriterionOperation')
            self.entity_path_method = (self.criterion_service.ad_group_path)
            self.mutate_operation = self.criterion_service.mutate_ad_group_criteria
            self.entity_name = 'ad_group_id'
        if exclusion_level == enums.ExclusionLevelEnum.ACCOUNT:
            self.criterion_service = self.client.get_service(
                'CustomerNegativeCriterionService')
            self.criterion_operation = self.client.get_type(
                'CustomerNegativeCriterionOperation')
            self.entity_path_method = self.criterion_service.customer_path
            self.mutate_operation = (
                self.criterion_service.mutate_customer_negative_criteria)
            self.entity_name = 'customer_id'

    def _create_exclusion_operations(
        self,
        placements: gaarf.report.GaarfReport,
        exclusion_level: enums.ExclusionLevelEnum,
        placement_exclusion_lists: dict[str, str],
    ) -> ExclusionOperations:
        """Generates exclusion operations on customer_id level and get all
    placements that cannot be excluded."""
        operations_mapping: dict[str, list] = defaultdict(list)
        excluded_placements: list[gaarf.report.GaarfReport] = []
        shared_set_operations_mapping: dict[str, list] = defaultdict(list)
        attachable_placements: list[gaarf.report.GaarfReport] = []
        campaign_set_mapping: dict[str, int] = {}
        for placement_info in placements:
            if placement_info.allowlisted or placement_info.excluded_already:
                continue
            placement_operation, relavant_placement_info = (
                self._create_placement_operation(placement_info,
                                                 exclusion_level,
                                                 placement_exclusion_lists))
            if shared_set := placement_operation.shared_set_resource_name:
                shared_set_operations_mapping[
                    placement_operation.customer_id].append(
                        placement_operation.exclusion_operation)
                attachable_placements.append(relavant_placement_info)
                if placement_operation.is_attachable:
                    campaign_set_mapping[
                        shared_set] = placement_info.campaign_id
            else:
                operations_mapping[placement_operation.customer_id].append(
                    placement_operation.exclusion_operation)
                excluded_placements.append(relavant_placement_info)
        return ExclusionOperations(
            placement_exclusion_operations=operations_mapping,
            shared_set_creation_operations=shared_set_operations_mapping,
            campaign_set_association_operations=campaign_set_mapping,
            excluded_placements=excluded_placements,
            attachable_placements=attachable_placements)

    def _create_placement_operation(
        self,
        placement_info: gaarf.report.GaarfRow,
        exclusion_level: enums.ExclusionLevelEnum,
        placement_exclusion_lists: dict[str, str] | None = None
    ) -> tuple[PlacementOperation, GaarfReport]:
        'Creates exclusion operation for a single placement.' ''
        entity_criterion = None
        shared_set_resource_name = None
        is_attachable = False
        if (exclusion_level in (enums.ExclusionLevelEnum.CAMPAIGN,
                                enums.ExclusionLevelEnum.AD_GROUP) and
                placement_info.campaign_type
                in self.associable_with_negative_lists):
            if shared_set_resource_name := self._create_shared_set(
                    placement_info.customer_id, placement_info.campaign_id,
                    placement_exclusion_lists):
                shared_criterion_operation = self.client.get_type(
                    'SharedCriterionOperation')
                entity_criterion = shared_criterion_operation.create
                entity_criterion.shared_set = shared_set_resource_name
            if placement_info.campaign_type in self.attachable_to_negative_lists:
                is_attachable = True

        if (placement_info.placement_type ==
                enums.PlacementTypeEnum.MOBILE_APPLICATION.name):
            app_id = self._format_app_id(placement_info.placement)
        if not entity_criterion:
            entity_criterion = self.criterion_operation.create
        # Assign specific criterion
        if placement_info.placement_type == (
                enums.PlacementTypeEnum.WEBSITE.name):
            entity_criterion.placement.url = placement_info.placement
        if (placement_info.placement_type ==
                enums.PlacementTypeEnum.MOBILE_APPLICATION.name):
            entity_criterion.mobile_application.app_id = app_id
        if placement_info.placement_type == (
                enums.PlacementTypeEnum.YOUTUBE_VIDEO.name):
            entity_criterion.youtube_video.video_id = placement_info.placement
        if (placement_info.placement_type ==
                enums.PlacementTypeEnum.YOUTUBE_CHANNEL.name):
            entity_criterion.youtube_channel.channel_id = (
                placement_info.placement)
        if exclusion_level == enums.ExclusionLevelEnum.ACCOUNT:
            entity_criterion.customer = (
                self.entity_path_method(placement_info.customer_id,
                                        placement_info.criterion_id))
        elif not shared_set_resource_name:
            entity_criterion.negative = True
            if exclusion_level == enums.ExclusionLevelEnum.AD_GROUP:
                entity_criterion.ad_group = self.entity_path_method(
                    placement_info.customer_id,
                    placement_info.get(self.entity_name))
            elif exclusion_level == enums.ExclusionLevelEnum.CAMPAIGN:
                entity_criterion.campaign = self.entity_path_method(
                    placement_info.customer_id,
                    placement_info.get(self.entity_name))
        if shared_set_resource_name:
            operation = deepcopy(shared_criterion_operation)
        else:
            operation = deepcopy(self.criterion_operation)
        placement_operation = PlacementOperation(
            customer_id=placement_info.customer_id,
            exclusion_operation=operation,
            shared_set_resource_name=shared_set_resource_name,
            is_attachable=is_attachable)
        revelant_placement_info = gaarf.report.GaarfReport(
            results=[placement_info.data],
            column_names=placement_info.column_names)
        return placement_operation, revelant_placement_info

    def _create_shared_set(
        self,
        customer_id: int,
        campaign_id: int,
        placement_exclusion_lists: dict[str, str],
        base_share_set_name: str = 'CPR Negative placements list - Campaign:'
    ) -> str | None:
        name = f'{base_share_set_name} {campaign_id}'
        if name in placement_exclusion_lists:
            return placement_exclusion_lists[name]
        shared_set = self.shared_set_operation.create
        shared_set.name = name
        shared_set.type_ = (
            self.client.enums.SharedSetTypeEnum.NEGATIVE_PLACEMENTS)

        operation = deepcopy(self.shared_set_operation)
        try:
            shared_set_response = self.shared_set_service.mutate_shared_sets(
                customer_id=str(customer_id), operations=[operation])
            shared_set_resource_name = shared_set_response.results[
                0].resource_name
            logging.debug('Created shared set "%s".', shared_set_resource_name)
            return shared_set_resource_name
        except googleads.errors.GoogleAdsException:
            logging.debug('Shared set "%s" already exists.', name)
            return None

    def _add_placements_to_shared_set(self, customer_id: int,
                                      operations: list) -> None:
        if not isinstance(operations, Iterable):
            operations = [operations]
        try:
            for attempt in tenacity.Retrying(
                    retry=tenacity.retry_if_exception_type(
                        exceptions.InternalServerError),
                    stop=tenacity.stop_after_attempt(3),
                    wait=tenacity.wait_exponential()):
                with attempt:
                    self.shared_criterion_service.mutate_shared_criteria(
                        customer_id=str(customer_id), operations=operations)
        except tenacity.RetryError as retry_failure:
            logging.error(
                "Cannot add placements to exclusion list for account '%s' %d times",
                customer_id, retry_failure.last_attempt.attempt_number)

    def _create_campaign_set_operations(self, customer_id,
                                        campaign_set_mapping: dict) -> list:
        campaign_set = self.campaign_set_operation.create
        operations = []
        for shared_set, campaign_id in campaign_set_mapping.items():
            campaign_set.campaign = self.campaign_service.campaign_path(
                customer_id, campaign_id)
            campaign_set.shared_set = shared_set
            operation = deepcopy(self.campaign_set_operation)
            operations.append(operation)
        return operations

    def _add_campaigns_to_shared_set(self, customer_id: str,
                                     operations: list) -> None:
        self.campaign_shared_set_service.mutate_campaign_shared_sets(
            customer_id=str(customer_id), operations=operations)

    def _format_app_id(self, app_id: str) -> str:
        if app_id.startswith('mobileapp::'):
            criteria = app_id.split('-')
            app_id = criteria[-1]
            app_store = criteria[0].split('::')[-1]
            app_store = app_store.replace('mobileapp::1000', '')
            app_store = app_store.replace('1000', '')
            return f'{app_store}-{app_id}'
        return app_id

    def _exclude(self, customer_id: str, operations) -> None:
        """Applies exclusion operations for a single customer_id."""
        if not isinstance(operations, Iterable):
            operations = [operations]
        try:
            for attempt in tenacity.Retrying(
                    retry=tenacity.retry_if_exception_type(
                        exceptions.InternalServerError),
                    stop=tenacity.stop_after_attempt(3),
                    wait=tenacity.wait_exponential()):
                with attempt:
                    self.mutate_operation(
                        customer_id=str(customer_id), operations=operations)
        except tenacity.RetryError as retry_failure:
            logging.error("Cannot exclude placements for account '%s' %d times",
                          customer_id,
                          retry_failure.last_attempt.attempt_number)
