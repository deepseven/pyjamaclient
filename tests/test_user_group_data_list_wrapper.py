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
from pyjama.model.user_group import UserGroup

globals()["Link"] = Link
globals()["MetaListWrapper"] = MetaListWrapper
globals()["UserGroup"] = UserGroup
from pyjama.model.user_group_data_list_wrapper import UserGroupDataListWrapper


class TestUserGroupDataListWrapper(unittest.TestCase):
    """UserGroupDataListWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserGroupDataListWrapper(self):
        """Test UserGroupDataListWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserGroupDataListWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
