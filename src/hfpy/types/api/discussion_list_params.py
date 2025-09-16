# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DiscussionListParams"]


class DiscussionListParams(TypedDict, total=False):
    repo_type: Required[Annotated[Literal["models", "spaces", "datasets"], PropertyInfo(alias="repoType")]]

    namespace: Required[str]

    author: str

    p: int

    search: str

    sort: Literal["recently-created", "trending", "reactions"]

    status: Literal["all", "open", "closed"]

    type: Literal["all", "discussion", "pull_request"]
