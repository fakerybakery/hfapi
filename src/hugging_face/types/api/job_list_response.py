# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "JobListResponse",
    "JobListResponseItem",
    "JobListResponseItemCreatedBy",
    "JobListResponseItemOwner",
    "JobListResponseItemStatus",
    "JobListResponseItemInitiator",
    "JobListResponseItemInitiatorUnionMember0",
    "JobListResponseItemInitiatorUnionMember1",
]


class JobListResponseItemCreatedBy(BaseModel):
    id: str

    name: str


class JobListResponseItemOwner(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    name: str

    type: Literal["user", "org"]


class JobListResponseItemStatus(BaseModel):
    message: Optional[str] = None

    stage: Literal["COMPLETED", "CANCELED", "ERROR", "DELETED", "RUNNING"]


class JobListResponseItemInitiatorUnionMember0(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    name: str

    type: Literal["user", "org"]


class JobListResponseItemInitiatorUnionMember1(BaseModel):
    id: str

    type: Literal["scheduled-job"]


JobListResponseItemInitiator: TypeAlias = Union[
    JobListResponseItemInitiatorUnionMember0, JobListResponseItemInitiatorUnionMember1
]


class JobListResponseItem(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: JobListResponseItemCreatedBy = FieldInfo(alias="createdBy")

    environment: Dict[str, str]

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

    owner: JobListResponseItemOwner

    status: JobListResponseItemStatus

    type: Literal["job"]

    arguments: Optional[List[str]] = None

    command: Optional[List[str]] = None

    docker_image: Optional[str] = FieldInfo(alias="dockerImage", default=None)

    initiator: Optional[JobListResponseItemInitiator] = None

    secrets: Optional[List[str]] = None

    space_id: Optional[str] = FieldInfo(alias="spaceId", default=None)

    timeout: Optional[float] = None


JobListResponse: TypeAlias = List[JobListResponseItem]
