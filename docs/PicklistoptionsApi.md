# pyjama.PicklistoptionsApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_picklist_option_id**](PicklistoptionsApi.md#get_picklist_option_id) | **GET** /picklistoptions/{picklistOptionId} | Get the pick list option with the specified ID
[**update_picklist_option**](PicklistoptionsApi.md#update_picklist_option) | **PUT** /picklistoptions/{picklistOptionId} | Update the pick list option with the specified ID


# **get_picklist_option_id**
> PickListOptionDataWrapper get_picklist_option_id(picklist_option_id)

Get the pick list option with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import picklistoptions_api
from pyjama.model.pick_list_option_data_wrapper import PickListOptionDataWrapper
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
    api_instance = picklistoptions_api.PicklistoptionsApi(api_client)
    picklist_option_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the pick list option with the specified ID
        api_response = api_instance.get_picklist_option_id(picklist_option_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling PicklistoptionsApi->get_picklist_option_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the pick list option with the specified ID
        api_response = api_instance.get_picklist_option_id(picklist_option_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling PicklistoptionsApi->get_picklist_option_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **picklist_option_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**PickListOptionDataWrapper**](PickListOptionDataWrapper.md)

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

# **update_picklist_option**
> AbstractRestResponse update_picklist_option(picklist_option_id, body)

Update the pick list option with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import picklistoptions_api
from pyjama.model.request_pick_list_option import RequestPickListOption
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
    api_instance = picklistoptions_api.PicklistoptionsApi(api_client)
    picklist_option_id = 1 # int | 
    body = RequestPickListOption(
        description="description_example",
        name="name_example",
        value="value_example",
        color="000000",
        sort_order=1,
        default=True,
    ) # RequestPickListOption | 

    # example passing only required values which don't have defaults set
    try:
        # Update the pick list option with the specified ID
        api_response = api_instance.update_picklist_option(picklist_option_id, body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling PicklistoptionsApi->update_picklist_option: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **picklist_option_id** | **int**|  |
 **body** | [**RequestPickListOption**](RequestPickListOption.md)|  |

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

