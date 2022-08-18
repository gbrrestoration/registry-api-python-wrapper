
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from rrap_mds_is_registry_api.api.access_check_api import AccessCheckApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from rrap_mds_is_registry_api.api.access_check_api import AccessCheckApi
from rrap_mds_is_registry_api.api.dataset_template_api import DatasetTemplateApi
from rrap_mds_is_registry_api.api.general_registry_api import GeneralRegistryApi
from rrap_mds_is_registry_api.api.model_api import ModelApi
from rrap_mds_is_registry_api.api.model_run_api import ModelRunApi
from rrap_mds_is_registry_api.api.model_run_workflow_definition_api import ModelRunWorkflowDefinitionApi
from rrap_mds_is_registry_api.api.organisation_api import OrganisationApi
from rrap_mds_is_registry_api.api.person_api import PersonApi
from rrap_mds_is_registry_api.api.default_api import DefaultApi
