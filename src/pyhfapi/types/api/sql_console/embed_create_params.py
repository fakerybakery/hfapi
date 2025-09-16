# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EmbedCreateParams", "View"]


class EmbedCreateParams(TypedDict, total=False):
    repo_type: Required[Annotated[Literal["datasets"], PropertyInfo(alias="repoType")]]

    namespace: Required[str]

    sql: Required[str]

    title: Required[str]

    views: Required[Iterable[View]]

    private: bool


class View(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]

    key: Required[str]

    view_name: Required[Annotated[str, PropertyInfo(alias="viewName")]]
