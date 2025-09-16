# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    count: float

    excluded_attributes: Annotated[Literal["members"], PropertyInfo(alias="excludedAttributes")]

    filter: str

    start_index: Annotated[float, PropertyInfo(alias="startIndex")]
