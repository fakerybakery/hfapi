# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["LFSFileDeleteBatchParams", "Deletions"]


class LFSFileDeleteBatchParams(TypedDict, total=False):
    namespace: Required[str]

    deletions: Required[Deletions]


class Deletions(TypedDict, total=False):
    sha: Required[SequenceNotStr[str]]

    rewrite_history: Annotated[bool, PropertyInfo(alias="rewriteHistory")]
