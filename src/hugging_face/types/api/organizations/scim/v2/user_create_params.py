# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ......_types import SequenceNotStr
from ......_utils import PropertyInfo

__all__ = ["UserCreateParams", "Email", "Name"]


class UserCreateParams(TypedDict, total=False):
    emails: Required[Iterable[Email]]

    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]

    body_name: Required[Annotated[Name, PropertyInfo(alias="name")]]

    schemas: Required[SequenceNotStr[str]]

    user_name: Required[Annotated[str, PropertyInfo(alias="userName")]]
    """
    Username for the user, it should respect the hub rules: No consecutive dashes,
    No digit-only, Does not start or end with a dash, Only dashes, letters or
    numbers, Not 24 chars hex string
    """

    active: bool


class Email(TypedDict, total=False):
    value: Required[str]


class Name(TypedDict, total=False):
    family_name: Required[Annotated[str, PropertyInfo(alias="familyName")]]

    given_name: Required[Annotated[str, PropertyInfo(alias="givenName")]]
