"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.model.item_category import ItemCategory
from rrap_mds_is_registry_api.model.item_sub_type import ItemSubType
from rrap_mds_is_registry_api.model.record_type import RecordType
globals()['ItemCategory'] = ItemCategory
globals()['ItemSubType'] = ItemSubType
globals()['RecordType'] = RecordType
from rrap_mds_is_registry_api.model.seeded_item import SeededItem


class TestSeededItem(unittest.TestCase):
    """SeededItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSeededItem(self):
        """Test SeededItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SeededItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
