# rrap_mds_is_registry_api.ModelRunWorkflowDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#create_entity_model_run_workflow_definition) | **POST** /registry/entity/model_run_workflow/create | Create Item
[**delete_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#delete_entity_model_run_workflow_definition) | **DELETE** /registry/entity/model_run_workflow/delete | Delete Item
[**fetch_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#fetch_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/fetch | Fetch Item
[**list_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#list_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/list | List Items
[**schema_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#schema_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/schema | Get Schema
[**seed_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#seed_entity_model_run_workflow_definition) | **POST** /registry/entity/model_run_workflow/seed | Seed Item
[**ui_schema_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#ui_schema_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/ui_schema | Get Ui Schema
[**update_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#update_entity_model_run_workflow_definition) | **PUT** /registry/entity/model_run_workflow/update | Update Item
[**validate_entity_model_run_workflow_definition**](ModelRunWorkflowDefinitionApi.md#validate_entity_model_run_workflow_definition) | **POST** /registry/entity/model_run_workflow/validate | Validate


# **create_entity_model_run_workflow_definition**
> ModelRunWorkflowDefinitionCreateResponse create_entity_model_run_workflow_definition(model_run_workflow_definition_domain_info)

Create Item

create_item POSTs a new item to the registry of the given item type.  The item does not need to include an id or creation time  as these will be automatically generated during creation.  Responds with the successfully created item.  If you want to seed an identity without providing full information, you can use the seed endpoint and then use the update endpoint later.  Arguments ---------- item : item_model_type     The item you want to create.  Returns -------  : GenericCreateResponse     The create response which will include a status and the item      created (if it was successful).  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
from rrap_mds_is_registry_api.model.model_run_workflow_definition_create_response import ModelRunWorkflowDefinitionCreateResponse
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.model_run_workflow_definition_domain_info import ModelRunWorkflowDefinitionDomainInfo
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)
    model_run_workflow_definition_domain_info = ModelRunWorkflowDefinitionDomainInfo(
        display_name="display_name_example",
        version="version_example",
        software="software_example",
        automation_schedule={},
        input_templates=[
            "input_templates_example",
        ],
        output_templates=[
            "output_templates_example",
        ],
    ) # ModelRunWorkflowDefinitionDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Create Item
        api_response = api_instance.create_entity_model_run_workflow_definition(model_run_workflow_definition_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->create_entity_model_run_workflow_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_run_workflow_definition_domain_info** | [**ModelRunWorkflowDefinitionDomainInfo**](ModelRunWorkflowDefinitionDomainInfo.md)|  |

### Return type

[**ModelRunWorkflowDefinitionCreateResponse**](ModelRunWorkflowDefinitionCreateResponse.md)

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

# **delete_entity_model_run_workflow_definition**
> StatusResponse delete_entity_model_run_workflow_definition(id)

Delete Item

delete_item Admin only endpoint which can be used to delete  objects from the registry. Delete is by ID. This endpoint will return successfully even if the object doesn't exist in the first place.  Arguments ---------- id : str     The handle ID of the object to delete  Returns -------  : StatusResponse     Was the deletion successful - returns true even if the item      did not exist.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Item
        api_response = api_instance.delete_entity_model_run_workflow_definition(id)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->delete_entity_model_run_workflow_definition: %s\n" % e)
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

# **fetch_entity_model_run_workflow_definition**
> ModelRunWorkflowDefinitionFetchResponse fetch_entity_model_run_workflow_definition(id)

Fetch Item

fetch_item Fetches the item specified by the id from the  registry. Only returns items which fit the specified item type in this route, or if you allow with the  seed_allowed flag, will return seed items of  matching category and subtype.  Arguments ---------- id : str     The handle id of the item to fetch. seed_allowed : bool, optional     Do you want to allow seed items to be returned, by default False  Returns -------  : GenericFetchResponse     Returns a status and possibly the item.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.model_run_workflow_definition_fetch_response import ModelRunWorkflowDefinitionFetchResponse
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)
    id = "id_example" # str | 
    seed_allowed = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Fetch Item
        api_response = api_instance.fetch_entity_model_run_workflow_definition(id)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->fetch_entity_model_run_workflow_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch Item
        api_response = api_instance.fetch_entity_model_run_workflow_definition(id, seed_allowed=seed_allowed)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->fetch_entity_model_run_workflow_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **seed_allowed** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**ModelRunWorkflowDefinitionFetchResponse**](ModelRunWorkflowDefinitionFetchResponse.md)

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

# **list_entity_model_run_workflow_definition**
> ModelRunWorkflowDefinitionListResponse list_entity_model_run_workflow_definition()

List Items

list_items Lists all items of the specified type (by route). Sorts items  into parsable complete entities (i.e. normal entities), parsable  seed items (i.e. incomplete), and completely unparsable entities.   If there are any unparsable entities, the success field of the return  status will be False, however the items will still be provided.   Arguments ----------  Returns -------  : GenericListResponse     The list of items, sorted complete, seed and unparsable, as well      as counts for each type.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
from rrap_mds_is_registry_api.model.model_run_workflow_definition_list_response import ModelRunWorkflowDefinitionListResponse
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Items
        api_response = api_instance.list_entity_model_run_workflow_definition()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->list_entity_model_run_workflow_definition: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelRunWorkflowDefinitionListResponse**](ModelRunWorkflowDefinitionListResponse.md)

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

# **schema_entity_model_run_workflow_definition**
> SchemaResponse schema_entity_model_run_workflow_definition()

Get Schema

get_schema Returns the auto generated pydantic model  json schema. This can be used to programmatically generate input forms, or to validate against the  pydantic model. You can also use the /validate  endpoint.  Arguments ----------  Returns -------  : SchemaResponse     Response with a json schema object.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Schema
        api_response = api_instance.schema_entity_model_run_workflow_definition()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->schema_entity_model_run_workflow_definition: %s\n" % e)
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

# **seed_entity_model_run_workflow_definition**
> ModelRunWorkflowDefinitionSeedResponse seed_entity_model_run_workflow_definition()

Seed Item

seed_item Posts a new empty item. This will mint a handle,  set the creation time, and produce the correct  category and sub type. This can then be updated  later using the update endpoint.  Arguments ----------  Returns -------  : GenericSeedResponse     The seed item that was created.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
from rrap_mds_is_registry_api.model.model_run_workflow_definition_seed_response import ModelRunWorkflowDefinitionSeedResponse
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Seed Item
        api_response = api_instance.seed_entity_model_run_workflow_definition()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->seed_entity_model_run_workflow_definition: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelRunWorkflowDefinitionSeedResponse**](ModelRunWorkflowDefinitionSeedResponse.md)

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

# **ui_schema_entity_model_run_workflow_definition**
> UiSchemaResponse ui_schema_entity_model_run_workflow_definition()

Get Ui Schema

Returns the ui schema override provided for this model.  This is for use by the front end - enabling overriding of specific model fields with specific components.   Parameters ---------- protected_roles : ProtectedRole, optional     _description_, by default Depends( read_user_protected_role_dependency)  Returns ------- UiSchemaResponse     A JSON style mapping of field names (possibly nested) to component overrides.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Ui Schema
        api_response = api_instance.ui_schema_entity_model_run_workflow_definition()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->ui_schema_entity_model_run_workflow_definition: %s\n" % e)
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

# **update_entity_model_run_workflow_definition**
> StatusResponse update_entity_model_run_workflow_definition(id, model_run_workflow_definition_domain_info)

Update Item

update_item PUT method to apply an update to an existing item. The  existing item can either be a complete object/item or a seed item of matching category and subtype.  To replace an item, you provide the id of the item as a query string alongside the domain information object that you want to update on that item.   Arguments ---------- id : str     The id of the object in the registry. (Handle) replacement_domain_info : item_domain_info_type     The new domain specific information for that record.  Returns -------  : StatusResponse     Was the update successful?  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.status_response import StatusResponse
from rrap_mds_is_registry_api.model.model_run_workflow_definition_domain_info import ModelRunWorkflowDefinitionDomainInfo
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)
    id = "id_example" # str | 
    model_run_workflow_definition_domain_info = ModelRunWorkflowDefinitionDomainInfo(
        display_name="display_name_example",
        version="version_example",
        software="software_example",
        automation_schedule={},
        input_templates=[
            "input_templates_example",
        ],
        output_templates=[
            "output_templates_example",
        ],
    ) # ModelRunWorkflowDefinitionDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Update Item
        api_response = api_instance.update_entity_model_run_workflow_definition(id, model_run_workflow_definition_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->update_entity_model_run_workflow_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **model_run_workflow_definition_domain_info** | [**ModelRunWorkflowDefinitionDomainInfo**](ModelRunWorkflowDefinitionDomainInfo.md)|  |

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

# **validate_entity_model_run_workflow_definition**
> StatusResponse validate_entity_model_run_workflow_definition(model_run_workflow_definition_domain_info)

Validate

validate Validates the given item body input. If this method responds with a success, then a create_item call  with this input should succeed. Validates in two stages 1) ensures that the pydantic model can parse your input - if this fails, you will receive a 422 error 2) ensures that the provided item category and subtype are correct.  Arguments ---------- item : item_model_type     The item which you want to validate  Returns -------  : StatusResponse     Success or failure object.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import model_run_workflow_definition_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.status_response import StatusResponse
from rrap_mds_is_registry_api.model.model_run_workflow_definition_domain_info import ModelRunWorkflowDefinitionDomainInfo
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
    api_instance = model_run_workflow_definition_api.ModelRunWorkflowDefinitionApi(api_client)
    model_run_workflow_definition_domain_info = ModelRunWorkflowDefinitionDomainInfo(
        display_name="display_name_example",
        version="version_example",
        software="software_example",
        automation_schedule={},
        input_templates=[
            "input_templates_example",
        ],
        output_templates=[
            "output_templates_example",
        ],
    ) # ModelRunWorkflowDefinitionDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Validate
        api_response = api_instance.validate_entity_model_run_workflow_definition(model_run_workflow_definition_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling ModelRunWorkflowDefinitionApi->validate_entity_model_run_workflow_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_run_workflow_definition_domain_info** | [**ModelRunWorkflowDefinitionDomainInfo**](ModelRunWorkflowDefinitionDomainInfo.md)|  |

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

