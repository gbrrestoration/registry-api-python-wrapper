"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.model.dataset import Dataset
from rrap_mds_is_registry_api.model.dataset_type import DatasetType
from rrap_mds_is_registry_api.model.template_resource import TemplateResource
globals()['Dataset'] = Dataset
globals()['DatasetType'] = DatasetType
globals()['TemplateResource'] = TemplateResource
from rrap_mds_is_registry_api.model.templated_dataset import TemplatedDataset


class TestTemplatedDataset(unittest.TestCase):
    """TemplatedDataset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTemplatedDataset(self):
        """Test TemplatedDataset"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TemplatedDataset()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
