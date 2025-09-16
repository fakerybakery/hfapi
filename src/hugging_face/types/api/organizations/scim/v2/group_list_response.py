# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = ["GroupListResponse", "Resource", "ResourceMeta", "ResourceMember"]


class ResourceMeta(BaseModel):
    location: str

    resource_type: Literal["Group"] = FieldInfo(alias="resourceType")


class ResourceMember(BaseModel):
    value: str


class Resource(BaseModel):
    id: str

    display_name: str = FieldInfo(alias="displayName")

    meta: ResourceMeta

    schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:Group"]]

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    members: Optional[List[ResourceMember]] = None


class GroupListResponse(BaseModel):
    items_per_page: int = FieldInfo(alias="itemsPerPage")

    resources: List[Resource] = FieldInfo(alias="Resources")

    schemas: List[Literal["urn:ietf:params:scim:api:messages:2.0:ListResponse"]]

    start_index: int = FieldInfo(alias="startIndex")

    total_results: int = FieldInfo(alias="totalResults")
