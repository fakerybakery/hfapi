# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ModelCommitResponse"]


class ModelCommitResponse(BaseModel):
    commit_oid: str = FieldInfo(alias="commitOid")
    """The OID of the commit"""

    commit_url: str = FieldInfo(alias="commitUrl")
    """The URL of the commit"""

    hook_output: str = FieldInfo(alias="hookOutput")
    """The output of the git hook"""

    success: bool
    """Whether the commit was successful"""

    pull_request_url: Optional[str] = FieldInfo(alias="pullRequestUrl", default=None)
    """The URL of the pull request"""
