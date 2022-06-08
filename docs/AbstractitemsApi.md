# pyjama.AbstractitemsApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_abstract_item**](AbstractitemsApi.md#get_abstract_item) | **GET** /abstractitems/{id} | Get any item, test plan, test cycle, test run, or attachment with the specified ID
[**get_abstract_item_version**](AbstractitemsApi.md#get_abstract_item_version) | **GET** /abstractitems/{id}/versions/{versionNum}/versioneditem | Get the  snapshot of the item at the specified version
[**get_abstract_item_versioned**](AbstractitemsApi.md#get_abstract_item_versioned) | **GET** /abstractitems/{id}/versions/{versionNum} | Get the numbered version for the item with the specified ID
[**get_abstract_item_versioned_relationships**](AbstractitemsApi.md#get_abstract_item_versioned_relationships) | **GET** /abstractitems/{id}/versionedrelationships | Get all versioned relationships that were associated to the item at the specified time
[**get_abstract_item_versions**](AbstractitemsApi.md#get_abstract_item_versions) | **GET** /abstractitems/{id}/versions | Get all versions for the item with the specified ID
[**get_abstract_items**](AbstractitemsApi.md#get_abstract_items) | **GET** /abstractitems | Search for items, test plans, test cycles, test runs, or attachments


# **get_abstract_item**
> AbstractItemDataWrapper get_abstract_item(id)

Get any item, test plan, test cycle, test run, or attachment with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import abstractitems_api
from pyjama.model.abstract_item_data_wrapper import AbstractItemDataWrapper
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
    api_instance = abstractitems_api.AbstractitemsApi(api_client)
    id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get any item, test plan, test cycle, test run, or attachment with the specified ID
        api_response = api_instance.get_abstract_item(id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get any item, test plan, test cycle, test run, or attachment with the specified ID
        api_response = api_instance.get_abstract_item(id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**AbstractItemDataWrapper**](AbstractItemDataWrapper.md)

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

# **get_abstract_item_version**
> AbstractVersionedItemDataWrapper get_abstract_item_version(version_num, id)

Get the  snapshot of the item at the specified version

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import abstractitems_api
from pyjama.model.abstract_versioned_item_data_wrapper import AbstractVersionedItemDataWrapper
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
    api_instance = abstractitems_api.AbstractitemsApi(api_client)
    version_num = 1 # int | 
    id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the  snapshot of the item at the specified version
        api_response = api_instance.get_abstract_item_version(version_num, id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the  snapshot of the item at the specified version
        api_response = api_instance.get_abstract_item_version(version_num, id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **int**|  |
 **id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**AbstractVersionedItemDataWrapper**](AbstractVersionedItemDataWrapper.md)

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

# **get_abstract_item_versioned**
> VersionDataWrapper get_abstract_item_versioned(version_num, id)

Get the numbered version for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import abstractitems_api
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
    api_instance = abstractitems_api.AbstractitemsApi(api_client)
    version_num = 1 # int | 
    id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the numbered version for the item with the specified ID
        api_response = api_instance.get_abstract_item_versioned(version_num, id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_versioned: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the numbered version for the item with the specified ID
        api_response = api_instance.get_abstract_item_versioned(version_num, id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_versioned: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **int**|  |
 **id** | **int**|  |
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

# **get_abstract_item_versioned_relationships**
> VersionedRelationshipDataListWrapper get_abstract_item_versioned_relationships(id, timestamp)

Get all versioned relationships that were associated to the item at the specified time

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import abstractitems_api
from pyjama.model.versioned_relationship_data_list_wrapper import VersionedRelationshipDataListWrapper
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
    api_instance = abstractitems_api.AbstractitemsApi(api_client)
    id = 1 # int | 
    timestamp = "timestamp_example" # str | Get relationships for the specified item at this date and time. Requires ISO8601 formatting (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\"
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all versioned relationships that were associated to the item at the specified time
        api_response = api_instance.get_abstract_item_versioned_relationships(id, timestamp)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_versioned_relationships: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all versioned relationships that were associated to the item at the specified time
        api_response = api_instance.get_abstract_item_versioned_relationships(id, timestamp, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_versioned_relationships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **timestamp** | **str**| Get relationships for the specified item at this date and time. Requires ISO8601 formatting (milliseconds or seconds) - \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot; or \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**VersionedRelationshipDataListWrapper**](VersionedRelationshipDataListWrapper.md)

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

# **get_abstract_item_versions**
> VersionDataListWrapper get_abstract_item_versions(id)

Get all versions for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import abstractitems_api
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
    api_instance = abstractitems_api.AbstractitemsApi(api_client)
    id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all versions for the item with the specified ID
        api_response = api_instance.get_abstract_item_versions(id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all versions for the item with the specified ID
        api_response = api_instance.get_abstract_item_versions(id, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_item_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
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

# **get_abstract_items**
> ItemDataListWrapper get_abstract_items()

Search for items, test plans, test cycles, test runs, or attachments

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import abstractitems_api
from pyjama.model.item_data_list_wrapper import ItemDataListWrapper
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
    api_instance = abstractitems_api.AbstractitemsApi(api_client)
    project = [
        1,
    ] # [int] |  (optional)
    item_type = [
        1,
    ] # [int] |  (optional)
    document_key = [
        "documentKey_example",
    ] # [str] |  (optional)
    release = [
        1,
    ] # [int] |  (optional)
    created_date = [
        "createdDate_example",
    ] # [str] | Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\" (optional)
    modified_date = [
        "modifiedDate_example",
    ] # [str] | Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\" (optional)
    last_activity_date = [
        "lastActivityDate_example",
    ] # [str] | Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" or \"yyyy-MM-dd'T'HH:mm:ssZ\" (optional)
    contains = [
        "contains_example",
    ] # [str] | Filter on the text contents of the item. Strings taken literally. Multiple 'contains' values will be bitwise ORed. (optional)
    sort_by = [
        "sortBy_example",
    ] # [str] | Sort orders can be added with the name of the field by which to sort, followed by .asc or .desc (e.g. 'name.asc' or 'modifiedDate.desc'). If not set, this defaults to sorting by sequence.asc and then documentKey.asc (optional)
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for items, test plans, test cycles, test runs, or attachments
        api_response = api_instance.get_abstract_items(project=project, item_type=item_type, document_key=document_key, release=release, created_date=created_date, modified_date=modified_date, last_activity_date=last_activity_date, contains=contains, sort_by=sort_by, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling AbstractitemsApi->get_abstract_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **[int]**|  | [optional]
 **item_type** | **[int]**|  | [optional]
 **document_key** | **[str]**|  | [optional]
 **release** | **[int]**|  | [optional]
 **created_date** | **[str]**| Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot; or \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional]
 **modified_date** | **[str]**| Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot; or \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional]
 **last_activity_date** | **[str]**| Filter datetime fields after a single date or within a range of values. Provide one or two values in ISO8601 format (milliseconds or seconds) - \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot; or \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional]
 **contains** | **[str]**| Filter on the text contents of the item. Strings taken literally. Multiple &#39;contains&#39; values will be bitwise ORed. | [optional]
 **sort_by** | **[str]**| Sort orders can be added with the name of the field by which to sort, followed by .asc or .desc (e.g. &#39;name.asc&#39; or &#39;modifiedDate.desc&#39;). If not set, this defaults to sorting by sequence.asc and then documentKey.asc | [optional]
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**ItemDataListWrapper**](ItemDataListWrapper.md)

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

