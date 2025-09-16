# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "OrganizationListMembersResponse",
    "OrganizationListMembersResponseItem",
    "OrganizationListMembersResponseItemResourceGroup",
]


class OrganizationListMembersResponseItemResourceGroup(BaseModel):
    id: str

    name: str

    num_users: float = FieldInfo(alias="numUsers")

    role: Literal["admin", "write", "contributor", "read"]


class OrganizationListMembersResponseItem(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_pro: bool = FieldInfo(alias="isPro")

    type: Literal["user"]

    user: str

    is_external_collaborator: Optional[bool] = FieldInfo(alias="isExternalCollaborator", default=None)

    is_following: Optional[bool] = FieldInfo(alias="isFollowing", default=None)

    resource_groups: Optional[List[OrganizationListMembersResponseItemResourceGroup]] = FieldInfo(
        alias="resourceGroups", default=None
    )

    role: Optional[Literal["admin", "write", "contributor", "read"]] = None

    two_fa_enabled: Optional[bool] = FieldInfo(alias="twoFaEnabled", default=None)

    verified_email: Optional[str] = FieldInfo(alias="verifiedEmail", default=None)


OrganizationListMembersResponse: TypeAlias = List[OrganizationListMembersResponseItem]
