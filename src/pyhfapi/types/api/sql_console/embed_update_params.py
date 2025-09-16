# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EmbedUpdateParams"]


class EmbedUpdateParams(TypedDict, total=False):
    repo_type: Required[Annotated[Literal["datasets"], PropertyInfo(alias="repoType")]]

    namespace: Required[str]

    repo: Required[str]

    private: bool

    sql: str

    title: str
