# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import is_given, strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.space_resolve_file_response import SpaceResolveFileResponse

__all__ = ["SpacesResource", "AsyncSpacesResource"]


class SpacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return SpacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return SpacesResourceWithStreamingResponse(self)

    def resolve_file(
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
    ) -> SpaceResolveFileResponse:
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
            f"/spaces/{namespace}/{repo}/resolve/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceResolveFileResponse,
        )


class AsyncSpacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncSpacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncSpacesResourceWithStreamingResponse(self)

    async def resolve_file(
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
    ) -> SpaceResolveFileResponse:
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
            f"/spaces/{namespace}/{repo}/resolve/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceResolveFileResponse,
        )


class SpacesResourceWithRawResponse:
    def __init__(self, spaces: SpacesResource) -> None:
        self._spaces = spaces

        self.resolve_file = to_raw_response_wrapper(
            spaces.resolve_file,
        )


class AsyncSpacesResourceWithRawResponse:
    def __init__(self, spaces: AsyncSpacesResource) -> None:
        self._spaces = spaces

        self.resolve_file = async_to_raw_response_wrapper(
            spaces.resolve_file,
        )


class SpacesResourceWithStreamingResponse:
    def __init__(self, spaces: SpacesResource) -> None:
        self._spaces = spaces

        self.resolve_file = to_streamed_response_wrapper(
            spaces.resolve_file,
        )


class AsyncSpacesResourceWithStreamingResponse:
    def __init__(self, spaces: AsyncSpacesResource) -> None:
        self._spaces = spaces

        self.resolve_file = async_to_streamed_response_wrapper(
            spaces.resolve_file,
        )
