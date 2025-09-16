# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DatasetUpdateSettingsResponse"]


class DatasetUpdateSettingsResponse(BaseModel):
    discussions_disabled: Optional[bool] = FieldInfo(alias="discussionsDisabled", default=None)

    gated: Union[Literal["auto", "manual"], object, None] = None

    gated_notifications_email: Optional[str] = FieldInfo(alias="gatedNotificationsEmail", default=None)

    gated_notifications_mode: Optional[Literal["bulk", "real-time"]] = FieldInfo(
        alias="gatedNotificationsMode", default=None
    )

    private: Optional[bool] = None

    xet_enabled: Optional[bool] = FieldInfo(alias="xetEnabled", default=None)
