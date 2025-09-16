# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CommentReplyParams"]


class CommentReplyParams(TypedDict, total=False):
    paper_id: Required[Annotated[str, PropertyInfo(alias="paperId")]]

    comment: Required[str]
