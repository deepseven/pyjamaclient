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
from pyjama.model.sync_status import SyncStatus

globals()["Link"] = Link
globals()["MetaWrapper"] = MetaWrapper
globals()["SyncStatus"] = SyncStatus
from pyjama.model.sync_status_data_wrapper import SyncStatusDataWrapper


class TestSyncStatusDataWrapper(unittest.TestCase):
    """SyncStatusDataWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyncStatusDataWrapper(self):
        """Test SyncStatusDataWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyncStatusDataWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
