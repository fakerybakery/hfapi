# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = ["UserUpdateAttributesResponse", "Email", "Meta", "Name"]


class Email(BaseModel):
    primary: bool

    value: str

    type: Optional[Literal["work"]] = None
    """We only support work emails, other types are converted to work"""


class Meta(BaseModel):
    location: str

    resource_type: Literal["User"] = FieldInfo(alias="resourceType")


class Name(BaseModel):
    family_name: str = FieldInfo(alias="familyName")

    formatted: str

    given_name: str = FieldInfo(alias="givenName")


class UserUpdateAttributesResponse(BaseModel):
    id: str

    active: bool

    display_name: str = FieldInfo(alias="displayName")

    emails: List[Email]

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    meta: Meta

    name: Name

    schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]]

    user_name: str = FieldInfo(alias="userName")
