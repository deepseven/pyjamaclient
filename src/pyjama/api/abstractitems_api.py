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
from ..model.abstract_item_data_wrapper import AbstractItemDataWrapper
from ..model.abstract_versioned_item_data_wrapper import (
    AbstractVersionedItemDataWrapper,
)
from ..model.item_data_list_wrapper import ItemDataListWrapper
from ..model.version_data_list_wrapper import VersionDataListWrapper
from ..model.version_data_wrapper import VersionDataWrapper
from ..model.versioned_relationship_data_list_wrapper import (
    VersionedRelationshipDataListWrapper,
)
from ..model_utils import check_allowed_values  # noqa: F401
from ..model_utils import (
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class AbstractitemsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_abstract_item_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractItemDataWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/abstractitems/{id}",
                "operation_id": "get_abstract_item",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["id", "include",],
                "required": ["id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"id": (int,), "include": ([str],),},
                "attribute_map": {"id": "id", "include": "include",},
                "location_map": {"id": "path", "include": "query",},
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_abstract_item_version_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractVersionedItemDataWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/abstractitems/{id}/versions/{versionNum}/versioneditem",
                "operation_id": "get_abstract_item_version",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["version_num", "id", "include",],
                "required": ["version_num", "id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "version_num": (int,),
                    "id": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "version_num": "versionNum",
                    "id": "id",
                    "include": "include",
                },
                "location_map": {
                    "version_num": "path",
                    "id": "path",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_abstract_item_versioned_endpoint = _Endpoint(
            settings={
                "response_type": (VersionDataWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/abstractitems/{id}/versions/{versionNum}",
                "operation_id": "get_abstract_item_versioned",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["version_num", "id", "include",],
                "required": ["version_num", "id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "version_num": (int,),
                    "id": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "version_num": "versionNum",
                    "id": "id",
                    "include": "include",
                },
                "location_map": {
                    "version_num": "path",
                    "id": "path",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_abstract_item_versioned_relationships_endpoint = _Endpoint(
            settings={
                "response_type": (VersionedRelationshipDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/abstractitems/{id}/versionedrelationships",
                "operation_id": "get_abstract_item_versioned_relationships",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["id", "timestamp", "start_at", "max_results", "include",],
                "required": ["id", "timestamp",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (int,),
                    "timestamp": (str,),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "id": "id",
                    "timestamp": "timestamp",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "id": "path",
                    "timestamp": "query",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_abstract_item_versions_endpoint = _Endpoint(
            settings={
                "response_type": (VersionDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/abstractitems/{id}/versions",
                "operation_id": "get_abstract_item_versions",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["id", "start_at", "max_results", "include",],
                "required": ["id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (int,),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "id": "id",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "id": "path",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_abstract_items_endpoint = _Endpoint(
            settings={
                "response_type": (ItemDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/abstractitems",
                "operation_id": "get_abstract_items",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "project",
                    "item_type",
                    "document_key",
                    "release",
                    "created_date",
                    "modified_date",
                    "last_activity_date",
                    "contains",
                    "sort_by",
                    "start_at",
                    "max_results",
                    "include",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "project": ([int],),
                    "item_type": ([int],),
                    "document_key": ([str],),
                    "release": ([int],),
                    "created_date": ([str],),
                    "modified_date": ([str],),
                    "last_activity_date": ([str],),
                    "contains": ([str],),
                    "sort_by": ([str],),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "project": "project",
                    "item_type": "itemType",
                    "document_key": "documentKey",
                    "release": "release",
                    "created_date": "createdDate",
                    "modified_date": "modifiedDate",
                    "last_activity_date": "lastActivityDate",
                    "contains": "contains",
                    "sort_by": "sortBy",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "project": "query",
                    "item_type": "query",
                    "document_key": "query",
                    "release": "query",
                    "created_date": "query",
                    "modified_date": "query",
                    "last_activity_date": "query",
                    "contains": "query",
                    "sort_by": "query",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {
                    "project": "multi",
                    "item_type": "multi",
                    "document_key": "multi",
                    "release": "multi",
                    "created_date": "multi",
                    "modified_date": "multi",
                    "last_activity_date": "multi",
                    "contains": "multi",
                    "sort_by": "multi",
                    "include": "multi",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )

    def get_abstract_item(self, id, **kwargs):
        """Get any item, test plan, test cycle, test run, or attachment with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abstract_item(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):

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
            AbstractItemDataWrapper
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
        kwargs["id"] = id
        return self.get_abstract_item_endpoint.call_with_http_info(**kwargs)

    def get_abstract_item_version(self, version_num, id, **kwargs):
        """Get the  snapshot of the item at the specified version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abstract_item_version(version_num, id, async_req=True)
        >>> result = thread.get()

        Args:
            version_num (int):
            id (int):

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
            AbstractVersionedItemDataWrapper
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
        kwargs["version_num"] = version_num
        kwargs["id"] = id
        return self.get_abstract_item_version_endpoint.call_with_http_info(**kwargs)

    def get_abstract_item_versioned(self, version_num, id, **kwargs):
        """Get the numbered version for the item with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abstract_item_versioned(version_num, id, async_req=True)
        >>> result = thread.get()

        Args:
            version_num (int):
            id (int):

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
            VersionDataWrapper
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
        kwargs["version_num"] = version_num
        kwargs["id"] = id
        return self.get_abstract_item_versioned_endpoint.call_with_http_info(**kwargs)

    def get_abstract_item_versioned_relationships(self, id, timestamp, **kwargs):
        """Get all versioned relationships that were associated to the item at the specified time  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abstract_item_versioned_relationships(id, timestamp, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):
            timestamp (str): Get relationships for the specified item at this date and time. Requires ISO8601 formatting (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\"

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
            VersionedRelationshipDataListWrapper
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
        kwargs["id"] = id
        kwargs["timestamp"] = timestamp
        return self.get_abstract_item_versioned_relationships_endpoint.call_with_http_info(
            **kwargs
        )

    def get_abstract_item_versions(self, id, **kwargs):
        """Get all versions for the item with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abstract_item_versions(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):

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
            VersionDataListWrapper
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
        kwargs["id"] = id
        return self.get_abstract_item_versions_endpoint.call_with_http_info(**kwargs)

    def get_abstract_items(self, **kwargs):
        """Search for items, test plans, test cycles, test runs, or attachments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abstract_items(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            project ([int]): [optional]
            item_type ([int]): [optional]
            document_key ([str]): [optional]
            release ([int]): [optional]
            created_date ([str]): Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\". [optional]
            modified_date ([str]): Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\". [optional]
            last_activity_date ([str]): Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\". [optional]
            contains ([str]): Filter on the text contents of the item. Strings taken literally. Multiple 'contains' values will be bitwise ORed.. [optional]
            sort_by ([str]): Sort orders can be added with the name of the field by which to sort, followed by .asc or .desc (e.g. 'name.asc' or 'modifiedDate.desc'). If not set, this defaults to sorting by sequence.asc and then documentKey.asc. [optional]
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
        return self.get_abstract_items_endpoint.call_with_http_info(**kwargs)
