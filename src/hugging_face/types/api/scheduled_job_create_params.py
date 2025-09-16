# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ScheduledJobCreateParams", "JobSpec"]


class ScheduledJobCreateParams(TypedDict, total=False):
    job_spec: Required[Annotated[JobSpec, PropertyInfo(alias="jobSpec")]]

    schedule: Required[str]
    """CRON schedule expression (e.g., '0 9 \\** \\** 1' for 9 AM every Monday)."""

    concurrency: bool
    """Whether multiple instances of this job can run concurrently"""

    suspend: bool
    """Whether the scheduled job is suspended (paused)"""


class JobSpec(TypedDict, total=False):
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

    command: SequenceNotStr[str]

    docker_image: Annotated[str, PropertyInfo(alias="dockerImage")]

    environment: Dict[str, str]

    secrets: Dict[str, str]

    space_id: Annotated[str, PropertyInfo(alias="spaceId")]

    timeout: Optional[int]
