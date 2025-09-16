# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ......_utils import PropertyInfo

__all__ = [
    "GroupUpdateAttributesParams",
    "Operation",
    "OperationUnionMember0",
    "OperationUnionMember0Value",
    "OperationUnionMember1",
]


class GroupUpdateAttributesParams(TypedDict, total=False):
    name: Required[str]

    operations: Required[Annotated[Iterable[Operation], PropertyInfo(alias="Operations")]]

    schemas: Required[List[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]]]


class OperationUnionMember0Value(TypedDict, total=False):
    value: Required[str]


class OperationUnionMember0(TypedDict, total=False):
    op: Required[str]

    path: Required[str]

    value: Iterable[OperationUnionMember0Value]


class OperationUnionMember1(TypedDict, total=False):
    op: Required[str]

    value: Required[object]

    path: str


Operation: TypeAlias = Union[OperationUnionMember0, OperationUnionMember1]
