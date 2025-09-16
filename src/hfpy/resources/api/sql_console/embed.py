# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

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
from ....types.api.sql_console import embed_create_params, embed_update_params
from ....types.api.sql_console.embed_create_response import EmbedCreateResponse
from ....types.api.sql_console.embed_update_response import EmbedUpdateResponse

__all__ = ["EmbedResource", "AsyncEmbedResource"]


class EmbedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return EmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return EmbedResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        repo_type: Literal["datasets"],
        namespace: str,
        sql: str,
        title: str,
        views: Iterable[embed_create_params.View],
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedCreateResponse:
        """
        Create SQL Console embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/api/{repo_type}/{namespace}/{repo}/sql-console/embed",
            body=maybe_transform(
                {
                    "sql": sql,
                    "title": title,
                    "views": views,
                    "private": private,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        repo_type: Literal["datasets"],
        namespace: str,
        repo: str,
        private: bool | NotGiven = NOT_GIVEN,
        sql: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedUpdateResponse:
        """
        Update SQL Console embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/{repo_type}/{namespace}/{repo}/sql-console/embed/{id}",
            body=maybe_transform(
                {
                    "private": private,
                    "sql": sql,
                    "title": title,
                },
                embed_update_params.EmbedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedUpdateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        repo_type: Literal["datasets"],
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete SQL Console embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/{repo_type}/{namespace}/{repo}/sql-console/embed/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEmbedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncEmbedResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        repo_type: Literal["datasets"],
        namespace: str,
        sql: str,
        title: str,
        views: Iterable[embed_create_params.View],
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedCreateResponse:
        """
        Create SQL Console embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/api/{repo_type}/{namespace}/{repo}/sql-console/embed",
            body=await async_maybe_transform(
                {
                    "sql": sql,
                    "title": title,
                    "views": views,
                    "private": private,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        repo_type: Literal["datasets"],
        namespace: str,
        repo: str,
        private: bool | NotGiven = NOT_GIVEN,
        sql: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbedUpdateResponse:
        """
        Update SQL Console embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/{repo_type}/{namespace}/{repo}/sql-console/embed/{id}",
            body=await async_maybe_transform(
                {
                    "private": private,
                    "sql": sql,
                    "title": title,
                },
                embed_update_params.EmbedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbedUpdateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        repo_type: Literal["datasets"],
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete SQL Console embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/{repo_type}/{namespace}/{repo}/sql-console/embed/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EmbedResourceWithRawResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.create = to_raw_response_wrapper(
            embed.create,
        )
        self.update = to_raw_response_wrapper(
            embed.update,
        )
        self.delete = to_raw_response_wrapper(
            embed.delete,
        )


class AsyncEmbedResourceWithRawResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.create = async_to_raw_response_wrapper(
            embed.create,
        )
        self.update = async_to_raw_response_wrapper(
            embed.update,
        )
        self.delete = async_to_raw_response_wrapper(
            embed.delete,
        )


class EmbedResourceWithStreamingResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.create = to_streamed_response_wrapper(
            embed.create,
        )
        self.update = to_streamed_response_wrapper(
            embed.update,
        )
        self.delete = to_streamed_response_wrapper(
            embed.delete,
        )


class AsyncEmbedResourceWithStreamingResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.create = async_to_streamed_response_wrapper(
            embed.create,
        )
        self.update = async_to_streamed_response_wrapper(
            embed.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            embed.delete,
        )
