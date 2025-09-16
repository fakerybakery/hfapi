# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .embed import (
    EmbedResource,
    AsyncEmbedResource,
    EmbedResourceWithRawResponse,
    AsyncEmbedResourceWithRawResponse,
    EmbedResourceWithStreamingResponse,
    AsyncEmbedResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SqlConsoleResource", "AsyncSqlConsoleResource"]


class SqlConsoleResource(SyncAPIResource):
    @cached_property
    def embed(self) -> EmbedResource:
        return EmbedResource(self._client)

    @cached_property
    def with_raw_response(self) -> SqlConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return SqlConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SqlConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return SqlConsoleResourceWithStreamingResponse(self)


class AsyncSqlConsoleResource(AsyncAPIResource):
    @cached_property
    def embed(self) -> AsyncEmbedResource:
        return AsyncEmbedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSqlConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncSqlConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSqlConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncSqlConsoleResourceWithStreamingResponse(self)


class SqlConsoleResourceWithRawResponse:
    def __init__(self, sql_console: SqlConsoleResource) -> None:
        self._sql_console = sql_console

    @cached_property
    def embed(self) -> EmbedResourceWithRawResponse:
        return EmbedResourceWithRawResponse(self._sql_console.embed)


class AsyncSqlConsoleResourceWithRawResponse:
    def __init__(self, sql_console: AsyncSqlConsoleResource) -> None:
        self._sql_console = sql_console

    @cached_property
    def embed(self) -> AsyncEmbedResourceWithRawResponse:
        return AsyncEmbedResourceWithRawResponse(self._sql_console.embed)


class SqlConsoleResourceWithStreamingResponse:
    def __init__(self, sql_console: SqlConsoleResource) -> None:
        self._sql_console = sql_console

    @cached_property
    def embed(self) -> EmbedResourceWithStreamingResponse:
        return EmbedResourceWithStreamingResponse(self._sql_console.embed)


class AsyncSqlConsoleResourceWithStreamingResponse:
    def __init__(self, sql_console: AsyncSqlConsoleResource) -> None:
        self._sql_console = sql_console

    @cached_property
    def embed(self) -> AsyncEmbedResourceWithStreamingResponse:
        return AsyncEmbedResourceWithStreamingResponse(self._sql_console.embed)
