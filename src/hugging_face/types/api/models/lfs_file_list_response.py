# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LFSFileListResponse", "LFSFileListResponseItem", "LFSFileListResponseItemPusher"]


class LFSFileListResponseItemPusher(BaseModel):
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


class LFSFileListResponseItem(BaseModel):
    file_oid: str = FieldInfo(alias="fileOid")

    oid: str

    pushed_at: datetime = FieldInfo(alias="pushedAt")

    size: float

    filename: Optional[str] = None
    """Potential filename of the LFS file"""

    pusher: Optional[LFSFileListResponseItemPusher] = None

    ref: Optional[str] = None

    xet_hash: Optional[str] = FieldInfo(alias="xetHash", default=None)


LFSFileListResponse: TypeAlias = List[LFSFileListResponseItem]
