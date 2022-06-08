# pyjama.ReleasesApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_release**](ReleasesApi.md#add_release) | **POST** /releases | Create a new release
[**get_release**](ReleasesApi.md#get_release) | **GET** /releases/{releaseId} | Get the release with the specified ID
[**get_releases**](ReleasesApi.md#get_releases) | **GET** /releases | Get all releases in the project with the specified ID
[**put_release**](ReleasesApi.md#put_release) | **PUT** /releases/{releaseId} | Update the release with the specified ID


# **add_release**
> CreatedResponse add_release(body)

Create a new release

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import releases_api
from pyjama.model.request_release import RequestRelease
from pyjama.model.created_response import CreatedResponse
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
    api_instance = releases_api.ReleasesApi(api_client)
    body = RequestRelease(
        name="name_example",
        description="description_example",
        release_date="release_date_example",
        project=1,
    ) # RequestRelease | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new release
        api_response = api_instance.add_release(body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling ReleasesApi->add_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestRelease**](RequestRelease.md)|  |

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

# **get_release**
> ReleaseDataWrapper get_release(release_id)

Get the release with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import releases_api
from pyjama.model.release_data_wrapper import ReleaseDataWrapper
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
    api_instance = releases_api.ReleasesApi(api_client)
    release_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the release with the specified ID
        api_response = api_instance.get_release(release_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling ReleasesApi->get_release: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the release with the specified ID
        api_response = api_instance.get_release(release_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling ReleasesApi->get_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**ReleaseDataWrapper**](ReleaseDataWrapper.md)

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

# **get_releases**
> ReleaseDataListWrapper get_releases(project)

Get all releases in the project with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import releases_api
from pyjama.model.release_data_list_wrapper import ReleaseDataListWrapper
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
    api_instance = releases_api.ReleasesApi(api_client)
    project = 1 # int | 
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all releases in the project with the specified ID
        api_response = api_instance.get_releases(project)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling ReleasesApi->get_releases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all releases in the project with the specified ID
        api_response = api_instance.get_releases(project, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling ReleasesApi->get_releases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**|  |
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**ReleaseDataListWrapper**](ReleaseDataListWrapper.md)

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

# **put_release**
> AbstractRestResponse put_release(release_id, body)

Update the release with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import releases_api
from pyjama.model.request_release import RequestRelease
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
    api_instance = releases_api.ReleasesApi(api_client)
    release_id = 1 # int | 
    body = RequestRelease(
        name="name_example",
        description="description_example",
        release_date="release_date_example",
        project=1,
    ) # RequestRelease | 

    # example passing only required values which don't have defaults set
    try:
        # Update the release with the specified ID
        api_response = api_instance.put_release(release_id, body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling ReleasesApi->put_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **int**|  |
 **body** | [**RequestRelease**](RequestRelease.md)|  |

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

