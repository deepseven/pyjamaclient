"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyjama
from pyjama.api.releases_api import ReleasesApi  # noqa: E501


class TestReleasesApi(unittest.TestCase):
    """ReleasesApi unit test stubs"""

    def setUp(self):
        self.api = ReleasesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_release(self):
        """Test case for add_release

        Create a new release  # noqa: E501
        """
        pass

    def test_get_release(self):
        """Test case for get_release

        Get the release with the specified ID  # noqa: E501
        """
        pass

    def test_get_releases(self):
        """Test case for get_releases

        Get all releases in the project with the specified ID  # noqa: E501
        """
        pass

    def test_put_release(self):
        """Test case for put_release

        Update the release with the specified ID  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
