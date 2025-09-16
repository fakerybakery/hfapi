# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserAccessRequestGrantParams"]


class UserAccessRequestGrantParams(TypedDict, total=False):
    namespace: Required[str]

    user: str

    user_id: Annotated[str, PropertyInfo(alias="userId")]
