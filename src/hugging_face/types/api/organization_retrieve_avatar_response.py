# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OrganizationRetrieveAvatarResponse"]


class OrganizationRetrieveAvatarResponse(BaseModel):
    avatar_url: str = FieldInfo(alias="avatarUrl")
