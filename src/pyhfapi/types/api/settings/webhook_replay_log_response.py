# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["WebhookReplayLogResponse"]


class WebhookReplayLogResponse(BaseModel):
    status: float
    """Replay HTTP status"""
