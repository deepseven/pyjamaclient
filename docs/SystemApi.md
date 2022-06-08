# pyjama.SystemApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_domains**](SystemApi.md#get_domains) | **GET** /system/settings/corsdomains | Get the current CORS domain whitelist
[**set_domains**](SystemApi.md#set_domains) | **POST** /system/settings/corsdomains | Update CORS domain whitelist


# **get_domains**
> CrossOriginDomainWhiteList get_domains()

Get the current CORS domain whitelist

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import system_api
from pyjama.model.cross_origin_domain_white_list import CrossOriginDomainWhiteList
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
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current CORS domain whitelist
        api_response = api_instance.get_domains()
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling SystemApi->get_domains: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CrossOriginDomainWhiteList**](CrossOriginDomainWhiteList.md)

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

# **set_domains**
> AbstractRestResponse set_domains(body)

Update CORS domain whitelist

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import system_api
from pyjama.model.cross_origin_domain_white_list import CrossOriginDomainWhiteList
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
    api_instance = system_api.SystemApi(api_client)
    body = CrossOriginDomainWhiteList(
        domains=[
            "domains_example",
        ],
    ) # CrossOriginDomainWhiteList | 

    # example passing only required values which don't have defaults set
    try:
        # Update CORS domain whitelist
        api_response = api_instance.set_domains(body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling SystemApi->set_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrossOriginDomainWhiteList**](CrossOriginDomainWhiteList.md)|  |

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

