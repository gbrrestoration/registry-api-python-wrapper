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
from rrap_mds_is_registry_api.model.item_model_run_workflow_definition import ItemModelRunWorkflowDefinition
from rrap_mds_is_registry_api.model.item_sub_type import ItemSubType
from rrap_mds_is_registry_api.model.seeded_item import SeededItem
globals()['ItemCategory'] = ItemCategory
globals()['ItemModelRunWorkflowDefinition'] = ItemModelRunWorkflowDefinition
globals()['ItemSubType'] = ItemSubType
globals()['SeededItem'] = SeededItem
from rrap_mds_is_registry_api.model.item3 import Item3


class TestItem3(unittest.TestCase):
    """Item3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testItem3(self):
        """Test Item3"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Item3()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
