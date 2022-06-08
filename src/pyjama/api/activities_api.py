"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ..api_client import ApiClient
from ..api_client import Endpoint as _Endpoint
from ..model.abstract_rest_response import AbstractRestResponse
from ..model.activity_data_list_wrapper import ActivityDataListWrapper
from ..model.activity_data_wrapper import ActivityDataWrapper
from ..model.item_data_list_wrapper import ItemDataListWrapper
from ..model_utils import check_allowed_values  # noqa: F401
from ..model_utils import (
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class ActivitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_activit_affected_items_endpoint = _Endpoint(
            settings={
                "response_type": (ItemDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/activities/{activityId}/affecteditems",
                "operation_id": "get_activit_affected_items",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["activity_id", "start_at", "max_results", "include",],
                "required": ["activity_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "activity_id": (int,),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "activity_id": "activityId",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "activity_id": "path",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_activities_endpoint = _Endpoint(
            settings={
                "response_type": (ActivityDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/activities",
                "operation_id": "get_activities",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "project",
                    "event_type",
                    "object_type",
                    "item_type",
                    "date",
                    "delete_events",
                    "start_at",
                    "max_results",
                    "include",
                ],
                "required": ["project",],
                "nullable": [],
                "enum": ["event_type", "object_type",],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("event_type",): {
                        "CREATE": "CREATE",
                        "UPDATE": "UPDATE",
                        "DELETE": "DELETE",
                        "PUBLIC": "PUBLIC",
                        "BATCH_SUMMARY": "BATCH_SUMMARY",
                    },
                    ("object_type",): {
                        "PROJECT": "PROJECT",
                        "ITEM": "ITEM",
                        "USER": "USER",
                        "RELATIONSHIP": "RELATIONSHIP",
                        "COMMENT": "COMMENT",
                        "ITEM_TAG": "ITEM_TAG",
                        "TAG": "TAG",
                        "ITEM_ATTACHMENT": "ITEM_ATTACHMENT",
                        "URL": "URL",
                        "TEST_RESULT": "TEST_RESULT",
                        "BASELINE": "BASELINE",
                        "CHANGE_REQUEST": "CHANGE_REQUEST",
                        "REVIEW": "REVIEW",
                        "REVISION": "REVISION",
                        "REVISION_ITEM": "REVISION_ITEM",
                        "TEST_PLAN": "TEST_PLAN",
                        "TEST_CYCLE": "TEST_CYCLE",
                        "TEST_RUN": "TEST_RUN",
                        "INTEGRATION": "INTEGRATION",
                        "MISCELLANEOUS": "MISCELLANEOUS",
                    },
                },
                "openapi_types": {
                    "project": (int,),
                    "event_type": ([str],),
                    "object_type": ([str],),
                    "item_type": ([int],),
                    "date": ([str],),
                    "delete_events": (bool,),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "project": "project",
                    "event_type": "eventType",
                    "object_type": "objectType",
                    "item_type": "itemType",
                    "date": "date",
                    "delete_events": "deleteEvents",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "project": "query",
                    "event_type": "query",
                    "object_type": "query",
                    "item_type": "query",
                    "date": "query",
                    "delete_events": "query",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {
                    "event_type": "multi",
                    "object_type": "multi",
                    "item_type": "multi",
                    "date": "multi",
                    "include": "multi",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_activity_endpoint = _Endpoint(
            settings={
                "response_type": (ActivityDataWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/activities/{activityId}",
                "operation_id": "get_activity",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["activity_id", "include",],
                "required": ["activity_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"activity_id": (int,), "include": ([str],),},
                "attribute_map": {"activity_id": "activityId", "include": "include",},
                "location_map": {"activity_id": "path", "include": "query",},
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.restore_items_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractRestResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/activities/{activityId}/restore",
                "operation_id": "restore_items",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": ["activity_id",],
                "required": ["activity_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"activity_id": (int,),},
                "attribute_map": {"activity_id": "activityId",},
                "location_map": {"activity_id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )

    def get_activit_affected_items(self, activity_id, **kwargs):
        """Get all items affected by the activity with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_activit_affected_items(activity_id, async_req=True)
        >>> result = thread.get()

        Args:
            activity_id (int):

        Keyword Args:
            start_at (int): [optional]
            max_results (int): If not set, this defaults to 20. This cannot be larger than 50. [optional]
            include ([str]): Links to include as full objects in the linked map. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ItemDataListWrapper
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["activity_id"] = activity_id
        return self.get_activit_affected_items_endpoint.call_with_http_info(**kwargs)

    def get_activities(self, project, **kwargs):
        """Get all activities in the project with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_activities(project, async_req=True)
        >>> result = thread.get()

        Args:
            project (int):

        Keyword Args:
            event_type ([str]): Event type to filter on. More than one event type can be chosen. [optional]
            object_type ([str]): Object type to filter on. More than one object type can be chosen. [optional]
            item_type ([int]): ID of item type to filter on. More than one item type can be chosen. [optional]
            date ([str]): Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\". [optional]
            delete_events (bool): Get item delete events only. [optional]
            start_at (int): [optional]
            max_results (int): If not set, this defaults to 20. This cannot be larger than 50. [optional]
            include ([str]): Links to include as full objects in the linked map. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ActivityDataListWrapper
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["project"] = project
        return self.get_activities_endpoint.call_with_http_info(**kwargs)

    def get_activity(self, activity_id, **kwargs):
        """Get the activity with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_activity(activity_id, async_req=True)
        >>> result = thread.get()

        Args:
            activity_id (int):

        Keyword Args:
            include ([str]): Links to include as full objects in the linked map. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ActivityDataWrapper
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["activity_id"] = activity_id
        return self.get_activity_endpoint.call_with_http_info(**kwargs)

    def restore_items(self, activity_id, **kwargs):
        """Restore item(s) associated with a delete activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.restore_items(activity_id, async_req=True)
        >>> result = thread.get()

        Args:
            activity_id (int):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            AbstractRestResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["activity_id"] = activity_id
        return self.restore_items_endpoint.call_with_http_info(**kwargs)
