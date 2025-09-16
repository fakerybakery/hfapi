# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "UsageGetResponse",
    "Period",
    "PeriodCharge",
    "PeriodInvoice",
    "PeriodInvoiceUnionMember0",
    "PeriodInvoiceUnionMember1",
    "Usage",
]


class PeriodCharge(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    amount_cents: float = FieldInfo(alias="amountCents")

    billed_through: Literal["stripe-payment-intent"] = FieldInfo(alias="billedThrough")

    created_at: datetime = FieldInfo(alias="createdAt")

    due_date: datetime = FieldInfo(alias="dueDate")

    payment_intent_id: str = FieldInfo(alias="paymentIntentId")

    payment_intent_status: Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_capture",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ] = FieldInfo(alias="paymentIntentStatus")

    usage_at_charge_time_micro_usd: float = FieldInfo(alias="usageAtChargeTimeMicroUSD")


class PeriodInvoiceUnionMember0(BaseModel):
    id: str

    amount_due_cents: float = FieldInfo(alias="amountDueCents")

    due_date: datetime = FieldInfo(alias="dueDate")

    status: Literal["draft", "open", "paid", "uncollectible", "void", "unpaid"]

    total_cents: float = FieldInfo(alias="totalCents")

    type: Literal["stripe"]

    collection_method: Optional[Literal["charge_automatically", "send_invoice"]] = FieldInfo(
        alias="collectionMethod", default=None
    )


class PeriodInvoiceUnionMember1(BaseModel):
    id: Literal["no-invoice"]

    type: Literal["no-invoice"]


PeriodInvoice: TypeAlias = Union[PeriodInvoiceUnionMember0, PeriodInvoiceUnionMember1]


class Period(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    entity_id: str = FieldInfo(alias="entityId")

    entity_name: str = FieldInfo(alias="entityName")

    entity_type: Literal["user", "org"] = FieldInfo(alias="entityType")

    period_end: datetime = FieldInfo(alias="periodEnd")

    period_start: datetime = FieldInfo(alias="periodStart")

    charges: Optional[List[PeriodCharge]] = None

    invoice: Optional[PeriodInvoice] = None


class Usage(BaseModel):
    active: bool

    entity_id: str = FieldInfo(alias="entityId")

    label: Optional[str] = None

    product: Literal[
        "hf/repository-storage",
        "jobs/cpu-basic/minutes",
        "jobs/cpu-upgrade/minutes",
        "jobs/cpu-performance/minutes",
        "jobs/cpu-xl/minutes",
        "jobs/t4-small/minutes",
        "jobs/t4-medium/minutes",
        "jobs/a10g-small/minutes",
        "jobs/a10g-large/minutes",
        "jobs/a10g-largex2/minutes",
        "jobs/a10g-largex4/minutes",
        "jobs/a100-large/minutes",
        "jobs/h100/minutes",
        "jobs/h100x8/minutes",
        "jobs/l4x1/minutes",
        "jobs/l4x4/minutes",
        "jobs/l40sx1/minutes",
        "jobs/l40sx4/minutes",
        "jobs/l40sx8/minutes",
        "jobs/v5e-2x4/minutes",
        "jobs/v5e-2x2/minutes",
        "jobs/v5e-1x1/minutes",
        "jobs/inf2x6/minutes",
        "spaces/zero-a10g/minutes",
        "spaces/cpu-basic/minutes",
        "spaces/cpu-upgrade/minutes",
        "spaces/cpu-performance/minutes",
        "spaces/cpu-xl/minutes",
        "spaces/t4-small/minutes",
        "spaces/t4-medium/minutes",
        "spaces/a10g-small/minutes",
        "spaces/a10g-large/minutes",
        "spaces/a10g-largex2/minutes",
        "spaces/a10g-largex4/minutes",
        "spaces/a100-large/minutes",
        "spaces/h100/minutes",
        "spaces/h100x8/minutes",
        "spaces/l4x1/minutes",
        "spaces/l4x4/minutes",
        "spaces/l40sx1/minutes",
        "spaces/l40sx4/minutes",
        "spaces/l40sx8/minutes",
        "spaces/inf2x6/minutes",
        "spaces/v5e-2x4/minutes",
        "spaces/v5e-2x2/minutes",
        "spaces/v5e-1x1/minutes",
        "spaces/storage-small/minutes",
        "spaces/storage-medium/minutes",
        "spaces/storage-large/minutes",
        "endpoints/azure/intel-xeon/x1",
        "endpoints/azure/intel-xeon/x2",
        "endpoints/azure/intel-xeon/x4",
        "endpoints/azure/intel-xeon/x8",
        "endpoints/aws/intel-icl/x1",
        "endpoints/aws/intel-icl/x2",
        "endpoints/aws/intel-icl/x4",
        "endpoints/aws/intel-icl/x8",
        "endpoints/aws/intel-spr/x1",
        "endpoints/aws/intel-spr/x2",
        "endpoints/aws/intel-spr/x4",
        "endpoints/aws/intel-spr/x8",
        "endpoints/aws/intel-spr/x16",
        "endpoints/aws/intel-spr-overcommitted/x16",
        "endpoints/aws/nvidia-t4/x1",
        "endpoints/aws/nvidia-t4/x4",
        "endpoints/aws/nvidia-l4/x1",
        "endpoints/aws/nvidia-l4/x4",
        "endpoints/aws/nvidia-l40s/x1",
        "endpoints/aws/nvidia-l40s/x4",
        "endpoints/aws/nvidia-l40s/x8",
        "endpoints/aws/nvidia-a10g/x1",
        "endpoints/aws/nvidia-a10g/x4",
        "endpoints/aws/nvidia-a100/x1",
        "endpoints/aws/nvidia-a100/x2",
        "endpoints/aws/nvidia-a100/x4",
        "endpoints/aws/nvidia-a100/x8",
        "endpoints/aws/nvidia-h200/x1",
        "endpoints/aws/nvidia-h200/x2",
        "endpoints/aws/nvidia-h200/x4",
        "endpoints/aws/nvidia-h200/x8",
        "endpoints/aws/inf2/x1",
        "endpoints/aws/inf2/x12",
        "endpoints/gcp/intel-spr/x1",
        "endpoints/gcp/intel-spr/x2",
        "endpoints/gcp/intel-spr/x4",
        "endpoints/gcp/intel-spr/x8",
        "endpoints/gcp/nvidia-t4/x1",
        "endpoints/gcp/nvidia-l4/x1",
        "endpoints/gcp/nvidia-l4/x4",
        "endpoints/gcp/nvidia-a100/x1",
        "endpoints/gcp/nvidia-a100/x2",
        "endpoints/gcp/nvidia-a100/x4",
        "endpoints/gcp/nvidia-a100/x8",
        "endpoints/gcp/nvidia-h100/x1",
        "endpoints/gcp/nvidia-h100/x2",
        "endpoints/gcp/nvidia-h100/x4",
        "endpoints/gcp/nvidia-h100/x8",
        "endpoints/gcp/v5e/1x1",
        "endpoints/gcp/v5e/2x2",
        "endpoints/gcp/v5e/2x4",
    ]

    product_pretty_name: str = FieldInfo(alias="productPrettyName")

    quantity: float

    total_cost_micro_usd: float = FieldInfo(alias="totalCostMicroUSD")

    unit_cost_micro_usd: float = FieldInfo(alias="unitCostMicroUSD")

    unit_label: Optional[str] = FieldInfo(alias="unitLabel", default=None)

    free_grant: Optional[bool] = FieldInfo(alias="freeGrant", default=None)

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    stopped_at: Optional[datetime] = FieldInfo(alias="stoppedAt", default=None)


class UsageGetResponse(BaseModel):
    period: Period

    usage: Dict[str, List[Usage]]
