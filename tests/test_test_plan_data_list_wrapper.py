"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyjama
from pyjama.model.link import Link
from pyjama.model.meta_list_wrapper import MetaListWrapper
from pyjama.model.test_plan import TestPlan

globals()["Link"] = Link
globals()["MetaListWrapper"] = MetaListWrapper
globals()["TestPlan"] = TestPlan
from pyjama.model.test_plan_data_list_wrapper import TestPlanDataListWrapper


class TestTestPlanDataListWrapper(unittest.TestCase):
    """TestPlanDataListWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTestPlanDataListWrapper(self):
        """Test TestPlanDataListWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TestPlanDataListWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
