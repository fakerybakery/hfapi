# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import scheduled_job_create_params
from ..._base_client import make_request_options
from ...types.api.scheduled_job_list_response import ScheduledJobListResponse
from ...types.api.scheduled_job_create_response import ScheduledJobCreateResponse
from ...types.api.scheduled_job_retrieve_response import ScheduledJobRetrieveResponse

__all__ = ["ScheduledJobsResource", "AsyncScheduledJobsResource"]


class ScheduledJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduledJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return ScheduledJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduledJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return ScheduledJobsResourceWithStreamingResponse(self)

    def create(
        self,
        namespace: str,
        *,
        job_spec: scheduled_job_create_params.JobSpec,
        schedule: str,
        concurrency: bool | NotGiven = NOT_GIVEN,
        suspend: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledJobCreateResponse:
        """
        Create a scheduled job

        Args:
          schedule: CRON schedule expression (e.g., '0 9 \\** \\** 1' for 9 AM every Monday).

          concurrency: Whether multiple instances of this job can run concurrently

          suspend: Whether the scheduled job is suspended (paused)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._post(
            f"/api/scheduled-jobs/{namespace}",
            body=maybe_transform(
                {
                    "job_spec": job_spec,
                    "schedule": schedule,
                    "concurrency": concurrency,
                    "suspend": suspend,
                },
                scheduled_job_create_params.ScheduledJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledJobCreateResponse,
        )

    def retrieve(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledJobRetrieveResponse:
        """
        Get a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        return self._get(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledJobRetrieveResponse,
        )

    def list(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledJobListResponse:
        """
        List scheduled jobs for an entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get(
            f"/api/scheduled-jobs/{namespace}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledJobListResponse,
        )

    def delete(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def resume(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resume a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def suspend(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Suspend a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}/suspend",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncScheduledJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduledJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduledJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduledJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncScheduledJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        namespace: str,
        *,
        job_spec: scheduled_job_create_params.JobSpec,
        schedule: str,
        concurrency: bool | NotGiven = NOT_GIVEN,
        suspend: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledJobCreateResponse:
        """
        Create a scheduled job

        Args:
          schedule: CRON schedule expression (e.g., '0 9 \\** \\** 1' for 9 AM every Monday).

          concurrency: Whether multiple instances of this job can run concurrently

          suspend: Whether the scheduled job is suspended (paused)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._post(
            f"/api/scheduled-jobs/{namespace}",
            body=await async_maybe_transform(
                {
                    "job_spec": job_spec,
                    "schedule": schedule,
                    "concurrency": concurrency,
                    "suspend": suspend,
                },
                scheduled_job_create_params.ScheduledJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledJobCreateResponse,
        )

    async def retrieve(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledJobRetrieveResponse:
        """
        Get a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        return await self._get(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledJobRetrieveResponse,
        )

    async def list(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledJobListResponse:
        """
        List scheduled jobs for an entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._get(
            f"/api/scheduled-jobs/{namespace}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledJobListResponse,
        )

    async def delete(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def resume(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resume a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def suspend(
        self,
        scheduled_job_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Suspend a scheduled job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not scheduled_job_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_job_id` but received {scheduled_job_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/scheduled-jobs/{namespace}/{scheduled_job_id}/suspend",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ScheduledJobsResourceWithRawResponse:
    def __init__(self, scheduled_jobs: ScheduledJobsResource) -> None:
        self._scheduled_jobs = scheduled_jobs

        self.create = to_raw_response_wrapper(
            scheduled_jobs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scheduled_jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            scheduled_jobs.list,
        )
        self.delete = to_raw_response_wrapper(
            scheduled_jobs.delete,
        )
        self.resume = to_raw_response_wrapper(
            scheduled_jobs.resume,
        )
        self.suspend = to_raw_response_wrapper(
            scheduled_jobs.suspend,
        )


class AsyncScheduledJobsResourceWithRawResponse:
    def __init__(self, scheduled_jobs: AsyncScheduledJobsResource) -> None:
        self._scheduled_jobs = scheduled_jobs

        self.create = async_to_raw_response_wrapper(
            scheduled_jobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scheduled_jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            scheduled_jobs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scheduled_jobs.delete,
        )
        self.resume = async_to_raw_response_wrapper(
            scheduled_jobs.resume,
        )
        self.suspend = async_to_raw_response_wrapper(
            scheduled_jobs.suspend,
        )


class ScheduledJobsResourceWithStreamingResponse:
    def __init__(self, scheduled_jobs: ScheduledJobsResource) -> None:
        self._scheduled_jobs = scheduled_jobs

        self.create = to_streamed_response_wrapper(
            scheduled_jobs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scheduled_jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            scheduled_jobs.list,
        )
        self.delete = to_streamed_response_wrapper(
            scheduled_jobs.delete,
        )
        self.resume = to_streamed_response_wrapper(
            scheduled_jobs.resume,
        )
        self.suspend = to_streamed_response_wrapper(
            scheduled_jobs.suspend,
        )


class AsyncScheduledJobsResourceWithStreamingResponse:
    def __init__(self, scheduled_jobs: AsyncScheduledJobsResource) -> None:
        self._scheduled_jobs = scheduled_jobs

        self.create = async_to_streamed_response_wrapper(
            scheduled_jobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scheduled_jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            scheduled_jobs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scheduled_jobs.delete,
        )
        self.resume = async_to_streamed_response_wrapper(
            scheduled_jobs.resume,
        )
        self.suspend = async_to_streamed_response_wrapper(
            scheduled_jobs.suspend,
        )
