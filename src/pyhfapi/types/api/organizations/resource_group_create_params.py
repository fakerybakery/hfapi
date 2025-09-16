# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo
from .repo_id_param import RepoIDParam

__all__ = ["ResourceGroupCreateParams", "AutoJoin", "AutoJoinUnionMember0", "AutoJoinEnabled", "User"]


class ResourceGroupCreateParams(TypedDict, total=False):
    body_name: Required[Annotated[str, PropertyInfo(alias="name")]]

    auto_join: Annotated[AutoJoin, PropertyInfo(alias="autoJoin")]

    description: str

    repos: Iterable[RepoIDParam]

    users: Iterable[User]


class AutoJoinUnionMember0(TypedDict, total=False):
    enabled: Required[Literal[True]]

    role: Required[Literal["admin", "write", "contributor", "read"]]


class AutoJoinEnabled(TypedDict, total=False):
    enabled: Required[object]


AutoJoin: TypeAlias = Union[AutoJoinUnionMember0, AutoJoinEnabled]


class User(TypedDict, total=False):
    role: Required[Literal["admin", "write", "contributor", "read"]]

    user: Required[str]
