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
from pyjama.model.meta_wrapper import MetaWrapper
from pyjama.model.user_group import UserGroup

globals()["Link"] = Link
globals()["MetaWrapper"] = MetaWrapper
globals()["UserGroup"] = UserGroup
from pyjama.model.user_group_data_wrapper import UserGroupDataWrapper


class TestUserGroupDataWrapper(unittest.TestCase):
    """UserGroupDataWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserGroupDataWrapper(self):
        """Test UserGroupDataWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserGroupDataWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
