# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["JobStartParams"]


class JobStartParams(TypedDict, total=False):
    environment: Required[Dict[str, str]]

    flavor: Required[
        Literal[
            "cpu-basic",
            "cpu-upgrade",
            "cpu-performance",
            "cpu-xl",
            "zero-a10g",
            "t4-small",
            "t4-medium",
            "l4x1",
            "l4x4",
            "l40sx1",
            "l40sx4",
            "l40sx8",
            "a10g-small",
            "a10g-large",
            "a10g-largex2",
            "a10g-largex4",
            "a100-large",
            "h100",
            "h100x8",
            "inf2x6",
        ]
    ]

    arch: Literal["amd64", "arm64"]

    arguments: SequenceNotStr[str]

    command: SequenceNotStr[str]

    docker_image: Annotated[str, PropertyInfo(alias="dockerImage")]

    secrets: Dict[str, str]

    space_id: Annotated[str, PropertyInfo(alias="spaceId")]

    timeout_seconds: Annotated[Optional[int], PropertyInfo(alias="timeoutSeconds")]
