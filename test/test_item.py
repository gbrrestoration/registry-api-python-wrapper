"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.model.dataset_structural_template import DatasetStructuralTemplate
from rrap_mds_is_registry_api.model.dataset_temporal_information import DatasetTemporalInformation
from rrap_mds_is_registry_api.model.dataset_usage_information import DatasetUsageInformation
from rrap_mds_is_registry_api.model.item_category import ItemCategory
from rrap_mds_is_registry_api.model.item_dataset_template import ItemDatasetTemplate
from rrap_mds_is_registry_api.model.item_sub_type import ItemSubType
from rrap_mds_is_registry_api.model.record_type import RecordType
from rrap_mds_is_registry_api.model.seeded_item import SeededItem
globals()['DatasetStructuralTemplate'] = DatasetStructuralTemplate
globals()['DatasetTemporalInformation'] = DatasetTemporalInformation
globals()['DatasetUsageInformation'] = DatasetUsageInformation
globals()['ItemCategory'] = ItemCategory
globals()['ItemDatasetTemplate'] = ItemDatasetTemplate
globals()['ItemSubType'] = ItemSubType
globals()['RecordType'] = RecordType
globals()['SeededItem'] = SeededItem
from rrap_mds_is_registry_api.model.item import Item


class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testItem(self):
        """Test Item"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Item()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
