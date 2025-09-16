# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = ["UserListResponse", "Resource", "ResourceEmail", "ResourceMeta", "ResourceName"]


class ResourceEmail(BaseModel):
    primary: bool

    value: str

    type: Optional[Literal["work"]] = None
    """We only support work emails, other types are converted to work"""


class ResourceMeta(BaseModel):
    location: str

    resource_type: Literal["User"] = FieldInfo(alias="resourceType")


class ResourceName(BaseModel):
    family_name: str = FieldInfo(alias="familyName")

    formatted: str

    given_name: str = FieldInfo(alias="givenName")


class Resource(BaseModel):
    id: str

    active: bool

    display_name: str = FieldInfo(alias="displayName")

    emails: List[ResourceEmail]

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    meta: ResourceMeta

    name: ResourceName

    schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]]

    user_name: str = FieldInfo(alias="userName")


class UserListResponse(BaseModel):
    items_per_page: int = FieldInfo(alias="itemsPerPage")

    resources: List[Resource] = FieldInfo(alias="Resources")

    schemas: List[Literal["urn:ietf:params:scim:api:messages:2.0:ListResponse"]]

    start_index: int = FieldInfo(alias="startIndex")

    total_results: int = FieldInfo(alias="totalResults")
