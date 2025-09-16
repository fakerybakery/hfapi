# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.api.datasets import user_access_request_grant_params, user_access_request_handle_params
from ....types.api.datasets.user_access_request_list_response import UserAccessRequestListResponse

__all__ = ["UserAccessRequestResource", "AsyncUserAccessRequestResource"]


class UserAccessRequestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserAccessRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return UserAccessRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserAccessRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return UserAccessRequestResourceWithStreamingResponse(self)

    def list(
        self,
        status: Literal["pending", "accepted", "rejected"],
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAccessRequestListResponse:
        """
        List access requests for a gated repository

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
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return self._get(
            f"/api/datasets/{namespace}/{repo}/user-access-request/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAccessRequestListResponse,
        )

    def cancel(
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
    ) -> None:
        """
        Cancel a the current user's access request to a gated repository

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/datasets/{namespace}/{repo}/user-access-request/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def grant(
        self,
        repo: str,
        *,
        namespace: str,
        user: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Grant access to a user for a gated repository

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/datasets/{namespace}/{repo}/user-access-request/grant",
            body=maybe_transform(
                {
                    "user": user,
                    "user_id": user_id,
                },
                user_access_request_grant_params.UserAccessRequestGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def handle(
        self,
        repo: str,
        *,
        namespace: str,
        status: Literal["accepted", "rejected", "pending"],
        rejection_reason: str | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Handle a user's access request to a gated repository

        Args:
          user: Either userId or user must be provided

          user_id: Either userId or user must be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/datasets/{namespace}/{repo}/user-access-request/handle",
            body=maybe_transform(
                {
                    "status": status,
                    "rejection_reason": rejection_reason,
                    "user": user,
                    "user_id": user_id,
                },
                user_access_request_handle_params.UserAccessRequestHandleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUserAccessRequestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserAccessRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncUserAccessRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserAccessRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncUserAccessRequestResourceWithStreamingResponse(self)

    async def list(
        self,
        status: Literal["pending", "accepted", "rejected"],
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAccessRequestListResponse:
        """
        List access requests for a gated repository

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
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return await self._get(
            f"/api/datasets/{namespace}/{repo}/user-access-request/{status}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAccessRequestListResponse,
        )

    async def cancel(
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
    ) -> None:
        """
        Cancel a the current user's access request to a gated repository

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/datasets/{namespace}/{repo}/user-access-request/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def grant(
        self,
        repo: str,
        *,
        namespace: str,
        user: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Grant access to a user for a gated repository

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/datasets/{namespace}/{repo}/user-access-request/grant",
            body=await async_maybe_transform(
                {
                    "user": user,
                    "user_id": user_id,
                },
                user_access_request_grant_params.UserAccessRequestGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def handle(
        self,
        repo: str,
        *,
        namespace: str,
        status: Literal["accepted", "rejected", "pending"],
        rejection_reason: str | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Handle a user's access request to a gated repository

        Args:
          user: Either userId or user must be provided

          user_id: Either userId or user must be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/datasets/{namespace}/{repo}/user-access-request/handle",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "rejection_reason": rejection_reason,
                    "user": user,
                    "user_id": user_id,
                },
                user_access_request_handle_params.UserAccessRequestHandleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UserAccessRequestResourceWithRawResponse:
    def __init__(self, user_access_request: UserAccessRequestResource) -> None:
        self._user_access_request = user_access_request

        self.list = to_raw_response_wrapper(
            user_access_request.list,
        )
        self.cancel = to_raw_response_wrapper(
            user_access_request.cancel,
        )
        self.grant = to_raw_response_wrapper(
            user_access_request.grant,
        )
        self.handle = to_raw_response_wrapper(
            user_access_request.handle,
        )


class AsyncUserAccessRequestResourceWithRawResponse:
    def __init__(self, user_access_request: AsyncUserAccessRequestResource) -> None:
        self._user_access_request = user_access_request

        self.list = async_to_raw_response_wrapper(
            user_access_request.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            user_access_request.cancel,
        )
        self.grant = async_to_raw_response_wrapper(
            user_access_request.grant,
        )
        self.handle = async_to_raw_response_wrapper(
            user_access_request.handle,
        )


class UserAccessRequestResourceWithStreamingResponse:
    def __init__(self, user_access_request: UserAccessRequestResource) -> None:
        self._user_access_request = user_access_request

        self.list = to_streamed_response_wrapper(
            user_access_request.list,
        )
        self.cancel = to_streamed_response_wrapper(
            user_access_request.cancel,
        )
        self.grant = to_streamed_response_wrapper(
            user_access_request.grant,
        )
        self.handle = to_streamed_response_wrapper(
            user_access_request.handle,
        )


class AsyncUserAccessRequestResourceWithStreamingResponse:
    def __init__(self, user_access_request: AsyncUserAccessRequestResource) -> None:
        self._user_access_request = user_access_request

        self.list = async_to_streamed_response_wrapper(
            user_access_request.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            user_access_request.cancel,
        )
        self.grant = async_to_streamed_response_wrapper(
            user_access_request.grant,
        )
        self.handle = async_to_streamed_response_wrapper(
            user_access_request.handle,
        )
