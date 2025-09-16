# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from .audit_log import (
    AuditLogResource,
    AsyncAuditLogResource,
    AuditLogResourceWithRawResponse,
    AsyncAuditLogResourceWithRawResponse,
    AuditLogResourceWithStreamingResponse,
    AsyncAuditLogResourceWithStreamingResponse,
)
from .scim.scim import (
    ScimResource,
    AsyncScimResource,
    ScimResourceWithRawResponse,
    AsyncScimResourceWithRawResponse,
    ScimResourceWithStreamingResponse,
    AsyncScimResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import organization_list_members_params, organization_retrieve_avatar_params
from ...._base_client import make_request_options
from .billing.billing import (
    BillingResource,
    AsyncBillingResource,
    BillingResourceWithRawResponse,
    AsyncBillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
    AsyncBillingResourceWithStreamingResponse,
)
from .resource_groups import (
    ResourceGroupsResource,
    AsyncResourceGroupsResource,
    ResourceGroupsResourceWithRawResponse,
    AsyncResourceGroupsResourceWithRawResponse,
    ResourceGroupsResourceWithStreamingResponse,
    AsyncResourceGroupsResourceWithStreamingResponse,
)
from ....types.api.organization_list_members_response import OrganizationListMembersResponse
from ....types.api.organization_retrieve_avatar_response import OrganizationRetrieveAvatarResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def audit_log(self) -> AuditLogResource:
        return AuditLogResource(self._client)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResource:
        return ResourceGroupsResource(self._client)

    @cached_property
    def scim(self) -> ScimResource:
        return ScimResource(self._client)

    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def list_members(
        self,
        name: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationListMembersResponse:
        """
        Get a list of members for the organization with optional search and pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/organizations/{name}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "search": search,
                    },
                    organization_list_members_params.OrganizationListMembersParams,
                ),
            ),
            cast_to=OrganizationListMembersResponse,
        )

    def retrieve_avatar(
        self,
        name: str,
        *,
        redirect: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveAvatarResponse:
        """
        This endpoint returns a JSON with the avatar URL for the organization.

        If called with the `Sec-Fetch-Dest: image` header, it instead redirects to the
        avatar URL

        Args:
          redirect: Redirect to the avatar url instead of returning it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/organizations/{name}/avatar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"redirect": redirect}, organization_retrieve_avatar_params.OrganizationRetrieveAvatarParams
                ),
            ),
            cast_to=OrganizationRetrieveAvatarResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def audit_log(self) -> AsyncAuditLogResource:
        return AsyncAuditLogResource(self._client)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResource:
        return AsyncResourceGroupsResource(self._client)

    @cached_property
    def scim(self) -> AsyncScimResource:
        return AsyncScimResource(self._client)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def list_members(
        self,
        name: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationListMembersResponse:
        """
        Get a list of members for the organization with optional search and pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/organizations/{name}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "search": search,
                    },
                    organization_list_members_params.OrganizationListMembersParams,
                ),
            ),
            cast_to=OrganizationListMembersResponse,
        )

    async def retrieve_avatar(
        self,
        name: str,
        *,
        redirect: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveAvatarResponse:
        """
        This endpoint returns a JSON with the avatar URL for the organization.

        If called with the `Sec-Fetch-Dest: image` header, it instead redirects to the
        avatar URL

        Args:
          redirect: Redirect to the avatar url instead of returning it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/organizations/{name}/avatar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"redirect": redirect}, organization_retrieve_avatar_params.OrganizationRetrieveAvatarParams
                ),
            ),
            cast_to=OrganizationRetrieveAvatarResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.list_members = to_raw_response_wrapper(
            organizations.list_members,
        )
        self.retrieve_avatar = to_raw_response_wrapper(
            organizations.retrieve_avatar,
        )

    @cached_property
    def audit_log(self) -> AuditLogResourceWithRawResponse:
        return AuditLogResourceWithRawResponse(self._organizations.audit_log)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResourceWithRawResponse:
        return ResourceGroupsResourceWithRawResponse(self._organizations.resource_groups)

    @cached_property
    def scim(self) -> ScimResourceWithRawResponse:
        return ScimResourceWithRawResponse(self._organizations.scim)

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._organizations.billing)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.list_members = async_to_raw_response_wrapper(
            organizations.list_members,
        )
        self.retrieve_avatar = async_to_raw_response_wrapper(
            organizations.retrieve_avatar,
        )

    @cached_property
    def audit_log(self) -> AsyncAuditLogResourceWithRawResponse:
        return AsyncAuditLogResourceWithRawResponse(self._organizations.audit_log)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResourceWithRawResponse:
        return AsyncResourceGroupsResourceWithRawResponse(self._organizations.resource_groups)

    @cached_property
    def scim(self) -> AsyncScimResourceWithRawResponse:
        return AsyncScimResourceWithRawResponse(self._organizations.scim)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._organizations.billing)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.list_members = to_streamed_response_wrapper(
            organizations.list_members,
        )
        self.retrieve_avatar = to_streamed_response_wrapper(
            organizations.retrieve_avatar,
        )

    @cached_property
    def audit_log(self) -> AuditLogResourceWithStreamingResponse:
        return AuditLogResourceWithStreamingResponse(self._organizations.audit_log)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResourceWithStreamingResponse:
        return ResourceGroupsResourceWithStreamingResponse(self._organizations.resource_groups)

    @cached_property
    def scim(self) -> ScimResourceWithStreamingResponse:
        return ScimResourceWithStreamingResponse(self._organizations.scim)

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._organizations.billing)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.list_members = async_to_streamed_response_wrapper(
            organizations.list_members,
        )
        self.retrieve_avatar = async_to_streamed_response_wrapper(
            organizations.retrieve_avatar,
        )

    @cached_property
    def audit_log(self) -> AsyncAuditLogResourceWithStreamingResponse:
        return AsyncAuditLogResourceWithStreamingResponse(self._organizations.audit_log)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResourceWithStreamingResponse:
        return AsyncResourceGroupsResourceWithStreamingResponse(self._organizations.resource_groups)

    @cached_property
    def scim(self) -> AsyncScimResourceWithStreamingResponse:
        return AsyncScimResourceWithStreamingResponse(self._organizations.scim)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._organizations.billing)
