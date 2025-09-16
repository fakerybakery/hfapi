# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["GroupRetrieveParams"]


class GroupRetrieveParams(TypedDict, total=False):
    name: Required[str]

    excluded_attributes: Annotated[Literal["members"], PropertyInfo(alias="excludedAttributes")]
