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
from ....types.api.spaces import lfs_file_list_params, lfs_file_delete_params, lfs_file_delete_batch_params
from ....types.api.spaces.lfs_file_list_response import LFSFileListResponse

__all__ = ["LFSFilesResource", "AsyncLFSFilesResource"]


class LFSFilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LFSFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return LFSFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LFSFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return LFSFilesResourceWithStreamingResponse(self)

    def list(
        self,
        repo: str,
        *,
        namespace: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        xet: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LFSFileListResponse:
        """
        List Xet/LFS files for a repo

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
        return self._get(
            f"/api/spaces/{namespace}/{repo}/lfs-files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "xet": xet,
                    },
                    lfs_file_list_params.LFSFileListParams,
                ),
            ),
            cast_to=LFSFileListResponse,
        )

    def delete(
        self,
        sha: str,
        *,
        namespace: str,
        repo: str,
        rewrite_history: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a Xet/LFS file

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
        if not sha:
            raise ValueError(f"Expected a non-empty value for `sha` but received {sha!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/spaces/{namespace}/{repo}/lfs-files/{sha}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"rewrite_history": rewrite_history}, lfs_file_delete_params.LFSFileDeleteParams),
            ),
            cast_to=NoneType,
        )

    def delete_batch(
        self,
        repo: str,
        *,
        namespace: str,
        deletions: lfs_file_delete_batch_params.Deletions,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Xet/LFS files in batch

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
            f"/api/spaces/{namespace}/{repo}/lfs-files/batch",
            body=maybe_transform({"deletions": deletions}, lfs_file_delete_batch_params.LFSFileDeleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLFSFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLFSFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncLFSFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLFSFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncLFSFilesResourceWithStreamingResponse(self)

    async def list(
        self,
        repo: str,
        *,
        namespace: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        xet: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LFSFileListResponse:
        """
        List Xet/LFS files for a repo

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
        return await self._get(
            f"/api/spaces/{namespace}/{repo}/lfs-files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "xet": xet,
                    },
                    lfs_file_list_params.LFSFileListParams,
                ),
            ),
            cast_to=LFSFileListResponse,
        )

    async def delete(
        self,
        sha: str,
        *,
        namespace: str,
        repo: str,
        rewrite_history: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a Xet/LFS file

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
        if not sha:
            raise ValueError(f"Expected a non-empty value for `sha` but received {sha!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/spaces/{namespace}/{repo}/lfs-files/{sha}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"rewrite_history": rewrite_history}, lfs_file_delete_params.LFSFileDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_batch(
        self,
        repo: str,
        *,
        namespace: str,
        deletions: lfs_file_delete_batch_params.Deletions,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Xet/LFS files in batch

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
            f"/api/spaces/{namespace}/{repo}/lfs-files/batch",
            body=await async_maybe_transform(
                {"deletions": deletions}, lfs_file_delete_batch_params.LFSFileDeleteBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LFSFilesResourceWithRawResponse:
    def __init__(self, lfs_files: LFSFilesResource) -> None:
        self._lfs_files = lfs_files

        self.list = to_raw_response_wrapper(
            lfs_files.list,
        )
        self.delete = to_raw_response_wrapper(
            lfs_files.delete,
        )
        self.delete_batch = to_raw_response_wrapper(
            lfs_files.delete_batch,
        )


class AsyncLFSFilesResourceWithRawResponse:
    def __init__(self, lfs_files: AsyncLFSFilesResource) -> None:
        self._lfs_files = lfs_files

        self.list = async_to_raw_response_wrapper(
            lfs_files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lfs_files.delete,
        )
        self.delete_batch = async_to_raw_response_wrapper(
            lfs_files.delete_batch,
        )


class LFSFilesResourceWithStreamingResponse:
    def __init__(self, lfs_files: LFSFilesResource) -> None:
        self._lfs_files = lfs_files

        self.list = to_streamed_response_wrapper(
            lfs_files.list,
        )
        self.delete = to_streamed_response_wrapper(
            lfs_files.delete,
        )
        self.delete_batch = to_streamed_response_wrapper(
            lfs_files.delete_batch,
        )


class AsyncLFSFilesResourceWithStreamingResponse:
    def __init__(self, lfs_files: AsyncLFSFilesResource) -> None:
        self._lfs_files = lfs_files

        self.list = async_to_streamed_response_wrapper(
            lfs_files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lfs_files.delete,
        )
        self.delete_batch = async_to_streamed_response_wrapper(
            lfs_files.delete_batch,
        )
