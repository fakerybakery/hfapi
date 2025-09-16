# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ModelSuperSquashResponse"]


class ModelSuperSquashResponse(BaseModel):
    commit_id: str = FieldInfo(alias="commitId")
    """The new commit ID after the squash"""
