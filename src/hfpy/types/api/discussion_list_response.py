# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .organizations.repo_id import RepoID

__all__ = [
    "DiscussionListResponse",
    "Discussion",
    "DiscussionTopReaction",
    "DiscussionAuthor",
    "DiscussionAuthorUnionMember0",
    "DiscussionAuthorUnionMember1",
    "DiscussionRepoOwner",
]


class DiscussionTopReaction(BaseModel):
    count: float

    reaction: Literal["🔥", "🚀", "👀", "❤️", "🤗", "😎", "➕", "🧠", "👍", "🤝", "😔", "🤯"]


class DiscussionAuthorUnionMember0(BaseModel):
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


class DiscussionAuthorUnionMember1(BaseModel):
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


DiscussionAuthor: TypeAlias = Union[DiscussionAuthorUnionMember0, DiscussionAuthorUnionMember1]


class DiscussionRepoOwner(BaseModel):
    is_discussion_author: bool = FieldInfo(alias="isDiscussionAuthor")

    is_participating: bool = FieldInfo(alias="isParticipating")

    name: str

    type: Literal["org", "user"]


class Discussion(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    is_pull_request: bool = FieldInfo(alias="isPullRequest")

    num: float

    num_comments: float = FieldInfo(alias="numComments")

    num_reaction_users: float = FieldInfo(alias="numReactionUsers")

    pinned: bool

    repo: RepoID

    status: Literal["draft", "open", "closed", "merged"]

    title: str

    top_reactions: List[DiscussionTopReaction] = FieldInfo(alias="topReactions")

    author: Optional[DiscussionAuthor] = None

    repo_owner: Optional[DiscussionRepoOwner] = FieldInfo(alias="repoOwner", default=None)


class DiscussionListResponse(BaseModel):
    count: float

    discussions: List[Discussion]

    start: float

    num_closed_discussions: Optional[float] = FieldInfo(alias="numClosedDiscussions", default=None)
    """Number of closed discussions on the first page"""
