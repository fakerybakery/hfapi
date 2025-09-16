# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.api.spaces import resource_group_add_params
from ....types.api.spaces.resource_group_add_response import ResourceGroupAddResponse
from ....types.api.spaces.resource_group_get_response import ResourceGroupGetResponse

__all__ = ["ResourceGroupResource", "AsyncResourceGroupResource"]


class ResourceGroupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return ResourceGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return ResourceGroupResourceWithStreamingResponse(self)

    def add(
        self,
        repo: str,
        *,
        namespace: str,
        resource_group_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupAddResponse:
        """
        Add the repository to a resource group

        Args:
          resource_group_id: The resource group to add the repository to, if null, the repository will be
              removed from the resource group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/api/spaces/{namespace}/{repo}/resource-group",
            body=maybe_transform(
                {"resource_group_id": resource_group_id}, resource_group_add_params.ResourceGroupAddParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupAddResponse,
        )

    def get(
        self,
        repo: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupGetResponse:
        """
        Get a resource group of the repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/api/spaces/{namespace}/{repo}/resource-group",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupGetResponse,
        )


class AsyncResourceGroupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncResourceGroupResourceWithStreamingResponse(self)

    async def add(
        self,
        repo: str,
        *,
        namespace: str,
        resource_group_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupAddResponse:
        """
        Add the repository to a resource group

        Args:
          resource_group_id: The resource group to add the repository to, if null, the repository will be
              removed from the resource group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/api/spaces/{namespace}/{repo}/resource-group",
            body=await async_maybe_transform(
                {"resource_group_id": resource_group_id}, resource_group_add_params.ResourceGroupAddParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupAddResponse,
        )

    async def get(
        self,
        repo: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupGetResponse:
        """
        Get a resource group of the repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/api/spaces/{namespace}/{repo}/resource-group",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupGetResponse,
        )


class ResourceGroupResourceWithRawResponse:
    def __init__(self, resource_group: ResourceGroupResource) -> None:
        self._resource_group = resource_group

        self.add = to_raw_response_wrapper(
            resource_group.add,
        )
        self.get = to_raw_response_wrapper(
            resource_group.get,
        )


class AsyncResourceGroupResourceWithRawResponse:
    def __init__(self, resource_group: AsyncResourceGroupResource) -> None:
        self._resource_group = resource_group

        self.add = async_to_raw_response_wrapper(
            resource_group.add,
        )
        self.get = async_to_raw_response_wrapper(
            resource_group.get,
        )


class ResourceGroupResourceWithStreamingResponse:
    def __init__(self, resource_group: ResourceGroupResource) -> None:
        self._resource_group = resource_group

        self.add = to_streamed_response_wrapper(
            resource_group.add,
        )
        self.get = to_streamed_response_wrapper(
            resource_group.get,
        )


class AsyncResourceGroupResourceWithStreamingResponse:
    def __init__(self, resource_group: AsyncResourceGroupResource) -> None:
        self._resource_group = resource_group

        self.add = async_to_streamed_response_wrapper(
            resource_group.add,
        )
        self.get = async_to_streamed_response_wrapper(
            resource_group.get,
        )
