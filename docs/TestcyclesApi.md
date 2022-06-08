# pyjama.TestcyclesApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_test_cycle**](TestcyclesApi.md#delete_test_cycle) | **DELETE** /testcycles/{testCycleId} | Delete the test cycle with the specified ID, including the test runs in the test cycle
[**get_test_cycle**](TestcyclesApi.md#get_test_cycle) | **GET** /testcycles/{testCycleId} | Get the test cycle with the specified ID
[**get_test_cycle_test_group**](TestcyclesApi.md#get_test_cycle_test_group) | **GET** /testcycles/{testCycleId}/testgroup/{testGroupId} | Get the test cycle test group for the test cycle with the specified ID
[**get_test_cycle_test_runs**](TestcyclesApi.md#get_test_cycle_test_runs) | **GET** /testcycles/{testCycleId}/testruns | Get all test runs for the test cycle with the specified ID
[**get_test_cycle_version**](TestcyclesApi.md#get_test_cycle_version) | **GET** /testcycles/{testCycleId}/versions/{versionNum}/versioneditem | Get the  snapshot of the test cycle at the specified version
[**get_test_cycle_versioned**](TestcyclesApi.md#get_test_cycle_versioned) | **GET** /testcycles/{testCycleId}/versions/{versionNum} | Get the numbered version for the item with the specified ID
[**get_test_cycle_versions**](TestcyclesApi.md#get_test_cycle_versions) | **GET** /testcycles/{testCycleId}/versions | Get all versions for the item with the specified ID
[**patch_test_cycle**](TestcyclesApi.md#patch_test_cycle) | **PATCH** /testcycles/{testCycleId} | Update the test cycle with the specified ID, including regenerating the test runs in the test cycle
[**update_test_cycle**](TestcyclesApi.md#update_test_cycle) | **PUT** /testcycles/{testCycleId} | Update the test cycle with the specified ID, including regenerating the test runs in the test cycle


# **delete_test_cycle**
> AbstractRestResponse delete_test_cycle(test_cycle_id)

Delete the test cycle with the specified ID, including the test runs in the test cycle

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    test_cycle_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the test cycle with the specified ID, including the test runs in the test cycle
        api_response = api_instance.delete_test_cycle(test_cycle_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->delete_test_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_cycle_id** | **int**|  |

### Return type

[**AbstractRestResponse**](AbstractRestResponse.md)

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

# **get_test_cycle**
> TestCycleDataWrapper get_test_cycle(test_cycle_id)

Get the test cycle with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
from pyjama.model.test_cycle_data_wrapper import TestCycleDataWrapper
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    test_cycle_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the test cycle with the specified ID
        api_response = api_instance.get_test_cycle(test_cycle_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the test cycle with the specified ID
        api_response = api_instance.get_test_cycle(test_cycle_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_cycle_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**TestCycleDataWrapper**](TestCycleDataWrapper.md)

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

# **get_test_cycle_test_group**
> TestCycleTestGroupDataWrapper get_test_cycle_test_group(test_group_id, test_cycle_id)

Get the test cycle test group for the test cycle with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
from pyjama.model.test_cycle_test_group_data_wrapper import TestCycleTestGroupDataWrapper
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    test_group_id = 1 # int | Get the test group with the specified ID
    test_cycle_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the test cycle test group for the test cycle with the specified ID
        api_response = api_instance.get_test_cycle_test_group(test_group_id, test_cycle_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_test_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the test cycle test group for the test cycle with the specified ID
        api_response = api_instance.get_test_cycle_test_group(test_group_id, test_cycle_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_test_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_group_id** | **int**| Get the test group with the specified ID |
 **test_cycle_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**TestCycleTestGroupDataWrapper**](TestCycleTestGroupDataWrapper.md)

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

# **get_test_cycle_test_runs**
> TestRunDataListWrapper get_test_cycle_test_runs(test_cycle_id)

Get all test runs for the test cycle with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
from pyjama.model.test_run_data_list_wrapper import TestRunDataListWrapper
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    test_cycle_id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all test runs for the test cycle with the specified ID
        api_response = api_instance.get_test_cycle_test_runs(test_cycle_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_test_runs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all test runs for the test cycle with the specified ID
        api_response = api_instance.get_test_cycle_test_runs(test_cycle_id, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_test_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_cycle_id** | **int**|  |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**TestRunDataListWrapper**](TestRunDataListWrapper.md)

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

# **get_test_cycle_version**
> VersionedTestCycleDataWrapper get_test_cycle_version(version_num, test_cycle_id)

Get the  snapshot of the test cycle at the specified version

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
from pyjama.model.versioned_test_cycle_data_wrapper import VersionedTestCycleDataWrapper
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    version_num = 1 # int | 
    test_cycle_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the  snapshot of the test cycle at the specified version
        api_response = api_instance.get_test_cycle_version(version_num, test_cycle_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the  snapshot of the test cycle at the specified version
        api_response = api_instance.get_test_cycle_version(version_num, test_cycle_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **int**|  |
 **test_cycle_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**VersionedTestCycleDataWrapper**](VersionedTestCycleDataWrapper.md)

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

# **get_test_cycle_versioned**
> VersionDataWrapper get_test_cycle_versioned(version_num, test_cycle_id)

Get the numbered version for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    version_num = 1 # int | 
    test_cycle_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the numbered version for the item with the specified ID
        api_response = api_instance.get_test_cycle_versioned(version_num, test_cycle_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_versioned: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the numbered version for the item with the specified ID
        api_response = api_instance.get_test_cycle_versioned(version_num, test_cycle_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_versioned: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **int**|  |
 **test_cycle_id** | **int**|  |
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

# **get_test_cycle_versions**
> VersionDataListWrapper get_test_cycle_versions(test_cycle_id)

Get all versions for the item with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    test_cycle_id = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all versions for the item with the specified ID
        api_response = api_instance.get_test_cycle_versions(test_cycle_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all versions for the item with the specified ID
        api_response = api_instance.get_test_cycle_versions(test_cycle_id, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->get_test_cycle_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_cycle_id** | **int**|  |
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

# **patch_test_cycle**
> AbstractRestResponse patch_test_cycle(test_cycle_id, body)

Update the test cycle with the specified ID, including regenerating the test runs in the test cycle

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
from pyjama.model.request_patch_operation import RequestPatchOperation
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    test_cycle_id = 1 # int | 
    body = [
        RequestPatchOperation(
            op="remove",
            path="path_example",
            value={},
        ),
    ] # [RequestPatchOperation] | 

    # example passing only required values which don't have defaults set
    try:
        # Update the test cycle with the specified ID, including regenerating the test runs in the test cycle
        api_response = api_instance.patch_test_cycle(test_cycle_id, body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->patch_test_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_cycle_id** | **int**|  |
 **body** | [**[RequestPatchOperation]**](RequestPatchOperation.md)|  |

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

# **update_test_cycle**
> AbstractRestResponse update_test_cycle(test_cycle_id, body)

Update the test cycle with the specified ID, including regenerating the test runs in the test cycle

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import testcycles_api
from pyjama.model.request_test_cycle import RequestTestCycle
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
    api_instance = testcycles_api.TestcyclesApi(api_client)
    test_cycle_id = 1 # int | 
    body = RequestTestCycle(
        fields={
            "key": {},
        },
        test_run_generation_config=TestRunGenerationConfig(
            test_groups_to_include=[
                1,
            ],
            test_run_statuses_to_include=[
                "PASSED",
            ],
        ),
    ) # RequestTestCycle | 

    # example passing only required values which don't have defaults set
    try:
        # Update the test cycle with the specified ID, including regenerating the test runs in the test cycle
        api_response = api_instance.update_test_cycle(test_cycle_id, body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling TestcyclesApi->update_test_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_cycle_id** | **int**|  |
 **body** | [**RequestTestCycle**](RequestTestCycle.md)|  |

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

