# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "CommentReplyResponse",
    "NewMessage",
    "NewMessageData",
    "NewMessageDataLatest",
    "NewMessageDataLatestAuthor",
    "NewMessageDataLatestAuthorUnionMember0",
    "NewMessageDataLatestAuthorUnionMember1",
    "NewMessageDataReaction",
    "NewMessageDataIdentifiedLanguage",
    "NewMessageAuthor",
    "NewMessageAuthorUnionMember0",
    "NewMessageAuthorUnionMember0OAuthApp",
    "NewMessageAuthorUnionMember0OAuthAppImageData",
    "NewMessageAuthorUnionMember1",
    "NewMessageAuthorUnionMember1OAuthApp",
    "NewMessageAuthorUnionMember1OAuthAppImageData",
]


class NewMessageDataLatestAuthorUnionMember0(BaseModel):
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


class NewMessageDataLatestAuthorUnionMember1(BaseModel):
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


NewMessageDataLatestAuthor: TypeAlias = Union[
    NewMessageDataLatestAuthorUnionMember0, NewMessageDataLatestAuthorUnionMember1
]


class NewMessageDataLatest(BaseModel):
    html: str

    raw: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    author: Optional[NewMessageDataLatestAuthor] = None


class NewMessageDataReaction(BaseModel):
    count: float

    reaction: Literal["🔥", "🚀", "👀", "❤️", "🤗", "😎", "➕", "🧠", "👍", "🤝", "😔", "🤯"]

    users: List[str]


class NewMessageDataIdentifiedLanguage(BaseModel):
    language: str

    probability: float


class NewMessageData(BaseModel):
    edited: bool

    editor_avatar_urls: List[str] = FieldInfo(alias="editorAvatarUrls")

    editors: List[str]

    hidden: bool

    latest: NewMessageDataLatest

    num_edits: float = FieldInfo(alias="numEdits")

    reactions: List[NewMessageDataReaction]

    hidden_by: Optional[str] = FieldInfo(alias="hiddenBy", default=None)

    hidden_reason: Optional[Literal["Spam", "Abuse", "Graphic Content", "Resolved", "Off-Topic"]] = FieldInfo(
        alias="hiddenReason", default=None
    )

    identified_language: Optional[NewMessageDataIdentifiedLanguage] = FieldInfo(
        alias="identifiedLanguage", default=None
    )

    is_report: Optional[bool] = FieldInfo(alias="isReport", default=None)

    parent_comment_id: Optional[str] = FieldInfo(alias="parentCommentId", default=None)

    related_event_id: Optional[str] = FieldInfo(alias="relatedEventId", default=None)


class NewMessageAuthorUnionMember0OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class NewMessageAuthorUnionMember0OAuthApp(BaseModel):
    name: str

    image_data: Optional[NewMessageAuthorUnionMember0OAuthAppImageData] = FieldInfo(alias="imageData", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class NewMessageAuthorUnionMember0(BaseModel):
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

    oauth_app: Optional[NewMessageAuthorUnionMember0OAuthApp] = FieldInfo(alias="oauthApp", default=None)


class NewMessageAuthorUnionMember1OAuthAppImageData(BaseModel):
    color_from: str = FieldInfo(alias="colorFrom")

    color_to: str = FieldInfo(alias="colorTo")

    emoji: str


class NewMessageAuthorUnionMember1OAuthApp(BaseModel):
    name: str

    image_data: Optional[NewMessageAuthorUnionMember1OAuthAppImageData] = FieldInfo(alias="imageData", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class NewMessageAuthorUnionMember1(BaseModel):
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

    oauth_app: Optional[NewMessageAuthorUnionMember1OAuthApp] = FieldInfo(alias="oauthApp", default=None)


NewMessageAuthor: TypeAlias = Union[NewMessageAuthorUnionMember0, NewMessageAuthorUnionMember1]


class NewMessage(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    data: NewMessageData

    type: Literal["comment"]

    author: Optional[NewMessageAuthor] = None


class CommentReplyResponse(BaseModel):
    new_message: NewMessage = FieldInfo(alias="newMessage")
