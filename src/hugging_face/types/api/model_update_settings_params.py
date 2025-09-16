# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ModelUpdateSettingsParams"]


class ModelUpdateSettingsParams(TypedDict, total=False):
    namespace: Required[str]

    discussions_disabled: Annotated[bool, PropertyInfo(alias="discussionsDisabled")]

    gated: Union[Literal["auto", "manual"], object]

    gated_notifications_email: Annotated[str, PropertyInfo(alias="gatedNotificationsEmail")]

    gated_notifications_mode: Annotated[Literal["bulk", "real-time"], PropertyInfo(alias="gatedNotificationsMode")]

    private: bool

    xet_enabled: Annotated[bool, PropertyInfo(alias="xetEnabled")]
