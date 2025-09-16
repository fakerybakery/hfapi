# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .organizations.repo_id import RepoID

__all__ = [
    "DiscussionRetrieveResponse",
    "UnionMember0",
    "UnionMember0Event",
    "UnionMember0EventUnionMember0",
    "UnionMember0EventUnionMember0Data",
    "UnionMember0EventUnionMember0DataLatest",
    "UnionMember0EventUnionMember0DataLatestAuthor",
    "UnionMember0EventUnionMember0DataLatestAuthorUnionMember0",
    "UnionMember0EventUnionMember0DataLatestAuthorUnionMember1",
    "UnionMember0EventUnionMember0DataReaction",
    "UnionMember0EventUnionMember0DataIdentifiedLanguage",
    "UnionMember0EventUnionMember0Author",
    "UnionMember0EventUnionMember0AuthorUnionMember0",
    "UnionMember0EventUnionMember0AuthorUnionMember0OAuthApp",
    "UnionMember0EventUnionMember0AuthorUnionMember0OAuthAppImageData",
    "UnionMember0EventUnionMember0AuthorUnionMember1",
    "UnionMember0EventUnionMember0AuthorUnionMember1OAuthApp",
    "UnionMember0EventUnionMember0AuthorUnionMember1OAuthAppImageData",
    "UnionMember0EventUnionMember1",
    "UnionMember0EventUnionMember1Data",
    "UnionMember0EventUnionMember1Author",
    "UnionMember0EventUnionMember1AuthorUnionMember0",
    "UnionMember0EventUnionMember1AuthorUnionMember0OAuthApp",
    "UnionMember0EventUnionMember1AuthorUnionMember0OAuthAppImageData",
    "UnionMember0EventUnionMember1AuthorUnionMember1",
    "UnionMember0EventUnionMember1AuthorUnionMember1OAuthApp",
    "UnionMember0EventUnionMember1AuthorUnionMember1OAuthAppImageData",
    "UnionMember0EventUnionMember2",
    "UnionMember0EventUnionMember2Data",
    "UnionMember0EventUnionMember2Author",
    "UnionMember0EventUnionMember2AuthorUnionMember0",
    "UnionMember0EventUnionMember2AuthorUnionMember0OAuthApp",
    "UnionMember0EventUnionMember2AuthorUnionMember0OAuthAppImageData",
    "UnionMember0EventUnionMember2AuthorUnionMember1",
    "UnionMember0EventUnionMember2AuthorUnionMember1OAuthApp",
    "UnionMember0EventUnionMember2AuthorUnionMember1OAuthAppImageData",
    "UnionMember0EventUnionMember3",
    "UnionMember0EventUnionMember3Data",
    "UnionMember0EventUnionMember3Author",
    "UnionMember0EventUnionMember3AuthorUnionMember0",
    "UnionMember0EventUnionMember3AuthorUnionMember0OAuthApp",
    "UnionMember0EventUnionMember3AuthorUnionMember0OAuthAppImageData",
    "UnionMember0EventUnionMember3AuthorUnionMember1",
    "UnionMember0EventUnionMember3AuthorUnionMember1OAuthApp",
    "UnionMember0EventUnionMember3AuthorUnionMember1OAuthAppImageData",
    "UnionMember0EventUnionMember4",
    "UnionMember0EventUnionMember4Data",
    "UnionMember0EventUnionMember4Author",
    "UnionMember0EventUnionMember4AuthorUnionMember0",
    "UnionMember0EventUnionMember4AuthorUnionMember0OAuthApp",
    "UnionMember0EventUnionMember4AuthorUnionMember0OAuthAppImageData",
    "UnionMember0EventUnionMember4AuthorUnionMember1",
    "UnionMember0EventUnionMember4AuthorUnionMember1OAuthApp",
    "UnionMember0EventUnionMember4AuthorUnionMember1OAuthAppImageData",
    "UnionMember0EventUnionMember5",
    "UnionMember0EventUnionMember5Data",
    "UnionMember0EventUnionMember5Author",
    "UnionMember0EventUnionMember5AuthorUnionMember0",
    "UnionMember0EventUnionMember5AuthorUnionMember0OAuthApp",
    "UnionMember0EventUnionMember5AuthorUnionMember0OAuthAppImageData",
    "UnionMember0EventUnionMember5AuthorUnionMember1",
    "UnionMember0EventUnionMember5AuthorUnionMember1OAuthApp",
    "UnionMember0EventUnionMember5AuthorUnionMember1OAuthAppImageData",
    "UnionMember0EventUnionMember6",
    "UnionMember0EventUnionMember6Data",
    "UnionMember0EventUnionMember6Author",
    "UnionMember0EventUnionMember6AuthorUnionMember0",
    "UnionMember0EventUnionMember6AuthorUnionMember0OAuthApp",
    "UnionMember0EventUnionMember6AuthorUnionMember0OAuthAppImageData",
    "UnionMember0EventUnionMember6AuthorUnionMember1",
    "UnionMember0EventUnionMember6AuthorUnionMember1OAuthApp",
    "UnionMember0EventUnionMember6AuthorUnionMember1OAuthAppImageData",
    "UnionMember0Author",
    "UnionMember0AuthorUnionMember0",
    "UnionMember0AuthorUnionMember1",
    "UnionMember0Org",
    "UnionMember1",
    "UnionMember1Changes",
    "UnionMember1Event",
    "UnionMember1EventUnionMember0",
    "UnionMember1EventUnionMember0Data",
    "UnionMember1EventUnionMember0DataLatest",
    "UnionMember1EventUnionMember0DataLatestAuthor",
    "UnionMember1EventUnionMember0DataLatestAuthorUnionMember0",
    "UnionMember1EventUnionMember0DataLatestAuthorUnionMember1",
    "UnionMember1EventUnionMember0DataReaction",
    "UnionMember1EventUnionMember0DataIdentifiedLanguage",
    "UnionMember1EventUnionMember0Author",
    "UnionMember1EventUnionMember0AuthorUnionMember0",
    "UnionMember1EventUnionMember0AuthorUnionMember0OAuthApp",
    "UnionMember1EventUnionMember0AuthorUnionMember0OAuthAppImageData",
    "UnionMember1EventUnionMember0AuthorUnionMember1",
    "UnionMember1EventUnionMember0AuthorUnionMember1OAuthApp",
    "UnionMember1EventUnionMember0AuthorUnionMember1OAuthAppImageData",
    "UnionMember1EventUnionMember1",
    "UnionMember1EventUnionMember1Data",
    "UnionMember1EventUnionMember1Author",
    "UnionMember1EventUnionMember1AuthorUnionMember0",
    "UnionMember1EventUnionMember1AuthorUnionMember0OAuthApp",
    "UnionMember1EventUnionMember1AuthorUnionMember0OAuthAppImageData",
    "UnionMember1EventUnionMember1AuthorUnionMember1",
    "UnionMember1EventUnionMember1AuthorUnionMember1OAuthApp",
    "UnionMember1EventUnionMember1AuthorUnionMember1OAuthAppImageData",
    "UnionMember1EventUnionMember2",
    "UnionMember1EventUnionMember2Data",
    "UnionMember1EventUnionMember2Author",
    "UnionMember1EventUnionMember2AuthorUnionMember0",
    "UnionMember1EventUnionMember2AuthorUnionMember0OAuthApp",
    "UnionMember1EventUnionMember2AuthorUnionMember0OAuthAppImageData",
    "UnionMember1EventUnionMember2AuthorUnionMember1",
    "UnionMember1EventUnionMember2AuthorUnionMember1OAuthApp",
    "UnionMember1EventUnionMember2AuthorUnionMember1OAuthAppImageData",
    "UnionMember1EventUnionMember3",
    "UnionMember1EventUnionMember3Data",
    "UnionMember1EventUnionMember3Author",
    "UnionMember1EventUnionMember3AuthorUnionMember0",
    "UnionMember1EventUnionMember3AuthorUnionMember0OAuthApp",
    "UnionMember1EventUnionMember3AuthorUnionMember0OAuthAppImageData",
    "UnionMember1EventUnionMember3AuthorUnionMember1",
    "UnionMember1EventUnionMember3AuthorUnionMember1OAuthApp",
    "UnionMember1EventUnionMember3AuthorUnionMember1OAuthAppImageData",
    "UnionMember1EventUnionMember4",
    "UnionMember1EventUnionMember4Data",
    "UnionMember1EventUnionMember4Author",
    "UnionMember1EventUnionMember4AuthorUnionMember0",
    "UnionMember1EventUnionMember4AuthorUnionMember0OAuthApp",
    "UnionMember1EventUnionMember4AuthorUnionMember0OAuthAppImageData",
    "UnionMember1EventUnionMember4AuthorUnionMember1",
    "UnionMember1EventUnionMember4AuthorUnionMember1OAuthApp",
    "UnionMember1EventUnionMember4AuthorUnionMember1OAuthAppImageData",
    "UnionMember1EventUnionMember5",
    "UnionMember1EventUnionMember5Data",
    "UnionMember1EventUnionMember5Author",
    "UnionMember1EventUnionMember5AuthorUnionMember0",
    "UnionMember1EventUnionMember5AuthorUnionMember0OAuthApp",
    "UnionMember1EventUnionMember5AuthorUnionMember0OAuthAppImageData",
    "UnionMember1EventUnionMember5AuthorUnionMember1",
    "UnionMember1EventUnionMember5AuthorUnionMember1OAuthApp",
    "UnionMember1EventUnionMember5AuthorUnionMember1OAuthAppImageData",
    "UnionMember1EventUnionMember6",
    "UnionMember1EventUnionMember6Data",
    "UnionMember1EventUnionMember6Author",
    "UnionMember1EventUnionMember6AuthorUnionMember0",
    "UnionMember1EventUnionMember6AuthorUnionMember0OAuthApp",
    "UnionMember1EventUnionMember6AuthorUnionMember0OAuthAppImageData",
    "UnionMember1EventUnionMember6AuthorUnionMember1",
    "UnionMember1EventUnionMember6AuthorUnionMember1OAuthApp",
    "UnionMember1EventUnionMember6AuthorUnionMember1OAuthAppImageData",
    "UnionMember1Author",
    "UnionMember1AuthorUnionMember0",
    "UnionMember1AuthorUnionMember1",
    "UnionMember1Org",
]


class UnionMember0EventUnionMember0DataLatestAuthorUnionMember0(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class UnionMember0EventUnionMember0DataLatestAuthorUnionMember1(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


UnionMember0EventUnionMember0DataLatestAuthor: TypeAlias = Union[
    UnionMember0EventUnionMember0DataLatestAuthorUnionMember0, UnionMember0EventUnionMember0DataLatestAuthorUnionMember1
]


class UnionMember0EventUnionMember0DataLatest(BaseModel):
    html: str

    raw: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    author: Optional[UnionMember0EventUnionMember0DataLatestAuthor] = None


class UnionMember0EventUnionMember0DataReaction(BaseModel):
    count: float

    reaction: Literal["🔥", "🚀", "👀", "❤️", "🤗", "😎", "➕", "🧠", "👍", "🤝", "😔", "🤯"]

    users: List[str]


class UnionMember0EventUnionMember0DataIdentifiedLanguage(BaseModel):
    language: str

    probability: float


class UnionMember0EventUnionMember0Data(BaseModel):
    edited: bool

    editor_avatar_urls: List[str] = FieldInfo(alias="editorAvatarUrls")

    editors: List[str]

    hidden: bool

    latest: UnionMember0EventUnionMember0DataLatest

    num_edits: float = FieldInfo(alias="numEdits")

    reactions: List[UnionMember0EventUnionMember0DataReaction]

    hidden_by: Optional[str] = FieldInfo(alias="hiddenBy", default=None)

    hidden_reason: Optional[Literal["Spam", "Abuse", "Graphic Content", "Resolved", "Off-Topic"]] = FieldInfo(
        alias="hiddenReason", default=None
    )

    identified_language: Optional[UnionMember0EventUnionMember0DataIdentifiedLanguage] = FieldInfo(
        alias="identifiedLanguage", default=None
    )

    is_report: Optional[bool] = FieldInfo(alias="isReport", default=None)

    parent_comment_id: Optional[str] = FieldInfo(alias="parentCommentId", default=None)

    related_event_id: Optional[str] = FieldInfo(alias="relatedEventId", default=None)


class UnionMember0EventUnionMember0AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember0AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember0AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember0AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember0AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember0EventUnionMember0AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember0AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember0AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember0AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember0AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember0EventUnionMember0Author: TypeAlias = Union[
    UnionMember0EventUnionMember0AuthorUnionMember0, UnionMember0EventUnionMember0AuthorUnionMember1
]


class UnionMember0EventUnionMember0(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember0EventUnionMember0Data

    type: Literal["comment"]

    author: Optional[UnionMember0EventUnionMember0Author] = None


class UnionMember0EventUnionMember1Data(BaseModel):
    status: Literal["draft", "open", "closed", "merged"]

    reason: Optional[str] = None


class UnionMember0EventUnionMember1AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember1AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember1AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember1AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember1AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember0EventUnionMember1AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember1AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember1AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember1AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember1AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember0EventUnionMember1Author: TypeAlias = Union[
    UnionMember0EventUnionMember1AuthorUnionMember0, UnionMember0EventUnionMember1AuthorUnionMember1
]


class UnionMember0EventUnionMember1(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember0EventUnionMember1Data

    type: Literal["status-change"]

    author: Optional[UnionMember0EventUnionMember1Author] = None


class UnionMember0EventUnionMember2Data(BaseModel):
    oid: str

    subject: str


class UnionMember0EventUnionMember2AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember2AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember2AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember2AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember2AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember0EventUnionMember2AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember2AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember2AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember2AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember2AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember0EventUnionMember2Author: TypeAlias = Union[
    UnionMember0EventUnionMember2AuthorUnionMember0, UnionMember0EventUnionMember2AuthorUnionMember1
]


class UnionMember0EventUnionMember2(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember0EventUnionMember2Data

    type: Literal["commit"]

    author: Optional[UnionMember0EventUnionMember2Author] = None


class UnionMember0EventUnionMember3Data(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: str


class UnionMember0EventUnionMember3AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember3AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember3AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember3AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember3AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember0EventUnionMember3AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember3AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember3AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember3AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember3AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember0EventUnionMember3Author: TypeAlias = Union[
    UnionMember0EventUnionMember3AuthorUnionMember0, UnionMember0EventUnionMember3AuthorUnionMember1
]


class UnionMember0EventUnionMember3(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember0EventUnionMember3Data

    type: Literal["title-change"]

    author: Optional[UnionMember0EventUnionMember3Author] = None


class UnionMember0EventUnionMember4Data(BaseModel):
    pinned: bool


class UnionMember0EventUnionMember4AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember4AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember4AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember4AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember4AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember0EventUnionMember4AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember4AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember4AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember4AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember4AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember0EventUnionMember4Author: TypeAlias = Union[
    UnionMember0EventUnionMember4AuthorUnionMember0, UnionMember0EventUnionMember4AuthorUnionMember1
]


class UnionMember0EventUnionMember4(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember0EventUnionMember4Data

    type: Literal["pinning-change"]

    author: Optional[UnionMember0EventUnionMember4Author] = None


class UnionMember0EventUnionMember5Data(BaseModel):
    locked: bool


class UnionMember0EventUnionMember5AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember5AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember5AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember5AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember5AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember0EventUnionMember5AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember5AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember5AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember5AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember5AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember0EventUnionMember5Author: TypeAlias = Union[
    UnionMember0EventUnionMember5AuthorUnionMember0, UnionMember0EventUnionMember5AuthorUnionMember1
]


class UnionMember0EventUnionMember5(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember0EventUnionMember5Data

    type: Literal["locking-change"]

    author: Optional[UnionMember0EventUnionMember5Author] = None


class UnionMember0EventUnionMember6Data(BaseModel):
    report: bool


class UnionMember0EventUnionMember6AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember6AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember6AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember6AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember6AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember0EventUnionMember6AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember0EventUnionMember6AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember0EventUnionMember6AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember0EventUnionMember6AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember0EventUnionMember6AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember0EventUnionMember6Author: TypeAlias = Union[
    UnionMember0EventUnionMember6AuthorUnionMember0, UnionMember0EventUnionMember6AuthorUnionMember1
]


class UnionMember0EventUnionMember6(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember0EventUnionMember6Data

    type: Literal["report-status-change"]

    author: Optional[UnionMember0EventUnionMember6Author] = None


UnionMember0Event: TypeAlias = Union[
    UnionMember0EventUnionMember0,
    UnionMember0EventUnionMember1,
    UnionMember0EventUnionMember2,
    UnionMember0EventUnionMember3,
    UnionMember0EventUnionMember4,
    UnionMember0EventUnionMember5,
    UnionMember0EventUnionMember6,
]


class UnionMember0AuthorUnionMember0(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class UnionMember0AuthorUnionMember1(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


UnionMember0Author: TypeAlias = Union[UnionMember0AuthorUnionMember0, UnionMember0AuthorUnionMember1]


class UnionMember0Org(BaseModel):
    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    name: str

    type: Literal["org"]

    details: Optional[str] = None

    email: Optional[str] = None

    is_enterprise: Optional[bool] = FieldInfo(alias="isEnterprise", default=None)

    plan: Optional[Literal["team", "enterprise", "plus", "academia"]] = None

    requires_sso: Optional[bool] = FieldInfo(alias="requiresSSO", default=None)


class UnionMember0(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    collection: Literal["discussions", "paper_discussions", "social_posts", "canonical_blogs", "community_blogs"]

    events: List[UnionMember0Event]

    is_pull_request: object = FieldInfo(alias="isPullRequest")

    is_report: bool = FieldInfo(alias="isReport")

    locked: bool

    pinned: bool

    status: Literal["draft", "open", "closed", "merged"]

    title: str

    author: Optional[UnionMember0Author] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    diff_url: Optional[str] = FieldInfo(alias="diffUrl", default=None)

    num: Optional[float] = None

    org: Optional[UnionMember0Org] = None

    repo: Optional[RepoID] = None


class UnionMember1Changes(BaseModel):
    base: str

    merge_commit_id: Optional[str] = FieldInfo(alias="mergeCommitId", default=None)


class UnionMember1EventUnionMember0DataLatestAuthorUnionMember0(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class UnionMember1EventUnionMember0DataLatestAuthorUnionMember1(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


UnionMember1EventUnionMember0DataLatestAuthor: TypeAlias = Union[
    UnionMember1EventUnionMember0DataLatestAuthorUnionMember0, UnionMember1EventUnionMember0DataLatestAuthorUnionMember1
]


class UnionMember1EventUnionMember0DataLatest(BaseModel):
    html: str

    raw: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    author: Optional[UnionMember1EventUnionMember0DataLatestAuthor] = None


class UnionMember1EventUnionMember0DataReaction(BaseModel):
    count: float

    reaction: Literal["🔥", "🚀", "👀", "❤️", "🤗", "😎", "➕", "🧠", "👍", "🤝", "😔", "🤯"]

    users: List[str]


class UnionMember1EventUnionMember0DataIdentifiedLanguage(BaseModel):
    language: str

    probability: float


class UnionMember1EventUnionMember0Data(BaseModel):
    edited: bool

    editor_avatar_urls: List[str] = FieldInfo(alias="editorAvatarUrls")

    editors: List[str]

    hidden: bool

    latest: UnionMember1EventUnionMember0DataLatest

    num_edits: float = FieldInfo(alias="numEdits")

    reactions: List[UnionMember1EventUnionMember0DataReaction]

    hidden_by: Optional[str] = FieldInfo(alias="hiddenBy", default=None)

    hidden_reason: Optional[Literal["Spam", "Abuse", "Graphic Content", "Resolved", "Off-Topic"]] = FieldInfo(
        alias="hiddenReason", default=None
    )

    identified_language: Optional[UnionMember1EventUnionMember0DataIdentifiedLanguage] = FieldInfo(
        alias="identifiedLanguage", default=None
    )

    is_report: Optional[bool] = FieldInfo(alias="isReport", default=None)

    parent_comment_id: Optional[str] = FieldInfo(alias="parentCommentId", default=None)

    related_event_id: Optional[str] = FieldInfo(alias="relatedEventId", default=None)


class UnionMember1EventUnionMember0AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember0AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember0AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember0AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember0AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember1EventUnionMember0AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember0AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember0AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember0AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember0AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember1EventUnionMember0Author: TypeAlias = Union[
    UnionMember1EventUnionMember0AuthorUnionMember0, UnionMember1EventUnionMember0AuthorUnionMember1
]


class UnionMember1EventUnionMember0(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember1EventUnionMember0Data

    type: Literal["comment"]

    author: Optional[UnionMember1EventUnionMember0Author] = None


class UnionMember1EventUnionMember1Data(BaseModel):
    status: Literal["draft", "open", "closed", "merged"]

    reason: Optional[str] = None


class UnionMember1EventUnionMember1AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember1AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember1AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember1AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember1AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember1EventUnionMember1AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember1AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember1AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember1AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember1AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember1EventUnionMember1Author: TypeAlias = Union[
    UnionMember1EventUnionMember1AuthorUnionMember0, UnionMember1EventUnionMember1AuthorUnionMember1
]


class UnionMember1EventUnionMember1(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember1EventUnionMember1Data

    type: Literal["status-change"]

    author: Optional[UnionMember1EventUnionMember1Author] = None


class UnionMember1EventUnionMember2Data(BaseModel):
    oid: str

    subject: str


class UnionMember1EventUnionMember2AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember2AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember2AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember2AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember2AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember1EventUnionMember2AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember2AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember2AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember2AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember2AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember1EventUnionMember2Author: TypeAlias = Union[
    UnionMember1EventUnionMember2AuthorUnionMember0, UnionMember1EventUnionMember2AuthorUnionMember1
]


class UnionMember1EventUnionMember2(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember1EventUnionMember2Data

    type: Literal["commit"]

    author: Optional[UnionMember1EventUnionMember2Author] = None


class UnionMember1EventUnionMember3Data(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: str


class UnionMember1EventUnionMember3AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember3AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember3AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember3AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember3AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember1EventUnionMember3AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember3AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember3AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember3AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember3AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember1EventUnionMember3Author: TypeAlias = Union[
    UnionMember1EventUnionMember3AuthorUnionMember0, UnionMember1EventUnionMember3AuthorUnionMember1
]


class UnionMember1EventUnionMember3(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember1EventUnionMember3Data

    type: Literal["title-change"]

    author: Optional[UnionMember1EventUnionMember3Author] = None


class UnionMember1EventUnionMember4Data(BaseModel):
    pinned: bool


class UnionMember1EventUnionMember4AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember4AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember4AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember4AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember4AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember1EventUnionMember4AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember4AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember4AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember4AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember4AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember1EventUnionMember4Author: TypeAlias = Union[
    UnionMember1EventUnionMember4AuthorUnionMember0, UnionMember1EventUnionMember4AuthorUnionMember1
]


class UnionMember1EventUnionMember4(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember1EventUnionMember4Data

    type: Literal["pinning-change"]

    author: Optional[UnionMember1EventUnionMember4Author] = None


class UnionMember1EventUnionMember5Data(BaseModel):
    locked: bool


class UnionMember1EventUnionMember5AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember5AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember5AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember5AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember5AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember1EventUnionMember5AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember5AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember5AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember5AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember5AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember1EventUnionMember5Author: TypeAlias = Union[
    UnionMember1EventUnionMember5AuthorUnionMember0, UnionMember1EventUnionMember5AuthorUnionMember1
]


class UnionMember1EventUnionMember5(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember1EventUnionMember5Data

    type: Literal["locking-change"]

    author: Optional[UnionMember1EventUnionMember5Author] = None


class UnionMember1EventUnionMember6Data(BaseModel):
    report: bool


class UnionMember1EventUnionMember6AuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember6AuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember6AuthorUnionMember0OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember6AuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember6AuthorUnionMember0OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


class UnionMember1EventUnionMember6AuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class UnionMember1EventUnionMember6AuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[UnionMember1EventUnionMember6AuthorUnionMember1OAuthAppImageData] = FieldInfo(
        alias="imageData", default=None
    )

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class UnionMember1EventUnionMember6AuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[UnionMember1EventUnionMember6AuthorUnionMember1OAuthApp] = FieldInfo(
        alias="oauthApp", default=None
    )


UnionMember1EventUnionMember6Author: TypeAlias = Union[
    UnionMember1EventUnionMember6AuthorUnionMember0, UnionMember1EventUnionMember6AuthorUnionMember1
]


class UnionMember1EventUnionMember6(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: UnionMember1EventUnionMember6Data

    type: Literal["report-status-change"]

    author: Optional[UnionMember1EventUnionMember6Author] = None


UnionMember1Event: TypeAlias = Union[
    UnionMember1EventUnionMember0,
    UnionMember1EventUnionMember1,
    UnionMember1EventUnionMember2,
    UnionMember1EventUnionMember3,
    UnionMember1EventUnionMember4,
    UnionMember1EventUnionMember5,
    UnionMember1EventUnionMember6,
]


class UnionMember1AuthorUnionMember0(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


class UnionMember1AuthorUnionMember1(BaseModel):
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

    is_user_following: Optional[bool] = FieldInfo(alias="isUserFollowing", default=None)


UnionMember1Author: TypeAlias = Union[UnionMember1AuthorUnionMember0, UnionMember1AuthorUnionMember1]


class UnionMember1Org(BaseModel):
    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_hf: bool = FieldInfo(alias="isHf")

    name: str

    type: Literal["org"]

    details: Optional[str] = None

    email: Optional[str] = None

    is_enterprise: Optional[bool] = FieldInfo(alias="isEnterprise", default=None)

    plan: Optional[Literal["team", "enterprise", "plus", "academia"]] = None

    requires_sso: Optional[bool] = FieldInfo(alias="requiresSSO", default=None)


class UnionMember1(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    changes: UnionMember1Changes

    collection: Literal["discussions"]

    events: List[UnionMember1Event]

    files_with_conflicts: Union[List[str], Literal[True]] = FieldInfo(alias="filesWithConflicts")
    """The list of files with conflicts.

    `true` means there are conflicts but we cannot list them.
    """

    is_pull_request: Literal[True] = FieldInfo(alias="isPullRequest")

    locked: bool

    pinned: bool

    status: Literal["draft", "open", "closed", "merged"]

    title: str

    author: Optional[UnionMember1Author] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    diff_url: Optional[str] = FieldInfo(alias="diffUrl", default=None)

    num: Optional[float] = None

    org: Optional[UnionMember1Org] = None

    repo: Optional[RepoID] = None


DiscussionRetrieveResponse: TypeAlias = Union[UnionMember0, UnionMember1]
