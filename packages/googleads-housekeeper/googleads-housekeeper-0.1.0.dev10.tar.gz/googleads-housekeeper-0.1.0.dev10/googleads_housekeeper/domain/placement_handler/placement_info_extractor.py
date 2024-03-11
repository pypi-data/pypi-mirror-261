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
"""Extracts extra info on placements from DB."""
from __future__ import annotations

import gaarf

from googleads_housekeeper.services import unit_of_work


class PlacementInfoExtractor:

    def __init__(self, uow: unit_of_work.AbstractUnitOfWork) -> None:
        self.website_info = uow.website_info
        self.youtube_channel_info = uow.youtube_channel_info
        self.youtube_video_info = uow.youtube_video_info

    def extract_placement_info(self,
                               placement_info: gaarf.report.GaarfRow) -> dict:
        if placement_info.placement_type == 'WEBSITE':
            return {
                'website_info':
                    self._get_placement_from_repo(self.website_info,
                                                  placement_info.placement)
            }
        if placement_info.placement_type == 'YOUTUBE_CHANNEL':
            return {
                'youtube_channel_info':
                    self._get_placement_from_repo(self.youtube_channel_info,
                                                  placement_info.placement)
            }

        if placement_info.placement_type == 'YOUTUBE_VIDEO':
            return {
                'youtube_video_info':
                    self._get_placement_from_repo(self.youtube_video_info,
                                                  placement_info.placement)
            }
        return {}

    def _get_placement_from_repo(self, repo, placement: str) -> dict:
        if placement := repo.get_by_condition('placement', placement):
            return placement[0]
        return {}
