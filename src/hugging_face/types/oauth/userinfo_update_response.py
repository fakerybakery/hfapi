# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserinfoUpdateResponse", "Org", "OrgResourceGroup"]


class OrgResourceGroup(BaseModel):
    name: str

    role: Literal["admin", "write", "contributor", "read"]

    sub: str


class Org(BaseModel):
    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    name: str
    """Name of the organization"""

    picture: str
    """Avatar URL of the organization"""

    preferred_username: str
    """Username of the organization"""

    sub: str
    """ID of the organization"""

    can_pay: Optional[bool] = FieldInfo(alias="canPay", default=None)

    missing_mfa: Optional[bool] = FieldInfo(alias="missingMFA", default=None)

    pending_sso: Optional[bool] = FieldInfo(alias="pendingSSO", default=None)

    resource_groups: Optional[List[OrgResourceGroup]] = FieldInfo(alias="resourceGroups", default=None)

    role_in_org: Optional[Literal["admin", "write", "contributor", "read"]] = FieldInfo(alias="roleInOrg", default=None)

    security_restrictions: Optional[List[Literal["mfa", "token-policy", "sso", "ip"]]] = FieldInfo(
        alias="securityRestrictions", default=None
    )
    """
    Current security restrictions for accessing data in this organization with
    current authentication method
    """


class UserinfoUpdateResponse(BaseModel):
    is_pro: bool = FieldInfo(alias="isPro")
    """Whether the user is a Pro user"""

    orgs: List[Org]

    sub: str
    """ID of the user"""

    can_pay: Optional[bool] = FieldInfo(alias="canPay", default=None)
    """Whether the user has access to billing"""

    email: Optional[str] = None
    """Email of the user"""

    email_verified: Optional[bool] = None
    """Whether the email is verified"""

    name: Optional[str] = None
    """Full name of the user"""

    picture: Optional[str] = None
    """Avatar URL of the user"""

    preferred_username: Optional[str] = None
    """Username of the user"""

    profile: Optional[str] = None
    """Profile URL of the user"""

    website: Optional[str] = None
    """Website of the user"""
