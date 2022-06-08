"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyjama
from pyjama.api.items_api import ItemsApi  # noqa: E501


class TestItemsApi(unittest.TestCase):
    """ItemsApi unit test stubs"""

    def setUp(self):
        self.api = ItemsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item(self):
        """Test case for add_item

        Create a new item  # noqa: E501
        """
        pass

    def test_add_item_attachment(self):
        """Test case for add_item_attachment

        Add an existing attachment to the item with the specified ID  # noqa: E501
        """
        pass

    def test_add_item_link(self):
        """Test case for add_item_link

        Create a new link for the item with the specified ID  # noqa: E501
        """
        pass

    def test_add_item_tag(self):
        """Test case for add_item_tag

        Add an existing tag to the item with the specified ID  # noqa: E501
        """
        pass

    def test_break_sync_on_item(self):
        """Test case for break_sync_on_item

        Remove an existing item from the Global ID pool of the item with the specified ID (break sync)  # noqa: E501
        """
        pass

    def test_connect_item_to_global_id_pool(self):
        """Test case for connect_item_to_global_id_pool

        Add an existing item to the Global ID pool of the item with the specified ID  # noqa: E501
        """
        pass

    def test_delete_item(self):
        """Test case for delete_item

        Delete the item with the specified ID (item becomes inactive and can be un-deleted if necessary)  # noqa: E501
        """
        pass

    def test_delete_item_link(self):
        """Test case for delete_item_link

        Delete the link with the specified ID  # noqa: E501
        """
        pass

    def test_duplicate_item(self):
        """Test case for duplicate_item

        Create a duplicate of item  # noqa: E501
        """
        pass

    def test_execute_transition(self):
        """Test case for execute_transition

        Executes a workflow transition for the item with the specified ID. Valid transitions can be found at /items/{id}/workflowtransitionoptions  # noqa: E501
        """
        pass

    def test_get_item(self):
        """Test case for get_item

        Get the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_activities(self):
        """Test case for get_item_activities

        Get all activities for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_attachments(self):
        """Test case for get_item_attachments

        Get all attachments for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_children(self):
        """Test case for get_item_children

        Get all children items for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_comments(self):
        """Test case for get_item_comments

        Get all comments for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_downstream_related(self):
        """Test case for get_item_downstream_related

        Get all downstream related items for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_downstream_relationships(self):
        """Test case for get_item_downstream_relationships

        Get all downstream relationships for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_link(self):
        """Test case for get_item_link

        Get the link with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_links(self):
        """Test case for get_item_links

        Get all links for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_location(self):
        """Test case for get_item_location

        Get the location for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_lock(self):
        """Test case for get_item_lock

        Get the locked state, last locked date, and last locked by user for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_parent(self):
        """Test case for get_item_parent

        Get the parent item for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_synced(self):
        """Test case for get_item_synced

        Get all synchronized items for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_synced_status(self):
        """Test case for get_item_synced_status

        Get the sync status for the synced item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_tag(self):
        """Test case for get_item_tag

        Get the tag with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_tags(self):
        """Test case for get_item_tags

        Get all tags for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_upstream_related(self):
        """Test case for get_item_upstream_related

        Get all upstream related items for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_upstream_relationships(self):
        """Test case for get_item_upstream_relationships

        Get all upstream relationships for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_version(self):
        """Test case for get_item_version

        Get the snapshot of the item at the specified version  # noqa: E501
        """
        pass

    def test_get_item_versioned(self):
        """Test case for get_item_versioned

        Get the numbered version for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_versions(self):
        """Test case for get_item_versions

        Get all versions for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_workflow_transition_options(self):
        """Test case for get_item_workflow_transition_options

        Get all valid workflow transitions that can be made on the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_items(self):
        """Test case for get_items

        Get all items in the project with the specified ID  # noqa: E501
        """
        pass

    def test_patch_item(self):
        """Test case for patch_item

        Update the item with the specified ID  # noqa: E501
        """
        pass

    def test_put_item(self):
        """Test case for put_item

        Update the item with the specified ID  # noqa: E501
        """
        pass

    def test_remove_attachment_from_item(self):
        """Test case for remove_attachment_from_item

        Remove an existing attachment from the item  # noqa: E501
        """
        pass

    def test_remove_tag_from_item(self):
        """Test case for remove_tag_from_item

        Remove an existing tag from the item with the specified ID  # noqa: E501
        """
        pass

    def test_update_item_link(self):
        """Test case for update_item_link

        Update the link with the specified ID  # noqa: E501
        """
        pass

    def test_update_item_location(self):
        """Test case for update_item_location

        Update the location for the item with the specified ID as an asynchronous request (a successful response signifies that the work was started and a work identifier is given. This identifier will be used in a future feature). Any child items are moved along with this item. Note that this currently only supports moving items between projects  # noqa: E501
        """
        pass

    def test_update_item_lock(self):
        """Test case for update_item_lock

        Update the locked state of the item with the specified ID  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
