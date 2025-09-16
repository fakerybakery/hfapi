# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DiscussionChangeStatusResponse",
    "NewStatus",
    "NewStatusData",
    "NewStatusAuthor",
    "NewStatusAuthorUnionMember0",
    "NewStatusAuthorUnionMember0OAuthApp",
    "NewStatusAuthorUnionMember0OAuthAppImageData",
    "NewStatusAuthorUnionMember1",
    "NewStatusAuthorUnionMember1OAuthApp",
    "NewStatusAuthorUnionMember1OAuthAppImageData",
]


class NewStatusData(BaseModel):
    status: Literal["draft", "open", "closed", "merged"]

    reason: Optional[str] = None


class NewStatusAuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class NewStatusAuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[NewStatusAuthorUnionMember0OAuthAppImageData] = FieldInfo(alias="imageData", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class NewStatusAuthorUnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    name: str

    type: Literal["org"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_org_member: Optional[bool] = FieldInfo(alias="isOrgMember", default=None)

    is_owner: Optional[bool] = FieldInfo(alias="isOwner", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)

    oauth_app: Optional[NewStatusAuthorUnionMember0OAuthApp] = FieldInfo(alias="oauthApp", default=None)


class NewStatusAuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class NewStatusAuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[NewStatusAuthorUnionMember1OAuthAppImageData] = FieldInfo(alias="imageData", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class NewStatusAuthorUnionMember1(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    is_hf_admin: bool = FieldInfo(alias="isHfAdmin")

    is_mod: bool = FieldInfo(alias="isMod")

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: Literal["user"]

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_org_member: Optional[bool] = FieldInfo(alias="isOrgMember", default=None)

    is_owner: Optional[bool] = FieldInfo(alias="isOwner", default=None)

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)

    oauth_app: Optional[NewStatusAuthorUnionMember1OAuthApp] = FieldInfo(alias="oauthApp", default=None)


NewStatusAuthor: TypeAlias = Union[NewStatusAuthorUnionMember0, NewStatusAuthorUnionMember1]


class NewStatus(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: NewStatusData

    type: Literal["status-change"]

    author: Optional[NewStatusAuthor] = None


class DiscussionChangeStatusResponse(BaseModel):
    new_status: NewStatus = FieldInfo(alias="newStatus")
