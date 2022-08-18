# openapi_client.GeneralRegistryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch**](GeneralRegistryApi.md#fetch) | **GET** /registry/general/fetch | Fetch Item
[**list**](GeneralRegistryApi.md#list) | **POST** /registry/general/list | List Items


# **fetch**
> UntypedFetchResponse fetch(id)

Fetch Item

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import general_registry_api
from openapi_client.model.untyped_fetch_response import UntypedFetchResponse
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_registry_api.GeneralRegistryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch Item
        api_response = api_instance.fetch(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GeneralRegistryApi->fetch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UntypedFetchResponse**](UntypedFetchResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> UnparsedListResponse list(query_filter)

List Items

list_items Lists all items in the registry based on the provided query filter. The items in this method are not parsed in any way.  Arguments ----------  Returns -------  : UnparsedListResponse  The list of items and a total count, no parsing.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import openapi_client
from openapi_client.api import general_registry_api
from openapi_client.model.unparsed_list_response import UnparsedListResponse
from openapi_client.model.query_filter import QueryFilter
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_registry_api.GeneralRegistryApi(api_client)
    query_filter = QueryFilter(
        item_category=ItemCategory("ACTIVITY"),
        item_subtype=ItemSubType("WORKFLOW_RUN"),
    ) # QueryFilter | 

    # example passing only required values which don't have defaults set
    try:
        # List Items
        api_response = api_instance.list(query_filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GeneralRegistryApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_filter** | [**QueryFilter**](QueryFilter.md)|  |

### Return type

[**UnparsedListResponse**](UnparsedListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

