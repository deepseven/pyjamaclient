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
from pyjama.model.relationship_type import RelationshipType

globals()["Link"] = Link
globals()["MetaListWrapper"] = MetaListWrapper
globals()["RelationshipType"] = RelationshipType
from pyjama.model.relationship_type_data_list_wrapper import (
    RelationshipTypeDataListWrapper,
)


class TestRelationshipTypeDataListWrapper(unittest.TestCase):
    """RelationshipTypeDataListWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRelationshipTypeDataListWrapper(self):
        """Test RelationshipTypeDataListWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RelationshipTypeDataListWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
