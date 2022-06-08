# pyjama.CommentsApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment**](CommentsApi.md#add_comment) | **POST** /comments | Create a new comment
[**get_comment**](CommentsApi.md#get_comment) | **GET** /comments/{id} | Get the comment with the specified ID
[**get_comment_replies**](CommentsApi.md#get_comment_replies) | **GET** /comments/{id}/replies | Get all reply comments for the comment with the specified ID
[**get_comments**](CommentsApi.md#get_comments) | **GET** /comments | Get all comments viewable by the current user


# **add_comment**
> CreatedResponse add_comment(body)

Create a new comment

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import comments_api
from pyjama.model.created_response import CreatedResponse
from pyjama.model.request_comment import RequestComment
from pprint import pprint
# Defining the host is optional and defaults to http://<jama_endpoint>/rest/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = pyjama.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure OAuth2 access token for authorization: oauth2
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyjama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    body = RequestComment(
        in_reply_to=1,
        body=RequestCommentBody(
            text="text_example",
        ),
        comment_type="GENERAL",
        location=RequestCommentLocation(
            item=1,
            project=1,
        ),
    ) # RequestComment | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new comment
        api_response = api_instance.add_comment(body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling CommentsApi->add_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestComment**](RequestComment.md)|  |

### Return type

[**CreatedResponse**](CreatedResponse.md)

### Authorization

[basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentDataWrapper get_comment(id)

Get the comment with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import comments_api
from pyjama.model.comment_data_wrapper import CommentDataWrapper
from pprint import pprint
# Defining the host is optional and defaults to http://<jama_endpoint>/rest/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = pyjama.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure OAuth2 access token for authorization: oauth2
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyjama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the comment with the specified ID
        api_response = api_instance.get_comment(id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling CommentsApi->get_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the comment with the specified ID
        api_response = api_instance.get_comment(id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling CommentsApi->get_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**CommentDataWrapper**](CommentDataWrapper.md)

### Authorization

[basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_replies**
> CommentDataListWrapper get_comment_replies(id)

Get all reply comments for the comment with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import comments_api
from pyjama.model.comment_data_list_wrapper import CommentDataListWrapper
from pprint import pprint
# Defining the host is optional and defaults to http://<jama_endpoint>/rest/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = pyjama.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure OAuth2 access token for authorization: oauth2
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyjama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all reply comments for the comment with the specified ID
        api_response = api_instance.get_comment_replies(id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling CommentsApi->get_comment_replies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all reply comments for the comment with the specified ID
        api_response = api_instance.get_comment_replies(id, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling CommentsApi->get_comment_replies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**CommentDataListWrapper**](CommentDataListWrapper.md)

### Authorization

[basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> CommentDataListWrapper get_comments()

Get all comments viewable by the current user

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import comments_api
from pyjama.model.comment_data_list_wrapper import CommentDataListWrapper
from pprint import pprint
# Defining the host is optional and defaults to http://<jama_endpoint>/rest/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = pyjama.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure OAuth2 access token for authorization: oauth2
configuration = pyjama.Configuration(
    host = "http://<jama_endpoint>/rest/latest"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyjama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comments_api.CommentsApi(api_client)
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    root_comments_only = False # bool | whether to show only root comments; true to get only root comments, without their comment replies (optional) if omitted the server will use the default value of False
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all comments viewable by the current user
        api_response = api_instance.get_comments(start_at=start_at, max_results=max_results, root_comments_only=root_comments_only, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling CommentsApi->get_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **root_comments_only** | **bool**| whether to show only root comments; true to get only root comments, without their comment replies | [optional] if omitted the server will use the default value of False
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**CommentDataListWrapper**](CommentDataListWrapper.md)

### Authorization

[basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

