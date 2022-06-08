# pyjama.UsersApi

All URIs are relative to *http://<jama_endpoint>/rest/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /users | Create a new user
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /users/current | Gets the current user
[**get_current_user_favorite_filters**](UsersApi.md#get_current_user_favorite_filters) | **GET** /users/current/favoritefilters | Gets the current user&#39;s favorite filters
[**get_user**](UsersApi.md#get_user) | **GET** /users/{userId} | Get the user with the specified ID
[**get_users**](UsersApi.md#get_users) | **GET** /users | Get all users
[**put_user**](UsersApi.md#put_user) | **PUT** /users/{userId} | Update the user with the specified ID
[**set_active_status**](UsersApi.md#set_active_status) | **PUT** /users/{userId}/active | Update the active status for the user with the specified ID


# **add_user**
> CreatedResponse add_user(body)

Create a new user

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import users_api
from pyjama.model.request_user import RequestUser
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
    api_instance = users_api.UsersApi(api_client)
    body = RequestUser(
        username="username_example",
        password="password_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone="phone_example",
        title="title_example",
        location="location_example",
        license_type="NAMED",
    ) # RequestUser | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new user
        api_response = api_instance.add_user(body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->add_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestUser**](RequestUser.md)|  |

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

# **get_current_user**
> UserDataWrapper get_current_user()

Gets the current user

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import users_api
from pyjama.model.user_data_wrapper import UserDataWrapper
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
    api_instance = users_api.UsersApi(api_client)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the current user
        api_response = api_instance.get_current_user(include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**UserDataWrapper**](UserDataWrapper.md)

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

# **get_current_user_favorite_filters**
> FilterDataListWrapper get_current_user_favorite_filters()

Gets the current user's favorite filters

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import users_api
from pyjama.model.filter_data_list_wrapper import FilterDataListWrapper
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
    api_instance = users_api.UsersApi(api_client)
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the current user's favorite filters
        api_response = api_instance.get_current_user_favorite_filters(start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->get_current_user_favorite_filters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**FilterDataListWrapper**](FilterDataListWrapper.md)

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

# **get_user**
> UserDataWrapper get_user(user_id)

Get the user with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import users_api
from pyjama.model.user_data_wrapper import UserDataWrapper
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | 
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the user with the specified ID
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the user with the specified ID
        api_response = api_instance.get_user(user_id, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**UserDataWrapper**](UserDataWrapper.md)

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

# **get_users**
> UserDataListWrapper get_users()

Get all users

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import users_api
from pyjama.model.user_data_list_wrapper import UserDataListWrapper
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
    api_instance = users_api.UsersApi(api_client)
    username = "username_example" # str |  (optional)
    email = "email_example" # str |  (optional)
    first_name = "firstName_example" # str |  (optional)
    last_name = "lastName_example" # str |  (optional)
    license_type = "NAMED" # str |  (optional)
    include_inactive = True # bool |  (optional)
    start_at = 1 # int |  (optional)
    max_results = 1 # int | If not set, this defaults to 20. This cannot be larger than 50 (optional)
    include = [
        "include_example",
    ] # [str] | Links to include as full objects in the linked map (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all users
        api_response = api_instance.get_users(username=username, email=email, first_name=first_name, last_name=last_name, license_type=license_type, include_inactive=include_inactive, start_at=start_at, max_results=max_results, include=include)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional]
 **email** | **str**|  | [optional]
 **first_name** | **str**|  | [optional]
 **last_name** | **str**|  | [optional]
 **license_type** | **str**|  | [optional]
 **include_inactive** | **bool**|  | [optional]
 **start_at** | **int**|  | [optional]
 **max_results** | **int**| If not set, this defaults to 20. This cannot be larger than 50 | [optional]
 **include** | **[str]**| Links to include as full objects in the linked map | [optional]

### Return type

[**UserDataListWrapper**](UserDataListWrapper.md)

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

# **put_user**
> AbstractRestResponse put_user(user_id, body)

Update the user with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import users_api
from pyjama.model.request_user import RequestUser
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | 
    body = RequestUser(
        username="username_example",
        password="password_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone="phone_example",
        title="title_example",
        location="location_example",
        license_type="NAMED",
    ) # RequestUser | 

    # example passing only required values which don't have defaults set
    try:
        # Update the user with the specified ID
        api_response = api_instance.put_user(user_id, body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->put_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |
 **body** | [**RequestUser**](RequestUser.md)|  |

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

# **set_active_status**
> AbstractRestResponse set_active_status(user_id, body)

Update the active status for the user with the specified ID

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth2):

```python
import time
import pyjama
from pyjama.api import users_api
from pyjama.model.request_active_status import RequestActiveStatus
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | 
    body = RequestActiveStatus(
        active=True,
    ) # RequestActiveStatus | 

    # example passing only required values which don't have defaults set
    try:
        # Update the active status for the user with the specified ID
        api_response = api_instance.set_active_status(user_id, body)
        pprint(api_response)
    except pyjama.ApiException as e:
        print("Exception when calling UsersApi->set_active_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  |
 **body** | [**RequestActiveStatus**](RequestActiveStatus.md)|  |

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

