# pyjama.BaselinesApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_baseline**](BaselinesApi.md#get_baseline) | **GET** /baselines/{baselineId} | Get the baseline with the specified ID
[**get_baseline_versioned_item**](BaselinesApi.md#get_baseline_versioned_item) | **GET** /baselines/{baselineId}/versioneditems/{itemId} | Get the baseline item with the specified ID in a baseline with the specified ID
[**get_baseline_versioned_items**](BaselinesApi.md#get_baseline_versioned_items) | **GET** /baselines/{baselineId}/versioneditems | Get all baseline items in a baseline with the specified ID
[**get_baseline_versioned_relationships**](BaselinesApi.md#get_baseline_versioned_relationships) | **GET** /baselines/{baselineId}/versioneditems/{itemId}/versionedrelationships | Get all versioned relationships for the item in the baseline
[**get_baselines**](BaselinesApi.md#get_baselines) | **GET** /baselines | Get all baselines in the project with the specified ID


# **get_baseline**
> BaselineDataWrapper get_baseline(baseline_id)

Get the baseline with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import baselines_api
from pyjama.model.baseline_data_wrapper import BaselineDataWrapper
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
    api_instance = baselines_api.BaselinesApi(api_client)
    baseline_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the baseline with the specified ID
        api_response = api_instance.get_baseline(baseline_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the baseline with the specified ID
        api_response = api_instance.get_baseline(baseline_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baseline_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**BaselineDataWrapper**](BaselineDataWrapper.md)

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

# **get_baseline_versioned_item**
> BaselineItemDataWrapper get_baseline_versioned_item(item_id, baseline_id)

Get the baseline item with the specified ID in a baseline with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import baselines_api
from pyjama.model.baseline_item_data_wrapper import BaselineItemDataWrapper
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
    api_instance = baselines_api.BaselinesApi(api_client)
    item_id = 1 # int | 
    baseline_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the baseline item with the specified ID in a baseline with the specified ID
        api_response = api_instance.get_baseline_versioned_item(item_id, baseline_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline_versioned_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the baseline item with the specified ID in a baseline with the specified ID
        api_response = api_instance.get_baseline_versioned_item(item_id, baseline_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline_versioned_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  |
 **baseline_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**BaselineItemDataWrapper**](BaselineItemDataWrapper.md)

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

# **get_baseline_versioned_items**
> BaselineItemDataListWrapper get_baseline_versioned_items(baseline_id)

Get all baseline items in a baseline with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import baselines_api
from pyjama.model.baseline_item_data_list_wrapper import BaselineItemDataListWrapper
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
    api_instance = baselines_api.BaselinesApi(api_client)
    baseline_id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all baseline items in a baseline with the specified ID
        api_response = api_instance.get_baseline_versioned_items(baseline_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline_versioned_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all baseline items in a baseline with the specified ID
        api_response = api_instance.get_baseline_versioned_items(baseline_id, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline_versioned_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baseline_id** | **int**|  |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**BaselineItemDataListWrapper**](BaselineItemDataListWrapper.md)

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

# **get_baseline_versioned_relationships**
> VersionedRelationshipDataListWrapper get_baseline_versioned_relationships(item_id, baseline_id)

Get all versioned relationships for the item in the baseline

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import baselines_api
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
    api_instance = baselines_api.BaselinesApi(api_client)
    item_id = 1 # int | 
    baseline_id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all versioned relationships for the item in the baseline
        api_response = api_instance.get_baseline_versioned_relationships(item_id, baseline_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline_versioned_relationships: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all versioned relationships for the item in the baseline
        api_response = api_instance.get_baseline_versioned_relationships(item_id, baseline_id, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baseline_versioned_relationships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  |
 **baseline_id** | **int**|  |
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

# **get_baselines**
> BaselineDataListWrapper get_baselines(project)

Get all baselines in the project with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import baselines_api
from pyjama.model.baseline_data_list_wrapper import BaselineDataListWrapper
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
    api_instance = baselines_api.BaselinesApi(api_client)
    project = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all baselines in the project with the specified ID
        api_response = api_instance.get_baselines(project)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baselines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all baselines in the project with the specified ID
        api_response = api_instance.get_baselines(project, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling BaselinesApi->get_baselines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**|  |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**BaselineDataListWrapper**](BaselineDataListWrapper.md)

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

