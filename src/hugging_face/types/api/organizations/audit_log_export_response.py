# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "AuditLogExportResponse",
    "AuditLogExportResponseItem",
    "AuditLogExportResponseItemAuthor",
    "AuditLogExportResponseItemLocation",
]


class AuditLogExportResponseItemAuthor(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    avatar_url: str = FieldInfo(alias="avatarUrl")

    type: Literal["user", "system"]

    user: str

    deleted: Optional[bool] = None


class AuditLogExportResponseItemLocation(BaseModel):
    formatted: str

    city: Optional[str] = None

    country: Optional[str] = None


class AuditLogExportResponseItem(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    author: AuditLogExportResponseItemAuthor

    created_at: datetime = FieldInfo(alias="createdAt")

    message: str

    type: Literal[
        "billing.update_payment_method",
        "billing.create_customer",
        "billing.remove_payment_method",
        "billing.aws_add",
        "billing.aws_remove",
        "billing.gcp_add",
        "billing.gcp_remove",
        "billing.marketplace_approve",
        "billing.cancel_subscription",
        "billing.renew_subscription",
        "billing.start_subscription",
        "billing.un_cancel_subscription",
        "billing.update_subscription",
        "billing.update_subscription_plan",
        "collection.create",
        "collection.delete",
        "org.add_user",
        "org.change_role",
        "org.create",
        "org.delete",
        "org.restore",
        "org.invite_user",
        "org.invite.accept",
        "org.invite.email",
        "org.join.from_domain",
        "org.join.automatic",
        "org.leave",
        "org.remove_user",
        "org.rename",
        "org.rotate_token",
        "org.sso_login",
        "org.sso_join",
        "org.update_join_settings",
        "org.update_settings",
        "org.token_approval.enabled",
        "org.token_approval.disabled",
        "org.token_approval.authorization_request",
        "org.token_approval.authorization_request.authorized",
        "org.token_approval.authorization_request.revoked",
        "org.token_approval.authorization_request.denied",
        "repo.add_secrets",
        "repo.remove_secrets",
        "repo.add_secret",
        "repo.update_secret",
        "repo.remove_secret",
        "repo.create",
        "repo.delete",
        "repo.disable",
        "repo.removeDisable",
        "repo.duplication",
        "repo.delete_doi",
        "repo.move",
        "repo.update_resource_group",
        "repo.update_settings",
        "repo.add_variable",
        "repo.update_variable",
        "repo.remove_variable",
        "repo.add_variables",
        "repo.remove_variables",
        "repo.delete_lfs_file",
        "spaces.add_storage",
        "spaces.remove_storage",
        "spaces.update_hardware",
        "spaces.update_sleep_time",
        "resource_group.create",
        "resource_group.add_users",
        "resource_group.remove_users",
        "resource_group.change_role",
        "resource_group.settings",
        "resource_group.delete",
        "jobs.create",
        "jobs.cancel",
        "scheduled_job.create",
        "scheduled_job.delete",
        "scheduled_job.resume",
        "scheduled_job.suspend",
    ]

    data: Optional[object] = None

    ip: Optional[str] = None

    location: Optional[AuditLogExportResponseItemLocation] = None

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)


AuditLogExportResponse: TypeAlias = List[AuditLogExportResponseItem]
