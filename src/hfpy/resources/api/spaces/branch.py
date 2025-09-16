# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ....types.api.spaces import branch_create_params

__all__ = ["BranchResource", "AsyncBranchResource"]


class BranchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BranchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return BranchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BranchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return BranchResourceWithStreamingResponse(self)

    def create(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        empty_branch: bool | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        starting_point: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a new branch

        Args:
          empty_branch: Create an empty branch

          overwrite: Overwrite the branch if it already exists

          starting_point: The commit to start from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/spaces/{namespace}/{repo}/branch/{rev}",
            body=maybe_transform(
                {
                    "empty_branch": empty_branch,
                    "overwrite": overwrite,
                    "starting_point": starting_point,
                },
                branch_create_params.BranchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a branch

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/spaces/{namespace}/{repo}/branch/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBranchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBranchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncBranchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBranchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncBranchResourceWithStreamingResponse(self)

    async def create(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        empty_branch: bool | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        starting_point: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a new branch

        Args:
          empty_branch: Create an empty branch

          overwrite: Overwrite the branch if it already exists

          starting_point: The commit to start from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/spaces/{namespace}/{repo}/branch/{rev}",
            body=await async_maybe_transform(
                {
                    "empty_branch": empty_branch,
                    "overwrite": overwrite,
                    "starting_point": starting_point,
                },
                branch_create_params.BranchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a branch

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/spaces/{namespace}/{repo}/branch/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BranchResourceWithRawResponse:
    def __init__(self, branch: BranchResource) -> None:
        self._branch = branch

        self.create = to_raw_response_wrapper(
            branch.create,
        )
        self.delete = to_raw_response_wrapper(
            branch.delete,
        )


class AsyncBranchResourceWithRawResponse:
    def __init__(self, branch: AsyncBranchResource) -> None:
        self._branch = branch

        self.create = async_to_raw_response_wrapper(
            branch.create,
        )
        self.delete = async_to_raw_response_wrapper(
            branch.delete,
        )


class BranchResourceWithStreamingResponse:
    def __init__(self, branch: BranchResource) -> None:
        self._branch = branch

        self.create = to_streamed_response_wrapper(
            branch.create,
        )
        self.delete = to_streamed_response_wrapper(
            branch.delete,
        )


class AsyncBranchResourceWithStreamingResponse:
    def __init__(self, branch: AsyncBranchResource) -> None:
        self._branch = branch

        self.create = async_to_streamed_response_wrapper(
            branch.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            branch.delete,
        )
