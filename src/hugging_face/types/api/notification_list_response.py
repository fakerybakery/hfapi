# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .organizations.repo_id import RepoID

__all__ = [
    "NotificationListResponse",
    "Count",
    "Notification",
    "NotificationUnionMember0",
    "NotificationUnionMember0Paper",
    "NotificationUnionMember0PaperDiscussion",
    "NotificationUnionMember0PaperDiscussionParticipating",
    "NotificationUnionMember1",
    "NotificationUnionMember1Discussion",
    "NotificationUnionMember1DiscussionParticipating",
    "NotificationUnionMember2",
    "NotificationUnionMember2Post",
    "NotificationUnionMember2PostParticipating",
    "NotificationUnionMember3",
    "NotificationUnionMember3CanonicalBlog",
    "NotificationUnionMember3CanonicalBlogParticipating",
    "NotificationUnionMember4",
    "NotificationUnionMember4CommunityBlog",
    "NotificationUnionMember4CommunityBlogParticipating",
]


class Count(BaseModel):
    all: float

    unread: float

    view: float


class NotificationUnionMember0Paper(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    title: str


class NotificationUnionMember0PaperDiscussionParticipating(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar: str

    user: str


class NotificationUnionMember0PaperDiscussion(BaseModel):
    id: str

    paper_id: str = FieldInfo(alias="paperId")

    participating: List[NotificationUnionMember0PaperDiscussionParticipating]


class NotificationUnionMember0(BaseModel):
    paper: NotificationUnionMember0Paper

    paper_discussion: NotificationUnionMember0PaperDiscussion = FieldInfo(alias="paperDiscussion")

    read: bool

    type: Literal["paper"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    discussion_event_id: Optional[str] = FieldInfo(alias="discussionEventId", default=None)


class NotificationUnionMember1DiscussionParticipating(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar: str

    user: str


class NotificationUnionMember1Discussion(BaseModel):
    id: str

    is_pull_request: bool = FieldInfo(alias="isPullRequest")

    num: float

    participating: List[NotificationUnionMember1DiscussionParticipating]

    status: Literal["draft", "open", "closed", "merged"]

    title: str


class NotificationUnionMember1(BaseModel):
    discussion: NotificationUnionMember1Discussion

    read: bool

    repo: RepoID

    type: Literal["repo"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    discussion_event_id: Optional[str] = FieldInfo(alias="discussionEventId", default=None)


class NotificationUnionMember2PostParticipating(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar: str

    user: str


class NotificationUnionMember2Post(BaseModel):
    id: str

    author_name: str = FieldInfo(alias="authorName")

    participating: List[NotificationUnionMember2PostParticipating]

    slug: str

    title: str


class NotificationUnionMember2(BaseModel):
    post: NotificationUnionMember2Post

    read: bool

    type: Literal["post"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    discussion_event_id: Optional[str] = FieldInfo(alias="discussionEventId", default=None)


class NotificationUnionMember3CanonicalBlogParticipating(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar: str

    user: str


class NotificationUnionMember3CanonicalBlog(BaseModel):
    id: str

    local: str

    participating: List[NotificationUnionMember3CanonicalBlogParticipating]

    title: str


class NotificationUnionMember3(BaseModel):
    canonical_blog: NotificationUnionMember3CanonicalBlog = FieldInfo(alias="canonicalBlog")

    read: bool

    type: Literal["canonical_blog"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    discussion_event_id: Optional[str] = FieldInfo(alias="discussionEventId", default=None)


class NotificationUnionMember4CommunityBlogParticipating(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar: str

    user: str


class NotificationUnionMember4CommunityBlog(BaseModel):
    id: str

    author_name: str = FieldInfo(alias="authorName")

    participating: List[NotificationUnionMember4CommunityBlogParticipating]

    slug: str

    title: str


class NotificationUnionMember4(BaseModel):
    community_blog: NotificationUnionMember4CommunityBlog = FieldInfo(alias="communityBlog")

    read: bool

    type: Literal["community_blog"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    discussion_event_id: Optional[str] = FieldInfo(alias="discussionEventId", default=None)


Notification: TypeAlias = Union[
    NotificationUnionMember0,
    NotificationUnionMember1,
    NotificationUnionMember2,
    NotificationUnionMember3,
    NotificationUnionMember4,
]


class NotificationListResponse(BaseModel):
    count: Count

    notifications: List[Notification]

    start: float
