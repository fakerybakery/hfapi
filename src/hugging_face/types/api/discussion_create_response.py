# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DiscussionCreateResponse", "References"]


class References(BaseModel):
    base: str

    merge_commit_id: Optional[str] = FieldInfo(alias="mergeCommitId", default=None)


class DiscussionCreateResponse(BaseModel):
    num: float

    pull_request: bool = FieldInfo(alias="pullRequest")

    url: str

    references: Optional[References] = None
