from amsdal.cloud.constants import AMSDAL_ENV_SUBDOMAIN as AMSDAL_ENV_SUBDOMAIN
from amsdal.cloud.models.base import DeployResponse as DeployResponse
from amsdal.cloud.services.actions.base import CloudActionBase as CloudActionBase
from amsdal.errors import AmsdalCloudAlreadyDeployedError as AmsdalCloudAlreadyDeployedError
from typing import Any

class CreateDeployAction(CloudActionBase):
    def want_deploy_input(self) -> str: ...
    def want_redeploy_input(self) -> str: ...
    def action(self, deploy_type: str, lakehouse_type: str, application_uuid: str | None = None, application_name: str | None = None) -> bool: ...
    def _redeploy(self, deploy_data: dict[str, Any]) -> bool: ...
