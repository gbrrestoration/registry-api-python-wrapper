# rrap-mds-is-registry-api
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import rrap_mds_is_registry_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rrap_mds_is_registry_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import rrap_mds_is_registry_api
from pprint import pprint
from rrap_mds_is_registry_api.api import access_check_api
from rrap_mds_is_registry_api.model.user import User
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
    api_instance = access_check_api.AccessCheckApi(api_client)

    try:
        # Check Admin Access
        api_response = api_instance.check_admin_access()
        pprint(api_response)
    except rrap_mds_is_registry_api.ApiException as e:
        print("Exception when calling AccessCheckApi->check_admin_access: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessCheckApi* | [**check_admin_access**](docs/AccessCheckApi.md#check_admin_access) | **GET** /check-access/check-admin-access | Check Admin Access
*AccessCheckApi* | [**check_general_access**](docs/AccessCheckApi.md#check_general_access) | **GET** /check-access/check-general-access | Check General Access
*AccessCheckApi* | [**check_read_access**](docs/AccessCheckApi.md#check_read_access) | **GET** /check-access/check-read-access | Check Read Access
*AccessCheckApi* | [**check_write_access**](docs/AccessCheckApi.md#check_write_access) | **GET** /check-access/check-write-access | Check Write Access
*DatasetTemplateApi* | [**create_entity_dataset_template**](docs/DatasetTemplateApi.md#create_entity_dataset_template) | **POST** /registry/entity/dataset_template/create | Create Item
*DatasetTemplateApi* | [**delete_entity_dataset_template**](docs/DatasetTemplateApi.md#delete_entity_dataset_template) | **DELETE** /registry/entity/dataset_template/delete | Delete Item
*DatasetTemplateApi* | [**fetch_entity_dataset_template**](docs/DatasetTemplateApi.md#fetch_entity_dataset_template) | **GET** /registry/entity/dataset_template/fetch | Fetch Item
*DatasetTemplateApi* | [**list_entity_dataset_template**](docs/DatasetTemplateApi.md#list_entity_dataset_template) | **GET** /registry/entity/dataset_template/list | List Items
*DatasetTemplateApi* | [**schema_entity_dataset_template**](docs/DatasetTemplateApi.md#schema_entity_dataset_template) | **GET** /registry/entity/dataset_template/schema | Get Schema
*DatasetTemplateApi* | [**seed_entity_dataset_template**](docs/DatasetTemplateApi.md#seed_entity_dataset_template) | **POST** /registry/entity/dataset_template/seed | Seed Item
*DatasetTemplateApi* | [**ui_schema_entity_dataset_template**](docs/DatasetTemplateApi.md#ui_schema_entity_dataset_template) | **GET** /registry/entity/dataset_template/ui_schema | Get Ui Schema
*DatasetTemplateApi* | [**update_entity_dataset_template**](docs/DatasetTemplateApi.md#update_entity_dataset_template) | **PUT** /registry/entity/dataset_template/update | Update Item
*DatasetTemplateApi* | [**validate_entity_dataset_template**](docs/DatasetTemplateApi.md#validate_entity_dataset_template) | **POST** /registry/entity/dataset_template/validate | Validate
*GeneralRegistryApi* | [**fetch**](docs/GeneralRegistryApi.md#fetch) | **GET** /registry/general/fetch | Fetch Item
*GeneralRegistryApi* | [**list**](docs/GeneralRegistryApi.md#list) | **POST** /registry/general/list | List Items
*ModelApi* | [**create_entity_model**](docs/ModelApi.md#create_entity_model) | **POST** /registry/entity/model/create | Create Item
*ModelApi* | [**delete_entity_model**](docs/ModelApi.md#delete_entity_model) | **DELETE** /registry/entity/model/delete | Delete Item
*ModelApi* | [**fetch_entity_model**](docs/ModelApi.md#fetch_entity_model) | **GET** /registry/entity/model/fetch | Fetch Item
*ModelApi* | [**list_entity_model**](docs/ModelApi.md#list_entity_model) | **GET** /registry/entity/model/list | List Items
*ModelApi* | [**schema_entity_model**](docs/ModelApi.md#schema_entity_model) | **GET** /registry/entity/model/schema | Get Schema
*ModelApi* | [**seed_entity_model**](docs/ModelApi.md#seed_entity_model) | **POST** /registry/entity/model/seed | Seed Item
*ModelApi* | [**ui_schema_entity_model**](docs/ModelApi.md#ui_schema_entity_model) | **GET** /registry/entity/model/ui_schema | Get Ui Schema
*ModelApi* | [**update_entity_model**](docs/ModelApi.md#update_entity_model) | **PUT** /registry/entity/model/update | Update Item
*ModelApi* | [**validate_entity_model**](docs/ModelApi.md#validate_entity_model) | **POST** /registry/entity/model/validate | Validate
*ModelRunApi* | [**create_activity_model_run**](docs/ModelRunApi.md#create_activity_model_run) | **POST** /registry/activity/model_run/create | Create Item
*ModelRunApi* | [**delete_activity_model_run**](docs/ModelRunApi.md#delete_activity_model_run) | **DELETE** /registry/activity/model_run/delete | Delete Item
*ModelRunApi* | [**fetch_activity_model_run**](docs/ModelRunApi.md#fetch_activity_model_run) | **GET** /registry/activity/model_run/fetch | Fetch Item
*ModelRunApi* | [**list_activity_model_run**](docs/ModelRunApi.md#list_activity_model_run) | **GET** /registry/activity/model_run/list | List Items
*ModelRunApi* | [**schema_activity_model_run**](docs/ModelRunApi.md#schema_activity_model_run) | **GET** /registry/activity/model_run/schema | Get Schema
*ModelRunApi* | [**seed_activity_model_run**](docs/ModelRunApi.md#seed_activity_model_run) | **POST** /registry/activity/model_run/seed | Seed Item
*ModelRunApi* | [**ui_schema_activity_model_run**](docs/ModelRunApi.md#ui_schema_activity_model_run) | **GET** /registry/activity/model_run/ui_schema | Get Ui Schema
*ModelRunApi* | [**update_activity_model_run**](docs/ModelRunApi.md#update_activity_model_run) | **PUT** /registry/activity/model_run/update | Update Item
*ModelRunApi* | [**validate_activity_model_run**](docs/ModelRunApi.md#validate_activity_model_run) | **POST** /registry/activity/model_run/validate | Validate
*ModelRunWorkflowDefinitionApi* | [**create_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#create_entity_model_run_workflow_definition) | **POST** /registry/entity/model_run_workflow/create | Create Item
*ModelRunWorkflowDefinitionApi* | [**delete_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#delete_entity_model_run_workflow_definition) | **DELETE** /registry/entity/model_run_workflow/delete | Delete Item
*ModelRunWorkflowDefinitionApi* | [**fetch_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#fetch_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/fetch | Fetch Item
*ModelRunWorkflowDefinitionApi* | [**list_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#list_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/list | List Items
*ModelRunWorkflowDefinitionApi* | [**schema_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#schema_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/schema | Get Schema
*ModelRunWorkflowDefinitionApi* | [**seed_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#seed_entity_model_run_workflow_definition) | **POST** /registry/entity/model_run_workflow/seed | Seed Item
*ModelRunWorkflowDefinitionApi* | [**ui_schema_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#ui_schema_entity_model_run_workflow_definition) | **GET** /registry/entity/model_run_workflow/ui_schema | Get Ui Schema
*ModelRunWorkflowDefinitionApi* | [**update_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#update_entity_model_run_workflow_definition) | **PUT** /registry/entity/model_run_workflow/update | Update Item
*ModelRunWorkflowDefinitionApi* | [**validate_entity_model_run_workflow_definition**](docs/ModelRunWorkflowDefinitionApi.md#validate_entity_model_run_workflow_definition) | **POST** /registry/entity/model_run_workflow/validate | Validate
*OrganisationApi* | [**create_agent_organisation**](docs/OrganisationApi.md#create_agent_organisation) | **POST** /registry/agent/organisation/create | Create Item
*OrganisationApi* | [**delete_agent_organisation**](docs/OrganisationApi.md#delete_agent_organisation) | **DELETE** /registry/agent/organisation/delete | Delete Item
*OrganisationApi* | [**fetch_agent_organisation**](docs/OrganisationApi.md#fetch_agent_organisation) | **GET** /registry/agent/organisation/fetch | Fetch Item
*OrganisationApi* | [**list_agent_organisation**](docs/OrganisationApi.md#list_agent_organisation) | **GET** /registry/agent/organisation/list | List Items
*OrganisationApi* | [**schema_agent_organisation**](docs/OrganisationApi.md#schema_agent_organisation) | **GET** /registry/agent/organisation/schema | Get Schema
*OrganisationApi* | [**seed_agent_organisation**](docs/OrganisationApi.md#seed_agent_organisation) | **POST** /registry/agent/organisation/seed | Seed Item
*OrganisationApi* | [**ui_schema_agent_organisation**](docs/OrganisationApi.md#ui_schema_agent_organisation) | **GET** /registry/agent/organisation/ui_schema | Get Ui Schema
*OrganisationApi* | [**update_agent_organisation**](docs/OrganisationApi.md#update_agent_organisation) | **PUT** /registry/agent/organisation/update | Update Item
*OrganisationApi* | [**validate_agent_organisation**](docs/OrganisationApi.md#validate_agent_organisation) | **POST** /registry/agent/organisation/validate | Validate
*PersonApi* | [**create_agent_person**](docs/PersonApi.md#create_agent_person) | **POST** /registry/agent/person/create | Create Item
*PersonApi* | [**delete_agent_person**](docs/PersonApi.md#delete_agent_person) | **DELETE** /registry/agent/person/delete | Delete Item
*PersonApi* | [**fetch_agent_person**](docs/PersonApi.md#fetch_agent_person) | **GET** /registry/agent/person/fetch | Fetch Item
*PersonApi* | [**list_agent_person**](docs/PersonApi.md#list_agent_person) | **GET** /registry/agent/person/list | List Items
*PersonApi* | [**schema_agent_person**](docs/PersonApi.md#schema_agent_person) | **GET** /registry/agent/person/schema | Get Schema
*PersonApi* | [**seed_agent_person**](docs/PersonApi.md#seed_agent_person) | **POST** /registry/agent/person/seed | Seed Item
*PersonApi* | [**ui_schema_agent_person**](docs/PersonApi.md#ui_schema_agent_person) | **GET** /registry/agent/person/ui_schema | Get Ui Schema
*PersonApi* | [**update_agent_person**](docs/PersonApi.md#update_agent_person) | **PUT** /registry/agent/person/update | Update Item
*PersonApi* | [**validate_agent_person**](docs/PersonApi.md#validate_agent_person) | **POST** /registry/agent/person/validate | Validate
*DefaultApi* | [**root**](docs/DefaultApi.md#root) | **GET** / | Root


## Documentation For Models

 - [AssociationInfo](docs/AssociationInfo.md)
 - [DataStoreDatasetResource](docs/DataStoreDatasetResource.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetParameter](docs/DatasetParameter.md)
 - [DatasetStructuralTemplate](docs/DatasetStructuralTemplate.md)
 - [DatasetTemplateCreateResponse](docs/DatasetTemplateCreateResponse.md)
 - [DatasetTemplateDomainInfo](docs/DatasetTemplateDomainInfo.md)
 - [DatasetTemplateFetchResponse](docs/DatasetTemplateFetchResponse.md)
 - [DatasetTemplateListResponse](docs/DatasetTemplateListResponse.md)
 - [DatasetTemplateSeedResponse](docs/DatasetTemplateSeedResponse.md)
 - [DatasetTemporalInformation](docs/DatasetTemporalInformation.md)
 - [DatasetType](docs/DatasetType.md)
 - [DatasetUsageInformation](docs/DatasetUsageInformation.md)
 - [DatasetUsageType](docs/DatasetUsageType.md)
 - [FileInformation](docs/FileInformation.md)
 - [FileSystemResource](docs/FileSystemResource.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [InputInfo](docs/InputInfo.md)
 - [Item](docs/Item.md)
 - [Item1](docs/Item1.md)
 - [Item2](docs/Item2.md)
 - [Item3](docs/Item3.md)
 - [Item4](docs/Item4.md)
 - [Item5](docs/Item5.md)
 - [ItemCategory](docs/ItemCategory.md)
 - [ItemDatasetTemplate](docs/ItemDatasetTemplate.md)
 - [ItemModel](docs/ItemModel.md)
 - [ItemModelRun](docs/ItemModelRun.md)
 - [ItemModelRunWorkflowDefinition](docs/ItemModelRunWorkflowDefinition.md)
 - [ItemOrganisation](docs/ItemOrganisation.md)
 - [ItemPerson](docs/ItemPerson.md)
 - [ItemSubType](docs/ItemSubType.md)
 - [LocationInner](docs/LocationInner.md)
 - [ModelCreateResponse](docs/ModelCreateResponse.md)
 - [ModelDomainInfo](docs/ModelDomainInfo.md)
 - [ModelFetchResponse](docs/ModelFetchResponse.md)
 - [ModelListResponse](docs/ModelListResponse.md)
 - [ModelRunCreateResponse](docs/ModelRunCreateResponse.md)
 - [ModelRunDomainInfo](docs/ModelRunDomainInfo.md)
 - [ModelRunFetchResponse](docs/ModelRunFetchResponse.md)
 - [ModelRunListResponse](docs/ModelRunListResponse.md)
 - [ModelRunRecord](docs/ModelRunRecord.md)
 - [ModelRunSeedResponse](docs/ModelRunSeedResponse.md)
 - [ModelRunWorkflowDefinitionCreateResponse](docs/ModelRunWorkflowDefinitionCreateResponse.md)
 - [ModelRunWorkflowDefinitionDomainInfo](docs/ModelRunWorkflowDefinitionDomainInfo.md)
 - [ModelRunWorkflowDefinitionFetchResponse](docs/ModelRunWorkflowDefinitionFetchResponse.md)
 - [ModelRunWorkflowDefinitionListResponse](docs/ModelRunWorkflowDefinitionListResponse.md)
 - [ModelRunWorkflowDefinitionResource](docs/ModelRunWorkflowDefinitionResource.md)
 - [ModelRunWorkflowDefinitionSeedResponse](docs/ModelRunWorkflowDefinitionSeedResponse.md)
 - [ModelSeedResponse](docs/ModelSeedResponse.md)
 - [ModellerResource](docs/ModellerResource.md)
 - [OrganisationCreateResponse](docs/OrganisationCreateResponse.md)
 - [OrganisationDomainInfo](docs/OrganisationDomainInfo.md)
 - [OrganisationFetchResponse](docs/OrganisationFetchResponse.md)
 - [OrganisationListResponse](docs/OrganisationListResponse.md)
 - [OrganisationResource](docs/OrganisationResource.md)
 - [OrganisationSeedResponse](docs/OrganisationSeedResponse.md)
 - [OutputInfo](docs/OutputInfo.md)
 - [PersonCreateResponse](docs/PersonCreateResponse.md)
 - [PersonDomainInfo](docs/PersonDomainInfo.md)
 - [PersonFetchResponse](docs/PersonFetchResponse.md)
 - [PersonListResponse](docs/PersonListResponse.md)
 - [PersonSeedResponse](docs/PersonSeedResponse.md)
 - [QueryFilter](docs/QueryFilter.md)
 - [SchemaResponse](docs/SchemaResponse.md)
 - [SeededItem](docs/SeededItem.md)
 - [Status](docs/Status.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [TemplateResource](docs/TemplateResource.md)
 - [TemplatedDataset](docs/TemplatedDataset.md)
 - [URLDatasetResource](docs/URLDatasetResource.md)
 - [UiSchemaResponse](docs/UiSchemaResponse.md)
 - [UnparsedListResponse](docs/UnparsedListResponse.md)
 - [UntypedFetchResponse](docs/UntypedFetchResponse.md)
 - [User](docs/User.md)
 - [ValidationError](docs/ValidationError.md)
 - [WorkflowRunCompletionStatus](docs/WorkflowRunCompletionStatus.md)


## Documentation For Authorization


## OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in rrap_mds_is_registry_api.apis and rrap_mds_is_registry_api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from rrap_mds_is_registry_api.api.default_api import DefaultApi`
- `from rrap_mds_is_registry_api.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import rrap_mds_is_registry_api
from rrap_mds_is_registry_api.apis import *
from rrap_mds_is_registry_api.models import *
```

