"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.dataset import Dataset
from openapi_client.model.dataset_type import DatasetType
from openapi_client.model.template_resource import TemplateResource
globals()['Dataset'] = Dataset
globals()['DatasetType'] = DatasetType
globals()['TemplateResource'] = TemplateResource
from openapi_client.model.templated_dataset import TemplatedDataset


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