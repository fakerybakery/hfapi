# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["NotificationDeleteParams"]


class NotificationDeleteParams(TypedDict, total=False):
    apply_to_all: Annotated[object, PropertyInfo(alias="applyToAll")]

    article_id: Annotated[str, PropertyInfo(alias="articleId")]

    last_update: Annotated[Union[str, datetime], PropertyInfo(alias="lastUpdate", format="iso8601")]

    mention: Literal["all", "participating", "mentions"]

    p: int

    paper_id: Annotated[str, PropertyInfo(alias="paperId")]

    post_author: Annotated[str, PropertyInfo(alias="postAuthor")]

    read_status: Annotated[Literal["all", "unread"], PropertyInfo(alias="readStatus")]

    repo_name: Annotated[str, PropertyInfo(alias="repoName")]

    repo_type: Annotated[Literal["dataset", "model", "space"], PropertyInfo(alias="repoType")]

    discussion_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="discussionIds")]
