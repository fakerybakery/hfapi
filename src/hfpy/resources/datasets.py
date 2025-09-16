# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import dataset_request_access_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.dataset_resolve_file_response import DatasetResolveFileResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def export_access_report(
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
    ) -> str:
        """
        Export a report of all access requests for a gated repository

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
            f"/datasets/{namespace}/{repo}/user-access-report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def request_access(
        self,
        repo: str,
        *,
        namespace: str,
        body: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The fields requested by repository card metadata
        (https://huggingface.co/docs/hub/en/models-gated#customize-requested-information)

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
            f"/datasets/{namespace}/{repo}/ask-access",
            body=maybe_transform(body, dataset_request_access_params.DatasetRequestAccessParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
    ) -> DatasetResolveFileResponse:
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
            f"/datasets/{namespace}/{repo}/resolve/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetResolveFileResponse,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def export_access_report(
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
    ) -> str:
        """
        Export a report of all access requests for a gated repository

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
            f"/datasets/{namespace}/{repo}/user-access-report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def request_access(
        self,
        repo: str,
        *,
        namespace: str,
        body: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The fields requested by repository card metadata
        (https://huggingface.co/docs/hub/en/models-gated#customize-requested-information)

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
            f"/datasets/{namespace}/{repo}/ask-access",
            body=await async_maybe_transform(body, dataset_request_access_params.DatasetRequestAccessParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
    ) -> DatasetResolveFileResponse:
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
            f"/datasets/{namespace}/{repo}/resolve/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetResolveFileResponse,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.export_access_report = to_raw_response_wrapper(
            datasets.export_access_report,
        )
        self.request_access = to_raw_response_wrapper(
            datasets.request_access,
        )
        self.resolve_file = to_raw_response_wrapper(
            datasets.resolve_file,
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.export_access_report = async_to_raw_response_wrapper(
            datasets.export_access_report,
        )
        self.request_access = async_to_raw_response_wrapper(
            datasets.request_access,
        )
        self.resolve_file = async_to_raw_response_wrapper(
            datasets.resolve_file,
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.export_access_report = to_streamed_response_wrapper(
            datasets.export_access_report,
        )
        self.request_access = to_streamed_response_wrapper(
            datasets.request_access,
        )
        self.resolve_file = to_streamed_response_wrapper(
            datasets.resolve_file,
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.export_access_report = async_to_streamed_response_wrapper(
            datasets.export_access_report,
        )
        self.request_access = async_to_streamed_response_wrapper(
            datasets.request_access,
        )
        self.resolve_file = async_to_streamed_response_wrapper(
            datasets.resolve_file,
        )
