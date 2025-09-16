# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.organizations import resource_group_create_params
from ....types.api.organizations.repo_id_param import RepoIDParam
from ....types.api.organizations.resource_group_list_response import ResourceGroupListResponse
from ....types.api.organizations.resource_group_create_response import ResourceGroupCreateResponse

__all__ = ["ResourceGroupsResource", "AsyncResourceGroupsResource"]


class ResourceGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return ResourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return ResourceGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        path_name: str,
        *,
        body_name: str,
        auto_join: resource_group_create_params.AutoJoin | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        repos: Iterable[RepoIDParam] | NotGiven = NOT_GIVEN,
        users: Iterable[resource_group_create_params.User] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupCreateResponse:
        """
        Create a new resource group in the organization.

        Requires the org to be Enterprise

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        return self._post(
            f"/api/organizations/{path_name}/resource-groups",
            body=maybe_transform(
                {
                    "body_name": body_name,
                    "auto_join": auto_join,
                    "description": description,
                    "repos": repos,
                    "users": users,
                },
                resource_group_create_params.ResourceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupCreateResponse,
        )

    def list(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupListResponse:
        """
        Get all resource groups the user has access to.

        Requires the org to be Enterprise

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/organizations/{name}/resource-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupListResponse,
        )


class AsyncResourceGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncResourceGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        path_name: str,
        *,
        body_name: str,
        auto_join: resource_group_create_params.AutoJoin | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        repos: Iterable[RepoIDParam] | NotGiven = NOT_GIVEN,
        users: Iterable[resource_group_create_params.User] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupCreateResponse:
        """
        Create a new resource group in the organization.

        Requires the org to be Enterprise

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        return await self._post(
            f"/api/organizations/{path_name}/resource-groups",
            body=await async_maybe_transform(
                {
                    "body_name": body_name,
                    "auto_join": auto_join,
                    "description": description,
                    "repos": repos,
                    "users": users,
                },
                resource_group_create_params.ResourceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupCreateResponse,
        )

    async def list(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupListResponse:
        """
        Get all resource groups the user has access to.

        Requires the org to be Enterprise

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/organizations/{name}/resource-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupListResponse,
        )


class ResourceGroupsResourceWithRawResponse:
    def __init__(self, resource_groups: ResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = to_raw_response_wrapper(
            resource_groups.create,
        )
        self.list = to_raw_response_wrapper(
            resource_groups.list,
        )


class AsyncResourceGroupsResourceWithRawResponse:
    def __init__(self, resource_groups: AsyncResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = async_to_raw_response_wrapper(
            resource_groups.create,
        )
        self.list = async_to_raw_response_wrapper(
            resource_groups.list,
        )


class ResourceGroupsResourceWithStreamingResponse:
    def __init__(self, resource_groups: ResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = to_streamed_response_wrapper(
            resource_groups.create,
        )
        self.list = to_streamed_response_wrapper(
            resource_groups.list,
        )


class AsyncResourceGroupsResourceWithStreamingResponse:
    def __init__(self, resource_groups: AsyncResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = async_to_streamed_response_wrapper(
            resource_groups.create,
        )
        self.list = async_to_streamed_response_wrapper(
            resource_groups.list,
        )
