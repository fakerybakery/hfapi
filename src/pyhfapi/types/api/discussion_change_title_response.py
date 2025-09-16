# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DiscussionChangeTitleResponse",
    "NewTitle",
    "NewTitleData",
    "NewTitleAuthor",
    "NewTitleAuthorUnionMember0",
    "NewTitleAuthorUnionMember0OAuthApp",
    "NewTitleAuthorUnionMember0OAuthAppImageData",
    "NewTitleAuthorUnionMember1",
    "NewTitleAuthorUnionMember1OAuthApp",
    "NewTitleAuthorUnionMember1OAuthAppImageData",
]


class NewTitleData(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: str


class NewTitleAuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class NewTitleAuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[NewTitleAuthorUnionMember0OAuthAppImageData] = FieldInfo(alias="imageData", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class NewTitleAuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[NewTitleAuthorUnionMember0OAuthApp] = FieldInfo(alias="oauthApp", default=None)


class NewTitleAuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class NewTitleAuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[NewTitleAuthorUnionMember1OAuthAppImageData] = FieldInfo(alias="imageData", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class NewTitleAuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[NewTitleAuthorUnionMember1OAuthApp] = FieldInfo(alias="oauthApp", default=None)


NewTitleAuthor: TypeAlias = Union[NewTitleAuthorUnionMember0, NewTitleAuthorUnionMember1]


class NewTitle(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: NewTitleData

    type: Literal["title-change"]

    author: Optional[NewTitleAuthor] = None


class DiscussionChangeTitleResponse(BaseModel):
    new_title: NewTitle = FieldInfo(alias="newTitle")
