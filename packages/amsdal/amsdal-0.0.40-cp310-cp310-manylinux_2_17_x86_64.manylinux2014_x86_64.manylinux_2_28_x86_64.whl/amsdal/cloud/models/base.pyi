from amsdal.cloud.enums import ResponseStatus as ResponseStatus
from pydantic import BaseModel
from typing import Any

class ResponseBaseModel(BaseModel):
    status: ResponseStatus
    errors: list[str] | None

class DeployResponse(BaseModel):
    status: str
    client_id: str
    deployment_id: str
    created_at: float
    last_update_at: float
    application_uuid: str | None
    application_name: str | None
    domain_url: str | None

class UpdateDeployStatusResponse(BaseModel):
    status: str
    deployment_id: str
    created_at: float
    last_update_at: float
    updated: bool

class ListDeployResponse(BaseModel):
    deployments: list[DeployResponse]

class DeployTransactionResponse(ResponseBaseModel):
    details: DeployResponse | UpdateDeployStatusResponse | ListDeployResponse | None

class ListSecretsDetails(BaseModel):
    secrets: list[str]

class ListSecretsResponse(ResponseBaseModel):
    details: ListSecretsDetails | None

class SignupReponseCredentials(BaseModel):
    amsdal_access_key_id: str
    amsdal_secret_access_key: str

class SignupResponse(ResponseBaseModel):
    details: SignupReponseCredentials | None

class CreateSessionDetails(BaseModel):
    token: str

class CreateSessionResponse(ResponseBaseModel):
    details: CreateSessionDetails | None

class ListDependenciesDetails(BaseModel):
    dependencies: list[str]

class ListApplicationDependenciesResponse(ResponseBaseModel):
    details: ListDependenciesDetails | None

class ExposeApplicationDBResponse(ResponseBaseModel):
    details: dict[str, Any] | None
