# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "APIGetUserInfoResponse",
    "Auth",
    "AuthAccessToken",
    "AuthAccessTokenFineGrained",
    "AuthAccessTokenFineGrainedScoped",
    "AuthAccessTokenFineGrainedScopedEntity",
    "AuthResource",
    "Org",
    "OrgResourceGroup",
]


class AuthAccessTokenFineGrainedScopedEntity(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    type: Literal["dataset", "model", "space", "collection", "org", "user", "resource-group", "oauth-app"]

    name: Optional[str] = None


class AuthAccessTokenFineGrainedScoped(BaseModel):
    entity: AuthAccessTokenFineGrainedScopedEntity

    permissions: List[str]


class AuthAccessTokenFineGrained(BaseModel):
    scoped: List[AuthAccessTokenFineGrainedScoped]

    can_read_gated_repos: Optional[bool] = FieldInfo(alias="canReadGatedRepos", default=None)
    """Allow access to all public gated repos to which the user has access"""

    global_: Optional[List[Literal["discussion.write", "post.write"]]] = FieldInfo(alias="global", default=None)


class AuthAccessToken(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    role: Literal["read", "write", "god", "fineGrained"]

    fine_grained: Optional[AuthAccessTokenFineGrained] = FieldInfo(alias="fineGrained", default=None)


class AuthResource(BaseModel):
    sub: str


class Auth(BaseModel):
    type: str

    access_token: Optional[AuthAccessToken] = FieldInfo(alias="accessToken", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    resource: Optional[AuthResource] = None


class OrgResourceGroup(BaseModel):
    id: str

    name: str

    role: Literal["admin", "write", "contributor", "read"]


class Org(BaseModel):
    id: str

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_enterprise: bool = FieldInfo(alias="isEnterprise")

    name: str

    type: Literal["org"]

    can_pay: Optional[bool] = FieldInfo(alias="canPay", default=None)

    email: Optional[str] = None

    missing_mfa: Optional[bool] = FieldInfo(alias="missingMFA", default=None)

    pending_sso: Optional[bool] = FieldInfo(alias="pendingSSO", default=None)

    period_end: Optional[float] = FieldInfo(alias="periodEnd", default=None)

    resource_groups: Optional[List[OrgResourceGroup]] = FieldInfo(alias="resourceGroups", default=None)

    role_in_org: Optional[Literal["admin", "write", "contributor", "read"]] = FieldInfo(alias="roleInOrg", default=None)

    security_restrictions: Optional[List[Literal["mfa", "token-policy", "sso", "ip"]]] = FieldInfo(
        alias="securityRestrictions", default=None
    )
    """
    Current security restrictions for accessing data in this organization with
    current authentication method
    """


class APIGetUserInfoResponse(BaseModel):
    id: str

    auth: Auth

    avatar_url: str = FieldInfo(alias="avatarUrl")

    fullname: str

    is_pro: bool = FieldInfo(alias="isPro")

    name: str

    orgs: List[Org]

    type: Literal["user"]

    can_pay: Optional[bool] = FieldInfo(alias="canPay", default=None)

    email: Optional[str] = None

    email_verified: Optional[bool] = FieldInfo(alias="emailVerified", default=None)

    period_end: Optional[float] = FieldInfo(alias="periodEnd", default=None)
