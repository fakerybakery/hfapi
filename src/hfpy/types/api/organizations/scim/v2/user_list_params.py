# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    count: float

    filter: str
    """
    You can filter results using the equals operator (eq) to find items that match
    specific values like `id`, `userName`, `emails`, and `externalId`. For example,
    to find a user named Bob, use this search: `?filter=userName%20eq%20Bob`
    """

    start_index: Annotated[float, PropertyInfo(alias="startIndex")]
