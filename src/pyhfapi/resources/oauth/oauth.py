# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .userinfo import (
    UserinfoResource,
    AsyncUserinfoResource,
    UserinfoResourceWithRawResponse,
    AsyncUserinfoResourceWithRawResponse,
    UserinfoResourceWithStreamingResponse,
    AsyncUserinfoResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def userinfo(self) -> UserinfoResource:
        return UserinfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def userinfo(self) -> AsyncUserinfoResource:
        return AsyncUserinfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def userinfo(self) -> UserinfoResourceWithRawResponse:
        return UserinfoResourceWithRawResponse(self._oauth.userinfo)


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def userinfo(self) -> AsyncUserinfoResourceWithRawResponse:
        return AsyncUserinfoResourceWithRawResponse(self._oauth.userinfo)


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def userinfo(self) -> UserinfoResourceWithStreamingResponse:
        return UserinfoResourceWithStreamingResponse(self._oauth.userinfo)


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

    @cached_property
    def userinfo(self) -> AsyncUserinfoResourceWithStreamingResponse:
        return AsyncUserinfoResourceWithStreamingResponse(self._oauth.userinfo)
