# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ResourceGroupAddParams"]


class ResourceGroupAddParams(TypedDict, total=False):
    namespace: Required[str]

    resource_group_id: Required[Annotated[Optional[str], PropertyInfo(alias="resourceGroupId")]]
    """
    The resource group to add the repository to, if null, the repository will be
    removed from the resource group
    """
