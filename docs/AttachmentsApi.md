# pyjama.AttachmentsApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_file**](AttachmentsApi.md#download_file) | **GET** /attachments/{attachmentId}/file | Download attachment file from the attachment with the specified ID
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /attachments/{attachmentId} | Get the attachment with the specified ID
[**get_attachment_comments**](AttachmentsApi.md#get_attachment_comments) | **GET** /attachments/{attachmentId}/comments | Get all comments for the item with the specified ID
[**get_attachment_lock**](AttachmentsApi.md#get_attachment_lock) | **GET** /attachments/{attachmentId}/lock | Get the locked state, last locked date, and last locked by user for the item with the specified ID
[**get_attachment_version**](AttachmentsApi.md#get_attachment_version) | **GET** /attachments/{attachmentId}/versions/{versionNum}/versioneditem | Get the  snapshot of the attachment at the specified version
[**get_attachment_versioned**](AttachmentsApi.md#get_attachment_versioned) | **GET** /attachments/{attachmentId}/versions/{versionNum} | Get the numbered version for the item with the specified ID
[**get_attachment_versions**](AttachmentsApi.md#get_attachment_versions) | **GET** /attachments/{attachmentId}/versions | Get all versions for the item with the specified ID
[**update_attachment_lock**](AttachmentsApi.md#update_attachment_lock) | **PUT** /attachments/{attachmentId}/lock | Update the locked state of the item with the specified ID
[**upload_file**](AttachmentsApi.md#upload_file) | **PUT** /attachments/{attachmentId}/file | Upload attachment file to the attachment with the specified ID


# **download_file**
> download_file(attachment_id)

Download attachment file from the attachment with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Download attachment file from the attachment with the specified ID
        api_instance.download_file(attachment_id)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentDataWrapper get_attachment(attachment_id)

Get the attachment with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
from pyjama.model.attachment_data_wrapper import AttachmentDataWrapper
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the attachment with the specified ID
        api_response = api_instance.get_attachment(attachment_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the attachment with the specified ID
        api_response = api_instance.get_attachment(attachment_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**AttachmentDataWrapper**](AttachmentDataWrapper.md)

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

# **get_attachment_comments**
> CommentDataListWrapper get_attachment_comments(attachment_id)

Get all comments for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    root_comments_only = False # bool |  (optional) if omitted the server will use the default value of False
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all comments for the item with the specified ID
        api_response = api_instance.get_attachment_comments(attachment_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_comments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all comments for the item with the specified ID
        api_response = api_instance.get_attachment_comments(attachment_id, start_at=start_at, max_results=max_results, root_comments_only=root_comments_only, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **root_comments_only** | **bool**|  | [optional] if omitted the server will use the default value of False
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

# **get_attachment_lock**
> LockDataWrapper get_attachment_lock(attachment_id)

Get the locked state, last locked date, and last locked by user for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
from pyjama.model.lock_data_wrapper import LockDataWrapper
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the locked state, last locked date, and last locked by user for the item with the specified ID
        api_response = api_instance.get_attachment_lock(attachment_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_lock: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the locked state, last locked date, and last locked by user for the item with the specified ID
        api_response = api_instance.get_attachment_lock(attachment_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**LockDataWrapper**](LockDataWrapper.md)

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

# **get_attachment_version**
> VersionedAttachmentDataWrapper get_attachment_version(version_num, attachment_id)

Get the  snapshot of the attachment at the specified version

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
from pyjama.model.versioned_attachment_data_wrapper import VersionedAttachmentDataWrapper
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    version_num = 1 # int | 
    attachment_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the  snapshot of the attachment at the specified version
        api_response = api_instance.get_attachment_version(version_num, attachment_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the  snapshot of the attachment at the specified version
        api_response = api_instance.get_attachment_version(version_num, attachment_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **int**|  |
 **attachment_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**VersionedAttachmentDataWrapper**](VersionedAttachmentDataWrapper.md)

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

# **get_attachment_versioned**
> VersionDataWrapper get_attachment_versioned(version_num, attachment_id)

Get the numbered version for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
from pyjama.model.version_data_wrapper import VersionDataWrapper
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    version_num = 1 # int | 
    attachment_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the numbered version for the item with the specified ID
        api_response = api_instance.get_attachment_versioned(version_num, attachment_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_versioned: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the numbered version for the item with the specified ID
        api_response = api_instance.get_attachment_versioned(version_num, attachment_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_versioned: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **int**|  |
 **attachment_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**VersionDataWrapper**](VersionDataWrapper.md)

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

# **get_attachment_versions**
> VersionDataListWrapper get_attachment_versions(attachment_id)

Get all versions for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
from pyjama.model.version_data_list_wrapper import VersionDataListWrapper
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all versions for the item with the specified ID
        api_response = api_instance.get_attachment_versions(attachment_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all versions for the item with the specified ID
        api_response = api_instance.get_attachment_versions(attachment_id, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachment_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**VersionDataListWrapper**](VersionDataListWrapper.md)

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

# **update_attachment_lock**
> AbstractRestResponse update_attachment_lock(attachment_id, body)

Update the locked state of the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
from pyjama.model.request_lock import RequestLock
from pyjama.model.abstract_rest_response import AbstractRestResponse
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = 1 # int | 
    body = RequestLock(
        locked=True,
    ) # RequestLock | 

    # example passing only required values which don't have defaults set
    try:
        # Update the locked state of the item with the specified ID
        api_response = api_instance.update_attachment_lock(attachment_id, body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->update_attachment_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  |
 **body** | [**RequestLock**](RequestLock.md)|  |

### Return type

[**AbstractRestResponse**](AbstractRestResponse.md)

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

# **upload_file**
> AbstractRestResponse upload_file(attachment_id)

Upload attachment file to the attachment with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import attachments_api
from pyjama.model.body_part import BodyPart
from pyjama.model.content_disposition import ContentDisposition
from pyjama.model.media_type import MediaType
from pyjama.model.multi_part import MultiPart
from pyjama.model.abstract_rest_response import AbstractRestResponse
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    attachment_id = 1 # int | 
    content_disposition = ContentDisposition(
        type="type_example",
        parameters={
            "key": "key_example",
        },
        file_name="file_name_example",
        creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        modification_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        read_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        size=1,
    ) # ContentDisposition |  (optional)
    entity = {} # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    media_type = MediaType(
        type="type_example",
        subtype="subtype_example",
        parameters={
            "key": "key_example",
        },
        wildcard_type=True,
        wildcard_subtype=True,
    ) # MediaType |  (optional)
    message_body_workers = {} # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    parent = MultiPart(
        content_disposition=ContentDisposition(
            type="type_example",
            parameters={
                "key": "key_example",
            },
            file_name="file_name_example",
            creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            modification_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            read_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            size=1,
        ),
        entity={},
        headers={
            "key": [
                "key_example",
            ],
        },
        media_type=MediaType(
            type="type_example",
            subtype="subtype_example",
            parameters={
                "key": "key_example",
            },
            wildcard_type=True,
            wildcard_subtype=True,
        ),
        message_body_workers={},
        parent=MultiPart(),
        providers={},
        body_parts=[
            BodyPart(
                content_disposition=ContentDisposition(
                    type="type_example",
                    parameters={
                        "key": "key_example",
                    },
                    file_name="file_name_example",
                    creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    modification_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    read_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    size=1,
                ),
                entity={},
                headers={
                    "key": [
                        "key_example",
                    ],
                },
                media_type=MediaType(
                    type="type_example",
                    subtype="subtype_example",
                    parameters={
                        "key": "key_example",
                    },
                    wildcard_type=True,
                    wildcard_subtype=True,
                ),
                message_body_workers={},
                parent=MultiPart(),
                providers={},
                parameterized_headers={
                    "key": [
                        ParameterizedHeader(
                            value="value_example",
                            parameters={
                                "key": "key_example",
                            },
                        ),
                    ],
                },
            ),
        ],
        parameterized_headers={
            "key": [
                ParameterizedHeader(
                    value="value_example",
                    parameters={
                        "key": "key_example",
                    },
                ),
            ],
        },
    ) # MultiPart |  (optional)
    providers = {} # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    body_parts = [
        BodyPart(
            content_disposition=ContentDisposition(
                type="type_example",
                parameters={
                    "key": "key_example",
                },
                file_name="file_name_example",
                creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                modification_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                read_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                size=1,
            ),
            entity={},
            headers={
                "key": [
                    "key_example",
                ],
            },
            media_type=MediaType(
                type="type_example",
                subtype="subtype_example",
                parameters={
                    "key": "key_example",
                },
                wildcard_type=True,
                wildcard_subtype=True,
            ),
            message_body_workers={},
            parent=MultiPart(
                content_disposition=ContentDisposition(
                    type="type_example",
                    parameters={
                        "key": "key_example",
                    },
                    file_name="file_name_example",
                    creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    modification_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    read_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    size=1,
                ),
                entity={},
                headers={
                    "key": [
                        "key_example",
                    ],
                },
                media_type=MediaType(
                    type="type_example",
                    subtype="subtype_example",
                    parameters={
                        "key": "key_example",
                    },
                    wildcard_type=True,
                    wildcard_subtype=True,
                ),
                message_body_workers={},
                parent=MultiPart(),
                providers={},
                body_parts=[],
                parameterized_headers={
                    "key": [
                        ParameterizedHeader(
                            value="value_example",
                            parameters={
                                "key": "key_example",
                            },
                        ),
                    ],
                },
            ),
            providers={},
            parameterized_headers={
                "key": [
                    ParameterizedHeader(
                        value="value_example",
                        parameters={
                            "key": "key_example",
                        },
                    ),
                ],
            },
        ),
    ] # [BodyPart] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload attachment file to the attachment with the specified ID
        api_response = api_instance.upload_file(attachment_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->upload_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload attachment file to the attachment with the specified ID
        api_response = api_instance.upload_file(attachment_id, content_disposition=content_disposition, entity=entity, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AttachmentsApi->upload_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  |
 **content_disposition** | [**ContentDisposition**](ContentDisposition.md)|  | [optional]
 **entity** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **media_type** | [**MediaType**](MediaType.md)|  | [optional]
 **message_body_workers** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **parent** | [**MultiPart**](MultiPart.md)|  | [optional]
 **providers** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **body_parts** | [**[BodyPart]**](BodyPart.md)|  | [optional]

### Return type

[**AbstractRestResponse**](AbstractRestResponse.md)

### Authorization

[basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

