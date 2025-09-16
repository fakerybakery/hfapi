# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "APIGetDailyPapersResponse",
    "APIGetDailyPapersResponseItem",
    "APIGetDailyPapersResponseItemPaper",
    "APIGetDailyPapersResponseItemPaperAuthor",
    "APIGetDailyPapersResponseItemPaperAuthorUser",
    "APIGetDailyPapersResponseItemPaperSubmittedOnDailyBy",
    "APIGetDailyPapersResponseItemSubmittedBy",
]


class APIGetDailyPapersResponseItemPaperAuthorUser(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: str

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_hf: Optional[bool] = FieldInfo(alias="isHf", default=None)

    is_hf_admin: Optional[bool] = FieldInfo(alias="isHfAdmin", default=None)

    is_mod: Optional[bool] = FieldInfo(alias="isMod", default=None)

    user: Optional[str] = None


class APIGetDailyPapersResponseItemPaperAuthor(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    hidden: bool

    name: str

    status: Optional[str] = None

    status_last_changed_at: Optional[datetime] = FieldInfo(alias="statusLastChangedAt", default=None)

    user: Optional[APIGetDailyPapersResponseItemPaperAuthorUser] = None
    """User overview information"""


class APIGetDailyPapersResponseItemPaperSubmittedOnDailyBy(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: str

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_hf: Optional[bool] = FieldInfo(alias="isHf", default=None)

    is_hf_admin: Optional[bool] = FieldInfo(alias="isHfAdmin", default=None)

    is_mod: Optional[bool] = FieldInfo(alias="isMod", default=None)

    user: Optional[str] = None


class APIGetDailyPapersResponseItemPaper(BaseModel):
    id: str

    authors: List[APIGetDailyPapersResponseItemPaperAuthor]

    discussion_id: str = FieldInfo(alias="discussionId")

    published_at: datetime = FieldInfo(alias="publishedAt")

    summary: str

    title: str

    upvotes: float

    ai_keywords: Optional[List[str]] = None

    ai_summary: Optional[str] = None

    github_repo: Optional[str] = FieldInfo(alias="githubRepo", default=None)

    github_stars: Optional[float] = FieldInfo(alias="githubStars", default=None)

    media_urls: Optional[List[str]] = FieldInfo(alias="mediaUrls", default=None)

    project_page: Optional[str] = FieldInfo(alias="projectPage", default=None)

    submitted_on_daily_at: Optional[datetime] = FieldInfo(alias="submittedOnDailyAt", default=None)

    submitted_on_daily_by: Optional[APIGetDailyPapersResponseItemPaperSubmittedOnDailyBy] = FieldInfo(
        alias="submittedOnDailyBy", default=None
    )
    """User overview information"""

    withdrawn_at: Optional[datetime] = FieldInfo(alias="withdrawnAt", default=None)


class APIGetDailyPapersResponseItemSubmittedBy(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    type: str

    follower_count: Optional[float] = FieldInfo(alias="followerCount", default=None)

    is_hf: Optional[bool] = FieldInfo(alias="isHf", default=None)

    is_hf_admin: Optional[bool] = FieldInfo(alias="isHfAdmin", default=None)

    is_mod: Optional[bool] = FieldInfo(alias="isMod", default=None)

    user: Optional[str] = None


class APIGetDailyPapersResponseItem(BaseModel):
    is_author_participating: bool = FieldInfo(alias="isAuthorParticipating")

    num_comments: float = FieldInfo(alias="numComments")

    paper: APIGetDailyPapersResponseItemPaper
    """Paper data with metadata"""

    published_at: datetime = FieldInfo(alias="publishedAt")

    submitted_by: APIGetDailyPapersResponseItemSubmittedBy = FieldInfo(alias="submittedBy")
    """User overview information"""

    summary: str

    thumbnail: str

    title: str

    media_urls: Optional[List[str]] = FieldInfo(alias="mediaUrls", default=None)


APIGetDailyPapersResponse: TypeAlias = List[APIGetDailyPapersResponseItem]
