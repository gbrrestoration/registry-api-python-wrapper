# rrap_mds_is_registry_api.ModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_registry_entity_model_create_post**](ModelApi.md#create_item_registry_entity_model_create_post) | **POST** /registry/entity/model/create | Create Item
[**delete_item_registry_entity_model_delete_delete**](ModelApi.md#delete_item_registry_entity_model_delete_delete) | **DELETE** /registry/entity/model/delete | Delete Item
[**fetch_item_registry_entity_model_fetch_get**](ModelApi.md#fetch_item_registry_entity_model_fetch_get) | **GET** /registry/entity/model/fetch | Fetch Item
[**get_schema_registry_entity_model_schema_get**](ModelApi.md#get_schema_registry_entity_model_schema_get) | **GET** /registry/entity/model/schema | Get Schema
[**get_ui_schema_registry_entity_model_ui_schema_get**](ModelApi.md#get_ui_schema_registry_entity_model_ui_schema_get) | **GET** /registry/entity/model/ui_schema | Get Ui Schema
[**list_items_registry_entity_model_list_get**](ModelApi.md#list_items_registry_entity_model_list_get) | **GET** /registry/entity/model/list | List Items
[**seed_item_registry_entity_model_seed_post**](ModelApi.md#seed_item_registry_entity_model_seed_post) | **POST** /registry/entity/model/seed | Seed Item
[**update_item_registry_entity_model_update_put**](ModelApi.md#update_item_registry_entity_model_update_put) | **PUT** /registry/entity/model/update | Update Item
[**validate_registry_entity_model_validate_post**](ModelApi.md#validate_registry_entity_model_validate_post) | **POST** /registry/entity/model/validate | Validate


# **create_item_registry_entity_model_create_post**
> ModelCreateResponse create_item_registry_entity_model_create_post(model_domain_info)

Create Item

create_item POSTs a new item to the registry of the given item type.  The item does not need to include an id or creation time  as these will be automatically generated during creation.  Responds with the successfully created item.  If you want to seed an identity without providing full information, you can use the seed endpoint and then use the update endpoint later.  Arguments ---------- item : item_model_type     The item you want to create.  Returns -------  : GenericCreateResponse     The create response which will include a status and the item      created (if it was successful).  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.model_domain_info import ModelDomainInfo
from rrap_mds_is_registry_api.model.model_create_response import ModelCreateResponse
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
    api_instance = model_api.ModelApi(api_client)
    model_domain_info = ModelDomainInfo(
        display_name="display_name_example",
        name="name_example",
        description="description_example",
        documentation_url="documentation_url_example",
        source_url="source_url_example",
    ) # ModelDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Create Item
        api_response = api_instance.create_item_registry_entity_model_create_post(model_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->create_item_registry_entity_model_create_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_domain_info** | [**ModelDomainInfo**](ModelDomainInfo.md)|  |

### Return type

[**ModelCreateResponse**](ModelCreateResponse.md)

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

# **delete_item_registry_entity_model_delete_delete**
> StatusResponse delete_item_registry_entity_model_delete_delete(id)

Delete Item

delete_item Admin only endpoint which can be used to delete  objects from the registry. Delete is by ID. This endpoint will return successfully even if the object doesn't exist in the first place.  Arguments ---------- id : str     The handle ID of the object to delete  Returns -------  : StatusResponse     Was the deletion successful - returns true even if the item      did not exist.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.status_response import StatusResponse
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
    api_instance = model_api.ModelApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Item
        api_response = api_instance.delete_item_registry_entity_model_delete_delete(id)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->delete_item_registry_entity_model_delete_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**StatusResponse**](StatusResponse.md)

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

# **fetch_item_registry_entity_model_fetch_get**
> ModelFetchResponse fetch_item_registry_entity_model_fetch_get(id)

Fetch Item

fetch_item Fetches the item specified by the id from the  registry. Only returns items which fit the specified item type in this route, or if you allow with the  seed_allowed flag, will return seed items of  matching category and subtype.  Arguments ---------- id : str     The handle id of the item to fetch. seed_allowed : bool, optional     Do you want to allow seed items to be returned, by default False  Returns -------  : GenericFetchResponse     Returns a status and possibly the item.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.model_fetch_response import ModelFetchResponse
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
    api_instance = model_api.ModelApi(api_client)
    id = "id_example" # str | 
    seed_allowed = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Fetch Item
        api_response = api_instance.fetch_item_registry_entity_model_fetch_get(id)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->fetch_item_registry_entity_model_fetch_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch Item
        api_response = api_instance.fetch_item_registry_entity_model_fetch_get(id, seed_allowed=seed_allowed)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->fetch_item_registry_entity_model_fetch_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **seed_allowed** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**ModelFetchResponse**](ModelFetchResponse.md)

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

# **get_schema_registry_entity_model_schema_get**
> SchemaResponse get_schema_registry_entity_model_schema_get()

Get Schema

get_schema Returns the auto generated pydantic model  json schema. This can be used to programmatically generate input forms, or to validate against the  pydantic model. You can also use the /validate  endpoint.  Arguments ----------  Returns -------  : SchemaResponse     Response with a json schema object.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.schema_response import SchemaResponse
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
    api_instance = model_api.ModelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Schema
        api_response = api_instance.get_schema_registry_entity_model_schema_get()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->get_schema_registry_entity_model_schema_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SchemaResponse**](SchemaResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ui_schema_registry_entity_model_ui_schema_get**
> UiSchemaResponse get_ui_schema_registry_entity_model_ui_schema_get()

Get Ui Schema

Returns the ui schema override provided for this model.  This is for use by the front end - enabling overriding of specific model fields with specific components.   Parameters ---------- protected_roles : ProtectedRole, optional     _description_, by default Depends( read_user_protected_role_dependency)  Returns ------- UiSchemaResponse     A JSON style mapping of field names (possibly nested) to component overrides.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.ui_schema_response import UiSchemaResponse
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
    api_instance = model_api.ModelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Ui Schema
        api_response = api_instance.get_ui_schema_registry_entity_model_ui_schema_get()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->get_ui_schema_registry_entity_model_ui_schema_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UiSchemaResponse**](UiSchemaResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items_registry_entity_model_list_get**
> ModelListResponse list_items_registry_entity_model_list_get()

List Items

list_items Lists all items of the specified type (by route). Sorts items  into parsable complete entities (i.e. normal entities), parsable  seed items (i.e. incomplete), and completely unparsable entities.   If there are any unparsable entities, the success field of the return  status will be False, however the items will still be provided.   Arguments ----------  Returns -------  : GenericListResponse     The list of items, sorted complete, seed and unparsable, as well      as counts for each type.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.model_list_response import ModelListResponse
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
    api_instance = model_api.ModelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Items
        api_response = api_instance.list_items_registry_entity_model_list_get()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->list_items_registry_entity_model_list_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelListResponse**](ModelListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seed_item_registry_entity_model_seed_post**
> ModelSeedResponse seed_item_registry_entity_model_seed_post()

Seed Item

seed_item Posts a new empty item. This will mint a handle,  set the creation time, and produce the correct  category and sub type. This can then be updated  later using the update endpoint.  Arguments ----------  Returns -------  : GenericSeedResponse     The seed item that was created.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.model_seed_response import ModelSeedResponse
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
    api_instance = model_api.ModelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Seed Item
        api_response = api_instance.seed_item_registry_entity_model_seed_post()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->seed_item_registry_entity_model_seed_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelSeedResponse**](ModelSeedResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_registry_entity_model_update_put**
> StatusResponse update_item_registry_entity_model_update_put(id, model_domain_info)

Update Item

update_item PUT method to apply an update to an existing item. The  existing item can either be a complete object/item or a seed item of matching category and subtype.  To replace an item, you provide the id of the item as a query string alongside the domain information object that you want to update on that item.   Arguments ---------- id : str     The id of the object in the registry. (Handle) replacement_domain_info : item_domain_info_type     The new domain specific information for that record.  Returns -------  : StatusResponse     Was the update successful?  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.status_response import StatusResponse
from rrap_mds_is_registry_api.model.model_domain_info import ModelDomainInfo
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
    api_instance = model_api.ModelApi(api_client)
    id = "id_example" # str | 
    model_domain_info = ModelDomainInfo(
        display_name="display_name_example",
        name="name_example",
        description="description_example",
        documentation_url="documentation_url_example",
        source_url="source_url_example",
    ) # ModelDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Update Item
        api_response = api_instance.update_item_registry_entity_model_update_put(id, model_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->update_item_registry_entity_model_update_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **model_domain_info** | [**ModelDomainInfo**](ModelDomainInfo.md)|  |

### Return type

[**StatusResponse**](StatusResponse.md)

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

# **validate_registry_entity_model_validate_post**
> StatusResponse validate_registry_entity_model_validate_post(model_domain_info)

Validate

validate Validates the given item body input. If this method responds with a success, then a create_item call  with this input should succeed. Validates in two stages 1) ensures that the pydantic model can parse your input - if this fails, you will receive a 422 error 2) ensures that the provided item category and subtype are correct.  Arguments ---------- item : item_model_type     The item which you want to validate  Returns -------  : StatusResponse     Success or failure object.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.status_response import StatusResponse
from rrap_mds_is_registry_api.model.model_domain_info import ModelDomainInfo
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
    api_instance = model_api.ModelApi(api_client)
    model_domain_info = ModelDomainInfo(
        display_name="display_name_example",
        name="name_example",
        description="description_example",
        documentation_url="documentation_url_example",
        source_url="source_url_example",
    ) # ModelDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Validate
        api_response = api_instance.validate_registry_entity_model_validate_post(model_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelApi->validate_registry_entity_model_validate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_domain_info** | [**ModelDomainInfo**](ModelDomainInfo.md)|  |

### Return type

[**StatusResponse**](StatusResponse.md)

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

