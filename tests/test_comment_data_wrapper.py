"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyjama
from pyjama.model.comment import Comment
from pyjama.model.link import Link
from pyjama.model.meta_wrapper import MetaWrapper

globals()["Comment"] = Comment
globals()["Link"] = Link
globals()["MetaWrapper"] = MetaWrapper
from pyjama.model.comment_data_wrapper import CommentDataWrapper


class TestCommentDataWrapper(unittest.TestCase):
    """CommentDataWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommentDataWrapper(self):
        """Test CommentDataWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommentDataWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
