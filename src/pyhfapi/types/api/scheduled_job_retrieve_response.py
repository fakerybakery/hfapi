# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScheduledJobRetrieveResponse", "JobSpec", "Owner", "Status", "StatusLastJob", "Initiator"]


class JobSpec(BaseModel):
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

    secrets: Optional[List[str]] = None

    space_id: Optional[str] = FieldInfo(alias="spaceId", default=None)

    tags: Optional[List[str]] = None

    timeout: Optional[float] = None


class Owner(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    name: str

    type: Literal["user", "org"]


class StatusLastJob(BaseModel):
    id: str

    at: datetime


class Status(BaseModel):
    last_job: Optional[StatusLastJob] = FieldInfo(alias="lastJob", default=None)

    next_job_run_at: datetime = FieldInfo(alias="nextJobRunAt")


class Initiator(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    name: str

    type: Literal["user", "org"]


class ScheduledJobRetrieveResponse(BaseModel):
    id: str

    concurrency: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    job_spec: JobSpec = FieldInfo(alias="jobSpec")

    owner: Owner

    schedule: str

    status: Status

    suspend: bool

    type: Literal["scheduled-job"]

    initiator: Optional[Initiator] = None
