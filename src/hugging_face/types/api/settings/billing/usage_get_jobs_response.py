# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["UsageGetJobsResponse", "Usage", "UsageJobDetail"]


class UsageJobDetail(BaseModel):
    hardware_flavor: str = FieldInfo(alias="hardwareFlavor")

    job_id: str = FieldInfo(alias="jobId")

    started_at: datetime = FieldInfo(alias="startedAt")

    total_cost_micro_usd: float = FieldInfo(alias="totalCostMicroUsd")

    total_minutes: float = FieldInfo(alias="totalMinutes")

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)


class Usage(BaseModel):
    job_details: List[UsageJobDetail] = FieldInfo(alias="jobDetails")

    period_end: datetime = FieldInfo(alias="periodEnd")

    period_start: datetime = FieldInfo(alias="periodStart")

    total_minutes: float = FieldInfo(alias="totalMinutes")

    used_micro_usd: float = FieldInfo(alias="usedMicroUsd")


class UsageGetJobsResponse(BaseModel):
    has_access: bool = FieldInfo(alias="hasAccess")

    usage: Usage
