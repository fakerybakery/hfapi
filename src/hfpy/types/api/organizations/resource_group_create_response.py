# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ResourceGroupCreateResponse", "Repo", "User", "AutoJoin", "AutoJoinUnionMember0", "AutoJoinEnabled"]


class Repo(BaseModel):
    name: str

    private: bool

    type: Literal["dataset", "model", "space"]

    added_by: Optional[str] = FieldInfo(alias="addedBy", default=None)


class User(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    name: str

    role: Literal["admin", "write", "contributor", "read"]

    type: Literal["user"]

    added_by: Optional[str] = FieldInfo(alias="addedBy", default=None)


class AutoJoinUnionMember0(BaseModel):
    enabled: Literal[True]

    role: Literal["admin", "write", "contributor", "read"]


class AutoJoinEnabled(BaseModel):
    enabled: object


AutoJoin: TypeAlias = Union[AutoJoinUnionMember0, AutoJoinEnabled]


class ResourceGroupCreateResponse(BaseModel):
    id: str

    name: str

    repos: List[Repo]

    users: List[User]

    auto_join: Optional[AutoJoin] = FieldInfo(alias="autoJoin", default=None)

    description: Optional[str] = None
