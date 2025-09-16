# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "UserAccessRequestListResponse",
    "UserAccessRequestListResponseItem",
    "UserAccessRequestListResponseItemGrantedBy",
    "UserAccessRequestListResponseItemGrantedByUnionMember0",
    "UserAccessRequestListResponseItemGrantedByUnionMember0Org",
    "UserAccessRequestListResponseItemUser",
    "UserAccessRequestListResponseItemUserOrg",
]


class UserAccessRequestListResponseItemGrantedByUnionMember0Org(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    name: str


class UserAccessRequestListResponseItemGrantedByUnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_pro: bool = FieldInfo(alias="isPro")

    type: Literal["user"]

    user: str

    details: Optional[str] = None

    email: Optional[str] = None

    is_following: Optional[bool] = FieldInfo(alias="isFollowing", default=None)

    num_datasets: Optional[float] = FieldInfo(alias="numDatasets", default=None)

    num_discussions: Optional[float] = FieldInfo(alias="numDiscussions", default=None)

    num_followers: Optional[float] = FieldInfo(alias="numFollowers", default=None)

    num_following: Optional[float] = FieldInfo(alias="numFollowing", default=None)

    num_likes: Optional[float] = FieldInfo(alias="numLikes", default=None)

    num_models: Optional[float] = FieldInfo(alias="numModels", default=None)

    num_papers: Optional[float] = FieldInfo(alias="numPapers", default=None)

    num_spaces: Optional[float] = FieldInfo(alias="numSpaces", default=None)

    num_upvotes: Optional[float] = FieldInfo(alias="numUpvotes", default=None)

    orgs: Optional[List[UserAccessRequestListResponseItemGrantedByUnionMember0Org]] = None

    reason_to_follow: Optional[str] = FieldInfo(alias="reasonToFollow", default=None)


UserAccessRequestListResponseItemGrantedBy: TypeAlias = Union[
    UserAccessRequestListResponseItemGrantedByUnionMember0, object
]


class UserAccessRequestListResponseItemUserOrg(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    name: str


class UserAccessRequestListResponseItemUser(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_pro: bool = FieldInfo(alias="isPro")

    type: Literal["user"]

    user: str

    details: Optional[str] = None

    email: Optional[str] = None

    is_following: Optional[bool] = FieldInfo(alias="isFollowing", default=None)

    num_datasets: Optional[float] = FieldInfo(alias="numDatasets", default=None)

    num_discussions: Optional[float] = FieldInfo(alias="numDiscussions", default=None)

    num_followers: Optional[float] = FieldInfo(alias="numFollowers", default=None)

    num_following: Optional[float] = FieldInfo(alias="numFollowing", default=None)

    num_likes: Optional[float] = FieldInfo(alias="numLikes", default=None)

    num_models: Optional[float] = FieldInfo(alias="numModels", default=None)

    num_papers: Optional[float] = FieldInfo(alias="numPapers", default=None)

    num_spaces: Optional[float] = FieldInfo(alias="numSpaces", default=None)

    num_upvotes: Optional[float] = FieldInfo(alias="numUpvotes", default=None)

    orgs: Optional[List[UserAccessRequestListResponseItemUserOrg]] = None

    reason_to_follow: Optional[str] = FieldInfo(alias="reasonToFollow", default=None)


class UserAccessRequestListResponseItem(BaseModel):
    status: Literal["accepted", "rejected", "pending"]

    timestamp: datetime

    fields: Optional[Dict[str, str]] = None

    granted_by: Optional[UserAccessRequestListResponseItemGrantedBy] = FieldInfo(alias="grantedBy", default=None)

    user: Optional[UserAccessRequestListResponseItemUser] = None


UserAccessRequestListResponse: TypeAlias = List[UserAccessRequestListResponseItem]
