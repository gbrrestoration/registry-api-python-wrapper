"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.item_organisation import ItemOrganisation
from openapi_client.model.seeded_item import SeededItem
from openapi_client.model.status import Status
globals()['ItemOrganisation'] = ItemOrganisation
globals()['SeededItem'] = SeededItem
globals()['Status'] = Status
from openapi_client.model.organisation_list_response import OrganisationListResponse


class TestOrganisationListResponse(unittest.TestCase):
    """OrganisationListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganisationListResponse(self):
        """Test OrganisationListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganisationListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
