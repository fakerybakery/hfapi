# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .comment import (
    CommentResource,
    AsyncCommentResource,
    CommentResourceWithRawResponse,
    AsyncCommentResourceWithRawResponse,
    CommentResourceWithStreamingResponse,
    AsyncCommentResourceWithStreamingResponse,
)
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
from ....types.api import paper_search_params
from ...._base_client import make_request_options

__all__ = ["PapersResource", "AsyncPapersResource"]


class PapersResource(SyncAPIResource):
    @cached_property
    def comment(self) -> CommentResource:
        return CommentResource(self._client)

    @cached_property
    def with_raw_response(self) -> PapersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return PapersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PapersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return PapersResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Perform a hybrid semantic / full-text-search on papers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/papers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"q": q}, paper_search_params.PaperSearchParams),
            ),
            cast_to=NoneType,
        )


class AsyncPapersResource(AsyncAPIResource):
    @cached_property
    def comment(self) -> AsyncCommentResource:
        return AsyncCommentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPapersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncPapersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPapersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncPapersResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Perform a hybrid semantic / full-text-search on papers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/papers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"q": q}, paper_search_params.PaperSearchParams),
            ),
            cast_to=NoneType,
        )


class PapersResourceWithRawResponse:
    def __init__(self, papers: PapersResource) -> None:
        self._papers = papers

        self.search = to_raw_response_wrapper(
            papers.search,
        )

    @cached_property
    def comment(self) -> CommentResourceWithRawResponse:
        return CommentResourceWithRawResponse(self._papers.comment)


class AsyncPapersResourceWithRawResponse:
    def __init__(self, papers: AsyncPapersResource) -> None:
        self._papers = papers

        self.search = async_to_raw_response_wrapper(
            papers.search,
        )

    @cached_property
    def comment(self) -> AsyncCommentResourceWithRawResponse:
        return AsyncCommentResourceWithRawResponse(self._papers.comment)


class PapersResourceWithStreamingResponse:
    def __init__(self, papers: PapersResource) -> None:
        self._papers = papers

        self.search = to_streamed_response_wrapper(
            papers.search,
        )

    @cached_property
    def comment(self) -> CommentResourceWithStreamingResponse:
        return CommentResourceWithStreamingResponse(self._papers.comment)


class AsyncPapersResourceWithStreamingResponse:
    def __init__(self, papers: AsyncPapersResource) -> None:
        self._papers = papers

        self.search = async_to_streamed_response_wrapper(
            papers.search,
        )

    @cached_property
    def comment(self) -> AsyncCommentResourceWithStreamingResponse:
        return AsyncCommentResourceWithStreamingResponse(self._papers.comment)
