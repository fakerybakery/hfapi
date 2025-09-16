# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["GroupCreateParams", "Member"]


class GroupCreateParams(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]

    members: Required[Iterable[Member]]
    """Array of SCIM user ids"""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]


class Member(TypedDict, total=False):
    value: Required[str]
