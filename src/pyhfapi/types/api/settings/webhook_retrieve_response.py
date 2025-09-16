# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["WebhookRetrieveResponse", "Webhook", "WebhookWatched", "WebhookJob"]


class WebhookWatched(BaseModel):
    name: str

    type: Literal["dataset", "model", "space", "user", "org"]


class WebhookJob(BaseModel):
    flavor: Literal[
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

    arch: Optional[Literal["amd64", "arm64"]] = None

    arguments: Optional[List[str]] = None

    command: Optional[List[str]] = None

    docker_image: Optional[str] = FieldInfo(alias="dockerImage", default=None)

    environment: Optional[Dict[str, str]] = None

    space_id: Optional[str] = FieldInfo(alias="spaceId", default=None)

    tags: Optional[List[str]] = None

    timeout: Optional[float] = None


class Webhook(BaseModel):
    id: str

    disabled: Union[bool, Literal["suspended-after-failure"]]

    domains: List[Literal["repo", "discussion"]]

    watched: List[WebhookWatched]

    job: Optional[WebhookJob] = None

    secret: Optional[str] = None

    url: Optional[str] = None


class WebhookRetrieveResponse(BaseModel):
    webhook: Webhook
    """Webhook"""
