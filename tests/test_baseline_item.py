"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyjama
from pyjama.model.allowed_resource import AllowedResource
from pyjama.model.baseline_location import BaselineLocation

globals()["AllowedResource"] = AllowedResource
globals()["BaselineLocation"] = BaselineLocation
from pyjama.model.baseline_item import BaselineItem


class TestBaselineItem(unittest.TestCase):
    """BaselineItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBaselineItem(self):
        """Test BaselineItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BaselineItem()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
