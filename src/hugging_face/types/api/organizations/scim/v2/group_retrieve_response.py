# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = ["GroupRetrieveResponse", "Meta", "Member"]


class Meta(BaseModel):
    location: str

    resource_type: Literal["Group"] = FieldInfo(alias="resourceType")


class Member(BaseModel):
    value: str


class GroupRetrieveResponse(BaseModel):
    id: str

    display_name: str = FieldInfo(alias="displayName")

    meta: Meta

    schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:Group"]]

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    members: Optional[List[Member]] = None
