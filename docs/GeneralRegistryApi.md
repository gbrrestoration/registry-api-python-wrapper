# rrap_mds_is_registry_api.GeneralRegistryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_item_registry_general_fetch_get**](GeneralRegistryApi.md#fetch_item_registry_general_fetch_get) | **GET** /registry/general/fetch | Fetch Item
[**list_items_registry_general_list_post**](GeneralRegistryApi.md#list_items_registry_general_list_post) | **POST** /registry/general/list | List Items


# **fetch_item_registry_general_fetch_get**
> UntypedFetchResponse fetch_item_registry_general_fetch_get(id)

Fetch Item

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import general_registry_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.untyped_fetch_response import UntypedFetchResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_registry_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_registry_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_registry_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_registry_api.GeneralRegistryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch Item
        api_response = api_instance.fetch_item_registry_general_fetch_get(id)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling GeneralRegistryApi->fetch_item_registry_general_fetch_get: %s\n" % e)
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

# **list_items_registry_general_list_post**
> UnparsedListResponse list_items_registry_general_list_post(query_filter)

List Items

list_items Lists all items in the registry based on the provided query filter. The items in this method are not parsed in any way.  Arguments ----------  Returns -------  : UnparsedListResponse  The list of items and a total count, no parsing.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import general_registry_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.query_filter import QueryFilter
from rrap_mds_is_registry_api.model.unparsed_list_response import UnparsedListResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rrap_mds_is_registry_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = rrap_mds_is_registry_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rrap_mds_is_registry_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_registry_api.GeneralRegistryApi(api_client)
    query_filter = QueryFilter(
        item_category=ItemCategory("ACTIVITY"),
        item_subtype=ItemSubType("WORKFLOW_RUN"),
    ) # QueryFilter | 

    # example passing only required values which don't have defaults set
    try:
        # List Items
        api_response = api_instance.list_items_registry_general_list_post(query_filter)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling GeneralRegistryApi->list_items_registry_general_list_post: %s\n" % e)
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

