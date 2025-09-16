# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ModelListRefsResponse", "Branch", "Convert", "Tag", "PullRequest"]


class Branch(BaseModel):
    name: str

    ref: str

    target_commit: str = FieldInfo(alias="targetCommit")


class Convert(BaseModel):
    name: str

    ref: str

    target_commit: str = FieldInfo(alias="targetCommit")


class Tag(BaseModel):
    name: str

    ref: str

    target_commit: str = FieldInfo(alias="targetCommit")


class PullRequest(BaseModel):
    name: str

    ref: str

    target_commit: str = FieldInfo(alias="targetCommit")


class ModelListRefsResponse(BaseModel):
    branches: List[Branch]

    converts: List[Convert]

    tags: List[Tag]

    pull_requests: Optional[List[PullRequest]] = FieldInfo(alias="pullRequests", default=None)
