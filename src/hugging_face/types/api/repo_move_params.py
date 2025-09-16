# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RepoMoveParams"]


class RepoMoveParams(TypedDict, total=False):
    from_repo: Required[Annotated[str, PropertyInfo(alias="fromRepo")]]

    to_repo: Required[Annotated[str, PropertyInfo(alias="toRepo")]]

    type: Literal["dataset", "model", "space"]
