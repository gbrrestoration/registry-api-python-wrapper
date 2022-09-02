# rrap_mds_is_registry_api.OrganisationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_organisation**](OrganisationApi.md#create_agent_organisation) | **POST** /registry/agent/organisation/create | Create Item
[**delete_agent_organisation**](OrganisationApi.md#delete_agent_organisation) | **DELETE** /registry/agent/organisation/delete | Delete Item
[**fetch_agent_organisation**](OrganisationApi.md#fetch_agent_organisation) | **GET** /registry/agent/organisation/fetch | Fetch Item
[**list_agent_organisation**](OrganisationApi.md#list_agent_organisation) | **GET** /registry/agent/organisation/list | List Items
[**schema_agent_organisation**](OrganisationApi.md#schema_agent_organisation) | **GET** /registry/agent/organisation/schema | Get Schema
[**seed_agent_organisation**](OrganisationApi.md#seed_agent_organisation) | **POST** /registry/agent/organisation/seed | Seed Item
[**ui_schema_agent_organisation**](OrganisationApi.md#ui_schema_agent_organisation) | **GET** /registry/agent/organisation/ui_schema | Get Ui Schema
[**update_agent_organisation**](OrganisationApi.md#update_agent_organisation) | **PUT** /registry/agent/organisation/update | Update Item
[**validate_agent_organisation**](OrganisationApi.md#validate_agent_organisation) | **POST** /registry/agent/organisation/validate | Validate


# **create_agent_organisation**
> OrganisationCreateResponse create_agent_organisation(organisation_domain_info)

Create Item

create_item POSTs a new item to the registry of the given item type.  The item does not need to include an id or creation time  as these will be automatically generated during creation.  Responds with the successfully created item.  If you want to seed an identity without providing full information, you can use the seed endpoint and then use the update endpoint later.  Arguments ---------- item : item_model_type     The item you want to create.  Returns -------  : GenericCreateResponse     The create response which will include a status and the item      created (if it was successful).  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
from rrap_mds_is_registry_api.model.organisation_create_response import OrganisationCreateResponse
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.organisation_domain_info import OrganisationDomainInfo
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
    api_instance = organisation_api.OrganisationApi(api_client)
    organisation_domain_info = OrganisationDomainInfo(
        display_name="display_name_example",
        name="name_example",
        ror="ror_example",
    ) # OrganisationDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Create Item
        api_response = api_instance.create_agent_organisation(organisation_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->create_agent_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_domain_info** | [**OrganisationDomainInfo**](OrganisationDomainInfo.md)|  |

### Return type

[**OrganisationCreateResponse**](OrganisationCreateResponse.md)

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

# **delete_agent_organisation**
> StatusResponse delete_agent_organisation(id)

Delete Item

delete_item Admin only endpoint which can be used to delete  objects from the registry. Delete is by ID. This endpoint will return successfully even if the object doesn't exist in the first place.  Arguments ---------- id : str     The handle ID of the object to delete  Returns -------  : StatusResponse     Was the deletion successful - returns true even if the item      did not exist.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Item
        api_response = api_instance.delete_agent_organisation(id)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->delete_agent_organisation: %s\n" % e)
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

# **fetch_agent_organisation**
> OrganisationFetchResponse fetch_agent_organisation(id)

Fetch Item

fetch_item Fetches the item specified by the id from the  registry. Only returns items which fit the specified item type in this route, or if you allow with the  seed_allowed flag, will return seed items of  matching category and subtype.  Arguments ---------- id : str     The handle id of the item to fetch. seed_allowed : bool, optional     Do you want to allow seed items to be returned, by default False  Returns -------  : GenericFetchResponse     Returns a status and possibly the item.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.organisation_fetch_response import OrganisationFetchResponse
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    seed_allowed = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Fetch Item
        api_response = api_instance.fetch_agent_organisation(id)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->fetch_agent_organisation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch Item
        api_response = api_instance.fetch_agent_organisation(id, seed_allowed=seed_allowed)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->fetch_agent_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **seed_allowed** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**OrganisationFetchResponse**](OrganisationFetchResponse.md)

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

# **list_agent_organisation**
> OrganisationListResponse list_agent_organisation()

List Items

list_items Lists all items of the specified type (by route). Sorts items  into parsable complete entities (i.e. normal entities), parsable  seed items (i.e. incomplete), and completely unparsable entities.   If there are any unparsable entities, the success field of the return  status will be False, however the items will still be provided.   Arguments ----------  Returns -------  : GenericListResponse     The list of items, sorted complete, seed and unparsable, as well      as counts for each type.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
from rrap_mds_is_registry_api.model.organisation_list_response import OrganisationListResponse
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
    api_instance = organisation_api.OrganisationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Items
        api_response = api_instance.list_agent_organisation()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->list_agent_organisation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganisationListResponse**](OrganisationListResponse.md)

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

# **schema_agent_organisation**
> JsonSchemaResponse schema_agent_organisation()

Get Schema

get_schema Returns the auto generated pydantic model  json schema.   This method uses only the domain info component of the item to ensure compliance with update and create endpoints.   This can be used to programmatically generate input forms, or to validate against the  pydantic model. You can also use the /validate  endpoint.  Arguments ----------  Returns -------  : SchemaResponse     Response with a json schema object.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
from rrap_mds_is_registry_api.model.json_schema_response import JsonSchemaResponse
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
    api_instance = organisation_api.OrganisationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Schema
        api_response = api_instance.schema_agent_organisation()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->schema_agent_organisation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonSchemaResponse**](JsonSchemaResponse.md)

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

# **seed_agent_organisation**
> OrganisationSeedResponse seed_agent_organisation()

Seed Item

seed_item Posts a new empty item. This will mint a handle,  set the creation time, and produce the correct  category and sub type. This can then be updated  later using the update endpoint.  Arguments ----------  Returns -------  : GenericSeedResponse     The seed item that was created.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
from rrap_mds_is_registry_api.model.organisation_seed_response import OrganisationSeedResponse
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
    api_instance = organisation_api.OrganisationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Seed Item
        api_response = api_instance.seed_agent_organisation()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->seed_agent_organisation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganisationSeedResponse**](OrganisationSeedResponse.md)

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

# **ui_schema_agent_organisation**
> UiSchemaResponse ui_schema_agent_organisation()

Get Ui Schema

Returns the ui schema override provided for this model.  This is for use by the front end - enabling overriding of specific model fields with specific components.   Parameters ---------- protected_roles : ProtectedRole, optional     _description_, by default Depends( read_user_protected_role_dependency)  Returns ------- UiSchemaResponse     A JSON style mapping of field names (possibly nested) to component overrides.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Ui Schema
        api_response = api_instance.ui_schema_agent_organisation()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->ui_schema_agent_organisation: %s\n" % e)
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

# **update_agent_organisation**
> StatusResponse update_agent_organisation(id, organisation_domain_info)

Update Item

update_item PUT method to apply an update to an existing item. The  existing item can either be a complete object/item or a seed item of matching category and subtype.  To replace an item, you provide the id of the item as a query string alongside the domain information object that you want to update on that item.   Arguments ---------- id : str     The id of the object in the registry. (Handle) replacement_domain_info : item_domain_info_type     The new domain specific information for that record.  Returns -------  : StatusResponse     Was the update successful?  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.status_response import StatusResponse
from rrap_mds_is_registry_api.model.organisation_domain_info import OrganisationDomainInfo
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    organisation_domain_info = OrganisationDomainInfo(
        display_name="display_name_example",
        name="name_example",
        ror="ror_example",
    ) # OrganisationDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Update Item
        api_response = api_instance.update_agent_organisation(id, organisation_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->update_agent_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **organisation_domain_info** | [**OrganisationDomainInfo**](OrganisationDomainInfo.md)|  |

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

# **validate_agent_organisation**
> StatusResponse validate_agent_organisation(organisation_domain_info)

Validate

validate Validates the given item body input. If this method responds with a success, then a create_item call  with this input should succeed. Validates in two stages 1) ensures that the pydantic model can parse your input - if this fails, you will receive a 422 error 2) ensures that the provided item category and subtype are correct.  Arguments ---------- item : item_model_type     The item which you want to validate  Returns -------  : StatusResponse     Success or failure object.  See Also (optional) --------  Examples (optional) --------

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import time
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.api import organisation_api
from rrap_mds_is_registry_api.model.http_validation_error import HTTPValidationError
from rrap_mds_is_registry_api.model.status_response import StatusResponse
from rrap_mds_is_registry_api.model.organisation_domain_info import OrganisationDomainInfo
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
    api_instance = organisation_api.OrganisationApi(api_client)
    organisation_domain_info = OrganisationDomainInfo(
        display_name="display_name_example",
        name="name_example",
        ror="ror_example",
    ) # OrganisationDomainInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Validate
        api_response = api_instance.validate_agent_organisation(organisation_domain_info)
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling OrganisationApi->validate_agent_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_domain_info** | [**OrganisationDomainInfo**](OrganisationDomainInfo.md)|  |

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

