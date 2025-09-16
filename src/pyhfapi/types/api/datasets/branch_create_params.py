# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BranchCreateParams"]


class BranchCreateParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    empty_branch: Annotated[bool, PropertyInfo(alias="emptyBranch")]
    """Create an empty branch"""

    overwrite: bool
    """Overwrite the branch if it already exists"""

    starting_point: Annotated[str, PropertyInfo(alias="startingPoint")]
    """The commit to start from"""
