"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyjama
from pyjama.api.tags_api import TagsApi  # noqa: E501


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_tag(self):
        """Test case for add_tag

        Create a new tag in the project with the specified ID  # noqa: E501
        """
        pass

    def test_delete_tag(self):
        """Test case for delete_tag

        Delete the tag with the specified ID  # noqa: E501
        """
        pass

    def test_get_tag(self):
        """Test case for get_tag

        Get the tag with the specified ID  # noqa: E501
        """
        pass

    def test_get_tag_items(self):
        """Test case for get_tag_items

        Get all items that have the tag with the specified ID  # noqa: E501
        """
        pass

    def test_get_tags(self):
        """Test case for get_tags

        Get all tags for the project with the specified ID  # noqa: E501
        """
        pass

    def test_put_tag(self):
        """Test case for put_tag

        Update the tag with the specified ID  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
