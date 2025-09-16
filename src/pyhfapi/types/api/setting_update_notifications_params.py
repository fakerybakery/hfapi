# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SettingUpdateNotificationsParams", "Notifications"]


class SettingUpdateNotificationsParams(TypedDict, total=False):
    notifications: Required[Notifications]

    prepaid_amount: Annotated[str, PropertyInfo(alias="prepaidAmount")]
    """To be provided when enabling launch_prepaid_credits"""


class Notifications(TypedDict, total=False):
    announcements: bool

    arxiv_paper_activity: bool

    daily_papers_digest: bool

    discussions_participating: bool

    discussions_watched: bool

    gated_user_access_request: bool

    launch_autonlp: bool

    launch_prepaid_credits: bool

    launch_spaces: bool

    launch_training_cluster: bool

    org_request: bool

    org_suggestions: bool

    org_suggestions_to_create: bool

    org_verified_suggestions: bool

    posts_participating: bool

    product_updates_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    secret_detected: bool

    user_follows: bool

    web_discussions_participating: bool

    web_discussions_watched: bool

    web_posts_participating: bool
