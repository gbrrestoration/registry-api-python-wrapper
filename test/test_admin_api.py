"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api.admin_api import AdminApi  # noqa: E501


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_registry_admin_export(self):
        """Test case for registry_admin_export

        Export Items  # noqa: E501
        """
        pass

    def test_registry_admin_import(self):
        """Test case for registry_admin_import

        Import Items Parsed  # noqa: E501
        """
        pass

    def test_registry_admin_restore(self):
        """Test case for registry_admin_restore

        Restore From Table Parsed  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
