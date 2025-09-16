# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LFSFileDeleteParams"]


class LFSFileDeleteParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    rewrite_history: Annotated[object, PropertyInfo(alias="rewriteHistory")]
