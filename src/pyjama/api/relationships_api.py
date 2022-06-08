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
from ..model.created_response import CreatedResponse
from ..model.relationship_data_list_wrapper import RelationshipDataListWrapper
from ..model.relationship_data_wrapper import RelationshipDataWrapper
from ..model.request_relationship import RequestRelationship
from ..model_utils import check_allowed_values  # noqa: F401
from ..model_utils import (
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class RelationshipsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.clear_suspect_link_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractRestResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/relationships/{relationshipId}/suspect",
                "operation_id": "clear_suspect_link",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": ["relationship_id",],
                "required": ["relationship_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"relationship_id": (int,),},
                "attribute_map": {"relationship_id": "relationshipId",},
                "location_map": {"relationship_id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.create_relationship_endpoint = _Endpoint(
            settings={
                "response_type": (CreatedResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/relationships",
                "operation_id": "create_relationship",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": ["body",],
                "required": ["body",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"body": (RequestRelationship,),},
                "attribute_map": {},
                "location_map": {"body": "body",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.delete_relationship_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractRestResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/relationships/{relationshipId}",
                "operation_id": "delete_relationship",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": ["relationship_id",],
                "required": ["relationship_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"relationship_id": (int,),},
                "attribute_map": {"relationship_id": "relationshipId",},
                "location_map": {"relationship_id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_relationship_endpoint = _Endpoint(
            settings={
                "response_type": (RelationshipDataWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/relationships/{relationshipId}",
                "operation_id": "get_relationship",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["relationship_id", "include",],
                "required": ["relationship_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"relationship_id": (int,), "include": ([str],),},
                "attribute_map": {
                    "relationship_id": "relationshipId",
                    "include": "include",
                },
                "location_map": {"relationship_id": "path", "include": "query",},
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_relationships_endpoint = _Endpoint(
            settings={
                "response_type": (RelationshipDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/relationships",
                "operation_id": "get_relationships",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["project", "start_at", "max_results", "include",],
                "required": ["project",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "project": (int,),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "project": "project",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "project": "query",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.update_relationship_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractRestResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/relationships/{relationshipId}",
                "operation_id": "update_relationship",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": ["relationship_id", "body",],
                "required": ["relationship_id", "body",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "relationship_id": (int,),
                    "body": (RequestRelationship,),
                },
                "attribute_map": {"relationship_id": "relationshipId",},
                "location_map": {"relationship_id": "path", "body": "body",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )

    def clear_suspect_link(self, relationship_id, **kwargs):
        """Remove an existing suspect link for the relationship with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_suspect_link(relationship_id, async_req=True)
        >>> result = thread.get()

        Args:
            relationship_id (int):

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
        kwargs["relationship_id"] = relationship_id
        return self.clear_suspect_link_endpoint.call_with_http_info(**kwargs)

    def create_relationship(self, body, **kwargs):
        """Create a new relationship  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_relationship(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (RequestRelationship):

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
            CreatedResponse
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
        kwargs["body"] = body
        return self.create_relationship_endpoint.call_with_http_info(**kwargs)

    def delete_relationship(self, relationship_id, **kwargs):
        """Delete the relationship with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_relationship(relationship_id, async_req=True)
        >>> result = thread.get()

        Args:
            relationship_id (int):

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
        kwargs["relationship_id"] = relationship_id
        return self.delete_relationship_endpoint.call_with_http_info(**kwargs)

    def get_relationship(self, relationship_id, **kwargs):
        """Get the relationship with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_relationship(relationship_id, async_req=True)
        >>> result = thread.get()

        Args:
            relationship_id (int):

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
            RelationshipDataWrapper
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
        kwargs["relationship_id"] = relationship_id
        return self.get_relationship_endpoint.call_with_http_info(**kwargs)

    def get_relationships(self, project, **kwargs):
        """Get all relationships in the project with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_relationships(project, async_req=True)
        >>> result = thread.get()

        Args:
            project (int):

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
            RelationshipDataListWrapper
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
        return self.get_relationships_endpoint.call_with_http_info(**kwargs)

    def update_relationship(self, relationship_id, body, **kwargs):
        """Update the relationship with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_relationship(relationship_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            relationship_id (int):
            body (RequestRelationship):

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
        kwargs["relationship_id"] = relationship_id
        kwargs["body"] = body
        return self.update_relationship_endpoint.call_with_http_info(**kwargs)
