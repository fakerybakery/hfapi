# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["UserUpdateAttributesParams", "Operation"]


class UserUpdateAttributesParams(TypedDict, total=False):
    name: Required[str]

    operations: Required[Annotated[Iterable[Operation], PropertyInfo(alias="Operations")]]

    schemas: Required[List[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]]]


class Operation(TypedDict, total=False):
    op: Required[str]

    value: Required[object]

    path: Literal[
        "active", "externalId", "userName", 'emails[type eq "work"].value', "name.givenName", "name.familyName"
    ]
