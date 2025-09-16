# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = ["GroupUpdateAttributesResponse", "Member", "Meta"]


class Member(BaseModel):
    value: str


class Meta(BaseModel):
    location: str

    resource_type: Literal["Group"] = FieldInfo(alias="resourceType")


class GroupUpdateAttributesResponse(BaseModel):
    id: str

    display_name: str = FieldInfo(alias="displayName")

    members: List[Member]

    meta: Meta

    schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:Group"]]

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
