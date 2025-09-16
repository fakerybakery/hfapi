# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["GroupUpdateParams", "Member"]


class GroupUpdateParams(TypedDict, total=False):
    name: Required[str]

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]

    members: Required[Iterable[Member]]

    schemas: Required[List[Literal["urn:ietf:params:scim:schemas:core:2.0:Group"]]]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]


class Member(TypedDict, total=False):
    value: Required[str]
