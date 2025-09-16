# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DiscussionCreateParams"]


class DiscussionCreateParams(TypedDict, total=False):
    repo_type: Required[Annotated[Literal["models", "spaces", "datasets"], PropertyInfo(alias="repoType")]]

    namespace: Required[str]

    description: Required[str]

    title: Required[str]

    pull_request: Annotated[bool, PropertyInfo(alias="pullRequest")]
