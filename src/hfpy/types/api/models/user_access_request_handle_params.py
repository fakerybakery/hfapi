# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserAccessRequestHandleParams"]


class UserAccessRequestHandleParams(TypedDict, total=False):
    namespace: Required[str]

    status: Required[Literal["accepted", "rejected", "pending"]]

    rejection_reason: Annotated[str, PropertyInfo(alias="rejectionReason")]

    user: str
    """Either userId or user must be provided"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Either userId or user must be provided"""
