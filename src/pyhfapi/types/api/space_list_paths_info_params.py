# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SpaceListPathsInfoParams"]


class SpaceListPathsInfoParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    expand: Required[Union[bool, object]]
    """Expand the response with the last commit and security file status"""

    paths: Required[Union[SequenceNotStr[str], str]]
