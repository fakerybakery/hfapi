# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import is_given, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.api.resolve_cache_resolve_model_response import ResolveCacheResolveModelResponse
from ...types.api.resolve_cache_resolve_space_response import ResolveCacheResolveSpaceResponse
from ...types.api.resolve_cache_resolve_dataset_response import ResolveCacheResolveDatasetResponse

__all__ = ["ResolveCacheResource", "AsyncResolveCacheResource"]


class ResolveCacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResolveCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return ResolveCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResolveCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return ResolveCacheResourceWithStreamingResponse(self)

    def resolve_dataset(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        accept: Literal["application/vnd.xet-fileinfo+json"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResolveCacheResolveDatasetResponse:
        """
        This endpoint requires to follow redirection

        Args:
          path: Wildcard path parameter

          accept: Returns json information about the XET file info - if the file is a xet file

          range: The range in bytes of the file to download

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Accept": str(accept) if is_given(accept) else NOT_GIVEN,
                    "Range": range,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/api/resolve-cache/datasets/{namespace}/{repo}/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveCacheResolveDatasetResponse,
        )

    def resolve_model(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        accept: Literal["application/vnd.xet-fileinfo+json"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResolveCacheResolveModelResponse:
        """
        This endpoint requires to follow redirection

        Args:
          path: Wildcard path parameter

          accept: Returns json information about the XET file info - if the file is a xet file

          range: The range in bytes of the file to download

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Accept": str(accept) if is_given(accept) else NOT_GIVEN,
                    "Range": range,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/api/resolve-cache/models/{namespace}/{repo}/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveCacheResolveModelResponse,
        )

    def resolve_space(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        accept: Literal["application/vnd.xet-fileinfo+json"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResolveCacheResolveSpaceResponse:
        """
        This endpoint requires to follow redirection

        Args:
          path: Wildcard path parameter

          accept: Returns json information about the XET file info - if the file is a xet file

          range: The range in bytes of the file to download

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Accept": str(accept) if is_given(accept) else NOT_GIVEN,
                    "Range": range,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/api/resolve-cache/spaces/{namespace}/{repo}/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveCacheResolveSpaceResponse,
        )


class AsyncResolveCacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResolveCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncResolveCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResolveCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncResolveCacheResourceWithStreamingResponse(self)

    async def resolve_dataset(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        accept: Literal["application/vnd.xet-fileinfo+json"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResolveCacheResolveDatasetResponse:
        """
        This endpoint requires to follow redirection

        Args:
          path: Wildcard path parameter

          accept: Returns json information about the XET file info - if the file is a xet file

          range: The range in bytes of the file to download

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Accept": str(accept) if is_given(accept) else NOT_GIVEN,
                    "Range": range,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/api/resolve-cache/datasets/{namespace}/{repo}/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveCacheResolveDatasetResponse,
        )

    async def resolve_model(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        accept: Literal["application/vnd.xet-fileinfo+json"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResolveCacheResolveModelResponse:
        """
        This endpoint requires to follow redirection

        Args:
          path: Wildcard path parameter

          accept: Returns json information about the XET file info - if the file is a xet file

          range: The range in bytes of the file to download

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Accept": str(accept) if is_given(accept) else NOT_GIVEN,
                    "Range": range,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/api/resolve-cache/models/{namespace}/{repo}/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveCacheResolveModelResponse,
        )

    async def resolve_space(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        accept: Literal["application/vnd.xet-fileinfo+json"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResolveCacheResolveSpaceResponse:
        """
        This endpoint requires to follow redirection

        Args:
          path: Wildcard path parameter

          accept: Returns json information about the XET file info - if the file is a xet file

          range: The range in bytes of the file to download

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Accept": str(accept) if is_given(accept) else NOT_GIVEN,
                    "Range": range,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/api/resolve-cache/spaces/{namespace}/{repo}/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveCacheResolveSpaceResponse,
        )


class ResolveCacheResourceWithRawResponse:
    def __init__(self, resolve_cache: ResolveCacheResource) -> None:
        self._resolve_cache = resolve_cache

        self.resolve_dataset = to_raw_response_wrapper(
            resolve_cache.resolve_dataset,
        )
        self.resolve_model = to_raw_response_wrapper(
            resolve_cache.resolve_model,
        )
        self.resolve_space = to_raw_response_wrapper(
            resolve_cache.resolve_space,
        )


class AsyncResolveCacheResourceWithRawResponse:
    def __init__(self, resolve_cache: AsyncResolveCacheResource) -> None:
        self._resolve_cache = resolve_cache

        self.resolve_dataset = async_to_raw_response_wrapper(
            resolve_cache.resolve_dataset,
        )
        self.resolve_model = async_to_raw_response_wrapper(
            resolve_cache.resolve_model,
        )
        self.resolve_space = async_to_raw_response_wrapper(
            resolve_cache.resolve_space,
        )


class ResolveCacheResourceWithStreamingResponse:
    def __init__(self, resolve_cache: ResolveCacheResource) -> None:
        self._resolve_cache = resolve_cache

        self.resolve_dataset = to_streamed_response_wrapper(
            resolve_cache.resolve_dataset,
        )
        self.resolve_model = to_streamed_response_wrapper(
            resolve_cache.resolve_model,
        )
        self.resolve_space = to_streamed_response_wrapper(
            resolve_cache.resolve_space,
        )


class AsyncResolveCacheResourceWithStreamingResponse:
    def __init__(self, resolve_cache: AsyncResolveCacheResource) -> None:
        self._resolve_cache = resolve_cache

        self.resolve_dataset = async_to_streamed_response_wrapper(
            resolve_cache.resolve_dataset,
        )
        self.resolve_model = async_to_streamed_response_wrapper(
            resolve_cache.resolve_model,
        )
        self.resolve_space = async_to_streamed_response_wrapper(
            resolve_cache.resolve_space,
        )
