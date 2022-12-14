"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api.access_check_api import AccessCheckApi  # noqa: E501


class TestAccessCheckApi(unittest.TestCase):
    """AccessCheckApi unit test stubs"""

    def setUp(self):
        self.api = AccessCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_admin_access(self):
        """Test case for check_admin_access

        Check Admin Access  # noqa: E501
        """
        pass

    def test_check_general_access(self):
        """Test case for check_general_access

        Check General Access  # noqa: E501
        """
        pass

    def test_check_read_access(self):
        """Test case for check_read_access

        Check Read Access  # noqa: E501
        """
        pass

    def test_check_write_access(self):
        """Test case for check_write_access

        Check Write Access  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
