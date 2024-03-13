from pydantic import Field

from .base_model import BaseModel
from .fragments import CredentialSecretChanged


class TableauCredentialSecretChanged(BaseModel):
    tableau_credential_secret_changed: "TableauCredentialSecretChangedTableauCredentialSecretChanged" = Field(
        alias="tableauCredentialSecretChanged"
    )


class TableauCredentialSecretChangedTableauCredentialSecretChanged(
    CredentialSecretChanged
):
    pass


TableauCredentialSecretChanged.model_rebuild()
TableauCredentialSecretChangedTableauCredentialSecretChanged.model_rebuild()
