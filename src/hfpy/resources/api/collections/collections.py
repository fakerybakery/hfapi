# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from typing_extensions import Literal

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, SequenceNotStr
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import collection_list_params, collection_create_params, collection_update_params
from ...._base_client import make_request_options
from ....types.api.collection_get_response import CollectionGetResponse
from ....types.api.collection_list_response import CollectionListResponse
from ....types.api.collection_create_response import CollectionCreateResponse
from ....types.api.collection_update_response import CollectionUpdateResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        namespace: str,
        title: str,
        description: str | NotGiven = NOT_GIVEN,
        item: collection_create_params.Item | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionCreateResponse:
        """
        Create a collection

        Args:
          private: If not provided, the collection will be public. This field will respect the
              organization's visibility setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/collections",
            body=maybe_transform(
                {
                    "namespace": namespace,
                    "title": title,
                    "description": description,
                    "item": item,
                    "private": private,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        namespace: str,
        slug: str,
        description: str | NotGiven = NOT_GIVEN,
        gating: collection_update_params.Gating | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        theme: Literal["orange", "blue", "green", "purple", "pink", "indigo"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionUpdateResponse:
        """
        Update a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/collections/{namespace}/{slug}-{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "gating": gating,
                    "position": position,
                    "private": private,
                    "theme": theme,
                    "title": title,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: object | NotGiven = NOT_GIVEN,
        item: Union[SequenceNotStr[str], str] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        owner: Union[SequenceNotStr[str], str] | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        sort: Literal["upvotes", "lastModified", "trending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        Get collections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CollectionListResponse,
            self._get(
                "/api/collections",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "cursor": cursor,
                            "expand": expand,
                            "item": item,
                            "limit": limit,
                            "owner": owner,
                            "q": q,
                            "sort": sort,
                        },
                        collection_list_params.CollectionListParams,
                    ),
                ),
                cast_to=cast(
                    Any, CollectionListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        id: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/collections/{namespace}/{slug}-{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionGetResponse:
        """
        Get a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/collections/{namespace}/{slug}-{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionGetResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        namespace: str,
        title: str,
        description: str | NotGiven = NOT_GIVEN,
        item: collection_create_params.Item | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionCreateResponse:
        """
        Create a collection

        Args:
          private: If not provided, the collection will be public. This field will respect the
              organization's visibility setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/collections",
            body=await async_maybe_transform(
                {
                    "namespace": namespace,
                    "title": title,
                    "description": description,
                    "item": item,
                    "private": private,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        namespace: str,
        slug: str,
        description: str | NotGiven = NOT_GIVEN,
        gating: collection_update_params.Gating | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        theme: Literal["orange", "blue", "green", "purple", "pink", "indigo"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionUpdateResponse:
        """
        Update a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/collections/{namespace}/{slug}-{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "gating": gating,
                    "position": position,
                    "private": private,
                    "theme": theme,
                    "title": title,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: object | NotGiven = NOT_GIVEN,
        item: Union[SequenceNotStr[str], str] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        owner: Union[SequenceNotStr[str], str] | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        sort: Literal["upvotes", "lastModified", "trending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        Get collections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CollectionListResponse,
            await self._get(
                "/api/collections",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "cursor": cursor,
                            "expand": expand,
                            "item": item,
                            "limit": limit,
                            "owner": owner,
                            "q": q,
                            "sort": sort,
                        },
                        collection_list_params.CollectionListParams,
                    ),
                ),
                cast_to=cast(
                    Any, CollectionListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        id: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/collections/{namespace}/{slug}-{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionGetResponse:
        """
        Get a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/collections/{namespace}/{slug}-{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionGetResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )
        self.get = to_raw_response_wrapper(
            collections.get,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._collections.items)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
        self.get = async_to_raw_response_wrapper(
            collections.get,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._collections.items)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )
        self.get = to_streamed_response_wrapper(
            collections.get,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._collections.items)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            collections.get,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._collections.items)
