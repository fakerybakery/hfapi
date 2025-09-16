# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["WebhookUpdateParams", "Watched", "Job"]


class WebhookUpdateParams(TypedDict, total=False):
    domains: Required[List[Literal["repo", "discussion"]]]

    watched: Required[Iterable[Watched]]

    job: Job

    secret: str

    url: str


class Watched(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["dataset", "model", "space", "user", "org"]]


class Job(TypedDict, total=False):
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

    environment: Dict[str, str]

    secrets: Dict[str, object]

    space_id: Annotated[str, PropertyInfo(alias="spaceId")]

    tags: SequenceNotStr[str]

    timeout: float
