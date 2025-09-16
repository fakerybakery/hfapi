# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "JobStartResponse",
    "CreatedBy",
    "Owner",
    "Status",
    "Initiator",
    "InitiatorUnionMember0",
    "InitiatorUnionMember1",
]


class CreatedBy(BaseModel):
    id: str

    name: str


class Owner(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    name: str

    type: Literal["user", "org"]


class Status(BaseModel):
    message: Optional[str] = None

    stage: Literal["COMPLETED", "CANCELED", "ERROR", "DELETED", "RUNNING"]


class InitiatorUnionMember0(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    name: str

    type: Literal["user", "org"]


class InitiatorUnionMember1(BaseModel):
    id: str

    type: Literal["scheduled-job"]


Initiator: TypeAlias = Union[InitiatorUnionMember0, InitiatorUnionMember1]


class JobStartResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: CreatedBy = FieldInfo(alias="createdBy")

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

    owner: Owner

    status: Status

    type: Literal["job"]

    arguments: Optional[List[str]] = None

    command: Optional[List[str]] = None

    docker_image: Optional[str] = FieldInfo(alias="dockerImage", default=None)

    initiator: Optional[Initiator] = None

    secrets: Optional[List[str]] = None

    space_id: Optional[str] = FieldInfo(alias="spaceId", default=None)

    timeout: Optional[float] = None
