# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SpaceGetSecurityStatusResponse", "FilesWithIssue"]


class FilesWithIssue(BaseModel):
    level: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    path: str


class SpaceGetSecurityStatusResponse(BaseModel):
    files_with_issues: List[FilesWithIssue] = FieldInfo(alias="filesWithIssues")

    scans_done: bool = FieldInfo(alias="scansDone")
