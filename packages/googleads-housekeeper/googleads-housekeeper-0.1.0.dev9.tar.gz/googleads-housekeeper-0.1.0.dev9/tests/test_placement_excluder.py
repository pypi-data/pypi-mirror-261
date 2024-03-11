from __future__ import annotations

import gaarf
import pytest

from googleads_housekeeper.domain.placement_handler import placement_excluder
from googleads_housekeeper.services import enums

_TEST_CUSTOMER_ID = 123456789
_TEST_CAMPAIGN_ID = 23456
_TEST_AD_GROUP_ID = 34567
_TEST_CRITERION_ID = 456789
_REPORT_COLUMN_NAMES = [
    'customer_id', 'campaign_id', 'campaign_type', 'ad_group_id',
    'placement_type', 'placement', 'criterion_id'
]
_REPORT_COLUMN_NAMES_WITH_ALLOWLISTING = _REPORT_COLUMN_NAMES + ['allowlisted']


class TestPlacementExcluder:

    @pytest.fixture
    def test_client(self, mocker):
        mocker.patch('google.ads.googleads.client.oauth2', return_value=[])
        return gaarf.api_clients.GoogleAdsApiClient()

    @pytest.fixture
    def excluder(self, test_client):
        return placement_excluder.PlacementExcluder(client=test_client)

    @pytest.fixture
    def placement_exclusion_lists(self):
        return {
            f'CPR Negative placements list - Campaign: {_TEST_CAMPAIGN_ID}':
                f'customers/{_TEST_CUSTOMER_ID}/sharedSet/123'
        }

    @pytest.fixture
    def website_placement_display_campaign(self):
        return gaarf.report.GaarfRow(
            data=[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'DISPLAY',
                _TEST_AD_GROUP_ID, 'WEBSITE', 'example.com',
                f'{_TEST_CRITERION_ID}'
            ],
            column_names=_REPORT_COLUMN_NAMES)

    @pytest.fixture
    def youtube_placement_video_campaign(self):
        return gaarf.report.GaarfRow(
            data=[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'VIDEO',
                _TEST_AD_GROUP_ID, 'YOUTUBE_VIDEO', 'test-video-id',
                f'{_TEST_CRITERION_ID}'
            ],
            column_names=_REPORT_COLUMN_NAMES)

    @pytest.mark.parametrize('exclusion_level,expected_resource', [
        (enums.ExclusionLevelEnum.AD_GROUP,
         f'customers/{_TEST_CUSTOMER_ID}/adGroupCriteria/'
         f'{_TEST_AD_GROUP_ID}~{_TEST_CRITERION_ID}'),
        (enums.ExclusionLevelEnum.CAMPAIGN,
         f'customers/{_TEST_CUSTOMER_ID}/campaignCriteria/'
         f'{_TEST_CAMPAIGN_ID}~{_TEST_CRITERION_ID}'),
        (enums.ExclusionLevelEnum.ACCOUNT,
         f'customers/{_TEST_CUSTOMER_ID}/customerNegativeCriteria/'
         f'{_TEST_CRITERION_ID}'),
    ])
    def test_create_placement_operation_returns_correct_resource_name(
            self, website_placement_display_campaign, excluder,
            placement_exclusion_lists, exclusion_level, expected_resource):

        excluder._init_criterion_service_and_operation(exclusion_level)
        operation, _ = excluder._create_placement_operation(
            website_placement_display_campaign, exclusion_level,
            placement_exclusion_lists)

        assert operation.exclusion_operation.create.resource_name == expected_resource
        assert 'example.com' in operation.exclusion_operation.create.placement.url
        assert not operation.is_attachable
        assert not operation.shared_set_resource_name

    def test_create_placement_operation_returns_correct_placement_type(
            self, website_placement_display_campaign, excluder,
            placement_exclusion_lists):

        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        excluder._init_criterion_service_and_operation(exclusion_level)
        operation, _ = excluder._create_placement_operation(
            website_placement_display_campaign, exclusion_level,
            placement_exclusion_lists)

        assert 'example.com' in operation.exclusion_operation.create.placement.url

    def test_create_placement_operation_returns_correct_placement_type_for_mobile_application(
            self, excluder, placement_exclusion_lists):

        placement_info = gaarf.report.GaarfRow(
            data=[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'DISPLAY',
                _TEST_AD_GROUP_ID, 'MOBILE_APPLICATION',
                'com.example.googleplay', '_TEST_CRITERION_ID'
            ],
            column_names=_REPORT_COLUMN_NAMES)

        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        excluder._init_criterion_service_and_operation(exclusion_level)
        operation, _ = excluder._create_placement_operation(
            placement_info, exclusion_level, placement_exclusion_lists)

        assert 'com.example.googleplay' in (
            operation.exclusion_operation.create.mobile_application.app_id)

    def test_create_placement_operation_returns_correct_placement_type_for_youtube_video(
            self, excluder, placement_exclusion_lists):

        placement_info = gaarf.report.GaarfRow(
            data=[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'DISPLAY',
                _TEST_AD_GROUP_ID, 'YOUTUBE_VIDEO', 'test-video-id',
                '_TEST_CRITERION_ID'
            ],
            column_names=_REPORT_COLUMN_NAMES)

        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        excluder._init_criterion_service_and_operation(exclusion_level)
        operation, _ = excluder._create_placement_operation(
            placement_info, exclusion_level, placement_exclusion_lists)

        assert 'test-video-id' in (
            operation.exclusion_operation.create.youtube_video.video_id)

    def test_create_placement_operation_returns_correct_placement_type_for_youtube_channel(
            self, excluder, placement_exclusion_lists):

        placement_info = gaarf.report.GaarfRow(
            data=[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'DISPLAY',
                _TEST_AD_GROUP_ID, 'YOUTUBE_CHANNEL', 'test-channel-id',
                '_TEST_CRITERION_ID'
            ],
            column_names=_REPORT_COLUMN_NAMES)

        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        excluder._init_criterion_service_and_operation(exclusion_level)
        operation, _ = excluder._create_placement_operation(
            placement_info, exclusion_level, placement_exclusion_lists)

        assert 'test-channel-id' in (
            operation.exclusion_operation.create.youtube_channel.channel_id)

    def test_create_placement_operation_does_not_create_shared_for_website(
            self, website_placement_display_campaign, excluder,
            placement_exclusion_lists):

        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        excluder._init_criterion_service_and_operation(exclusion_level)
        operation, _ = excluder._create_placement_operation(
            website_placement_display_campaign, exclusion_level,
            placement_exclusion_lists)

        assert not operation.shared_set_resource_name

    def test_create_placement_operation_returns_shared_set_operation_for_video_campaign(
            self, youtube_placement_video_campaign, excluder,
            placement_exclusion_lists):

        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        excluder._init_criterion_service_and_operation(exclusion_level)
        operation, _ = excluder._create_placement_operation(
            youtube_placement_video_campaign, exclusion_level,
            placement_exclusion_lists)

        assert operation.exclusion_operation.create.shared_set in (
            placement_exclusion_lists.values())
        assert not operation.is_attachable

    def test_create_placement_exclusion_operations_returns_only_operations_for_display_campaign(
            self, excluder, placement_exclusion_lists):
        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        report = gaarf.report.GaarfReport(
            results=[[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'DISPLAY',
                _TEST_AD_GROUP_ID, 'WEBSITE', 'example.com',
                '_TEST_CRITERION_ID', False
            ]],
            column_names=_REPORT_COLUMN_NAMES_WITH_ALLOWLISTING)
        excluder._init_criterion_service_and_operation(exclusion_level)
        exclusion_operations = excluder._create_exclusion_operations(
            report, exclusion_level, placement_exclusion_lists)

        assert _TEST_CUSTOMER_ID in exclusion_operations.placement_exclusion_operations
        assert not exclusion_operations.shared_set_creation_operations
        assert not exclusion_operations.campaign_set_association_operations

    def test_create_placement_exclusion_operations_returns_nothing_for_allowlisted_placement(
            self, excluder, placement_exclusion_lists):
        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        report = gaarf.report.GaarfReport(
            results=[[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'VIDEO',
                _TEST_AD_GROUP_ID, 'YOUTUBE_VIDEO', 'test-video-id',
                '_TEST_CRITERION_ID', True
            ]],
            column_names=_REPORT_COLUMN_NAMES_WITH_ALLOWLISTING)
        excluder._init_criterion_service_and_operation(exclusion_level)
        exclusion_operations = excluder._create_exclusion_operations(
            report, exclusion_level, placement_exclusion_lists)
        assert not exclusion_operations.placement_exclusion_operations
        assert not exclusion_operations.shared_set_creation_operations
        assert not exclusion_operations.campaign_set_association_operations

    def test_create_placement_exclusion_operations_returns_only_share_set_operations_for_video_campaign(
            self, excluder, placement_exclusion_lists):
        exclusion_level = enums.ExclusionLevelEnum.AD_GROUP
        report = gaarf.report.GaarfReport(
            results=[[
                _TEST_CUSTOMER_ID, _TEST_CAMPAIGN_ID, 'VIDEO',
                _TEST_AD_GROUP_ID, 'YOUTUBE_VIDEO', 'test-video-id',
                '_TEST_CRITERION_ID', False
            ]],
            column_names=_REPORT_COLUMN_NAMES_WITH_ALLOWLISTING)
        excluder._init_criterion_service_and_operation(exclusion_level)
        exclusion_operations = excluder._create_exclusion_operations(
            report, exclusion_level, placement_exclusion_lists)

        assert not exclusion_operations.placement_exclusion_operations
        assert _TEST_CUSTOMER_ID in exclusion_operations.shared_set_creation_operations
        assert not exclusion_operations.campaign_set_association_operations
