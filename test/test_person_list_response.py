"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.model.item_person import ItemPerson
from rrap_mds_is_registry_api.model.seeded_item import SeededItem
from rrap_mds_is_registry_api.model.status import Status
globals()['ItemPerson'] = ItemPerson
globals()['SeededItem'] = SeededItem
globals()['Status'] = Status
from rrap_mds_is_registry_api.model.person_list_response import PersonListResponse


class TestPersonListResponse(unittest.TestCase):
    """PersonListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPersonListResponse(self):
        """Test PersonListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PersonListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
