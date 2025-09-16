# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .comment.comment import (
    CommentResource,
    AsyncCommentResource,
    CommentResourceWithRawResponse,
    AsyncCommentResourceWithRawResponse,
    CommentResourceWithStreamingResponse,
    AsyncCommentResourceWithStreamingResponse,
)

__all__ = ["BlogResource", "AsyncBlogResource"]


class BlogResource(SyncAPIResource):
    @cached_property
    def comment(self) -> CommentResource:
        return CommentResource(self._client)

    @cached_property
    def with_raw_response(self) -> BlogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return BlogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return BlogResourceWithStreamingResponse(self)


class AsyncBlogResource(AsyncAPIResource):
    @cached_property
    def comment(self) -> AsyncCommentResource:
        return AsyncCommentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBlogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncBlogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncBlogResourceWithStreamingResponse(self)


class BlogResourceWithRawResponse:
    def __init__(self, blog: BlogResource) -> None:
        self._blog = blog

    @cached_property
    def comment(self) -> CommentResourceWithRawResponse:
        return CommentResourceWithRawResponse(self._blog.comment)


class AsyncBlogResourceWithRawResponse:
    def __init__(self, blog: AsyncBlogResource) -> None:
        self._blog = blog

    @cached_property
    def comment(self) -> AsyncCommentResourceWithRawResponse:
        return AsyncCommentResourceWithRawResponse(self._blog.comment)


class BlogResourceWithStreamingResponse:
    def __init__(self, blog: BlogResource) -> None:
        self._blog = blog

    @cached_property
    def comment(self) -> CommentResourceWithStreamingResponse:
        return CommentResourceWithStreamingResponse(self._blog.comment)


class AsyncBlogResourceWithStreamingResponse:
    def __init__(self, blog: AsyncBlogResource) -> None:
        self._blog = blog

    @cached_property
    def comment(self) -> AsyncCommentResourceWithStreamingResponse:
        return AsyncCommentResourceWithStreamingResponse(self._blog.comment)
