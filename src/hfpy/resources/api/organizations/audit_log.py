# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.api.organizations import audit_log_export_params
from ....types.api.organizations.audit_log_export_response import AuditLogExportResponse

__all__ = ["AuditLogResource", "AsyncAuditLogResource"]


class AuditLogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AuditLogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AuditLogResourceWithStreamingResponse(self)

    def export(
        self,
        name: str,
        *,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuditLogExportResponse:
        """Export the audit log events in JSON format for a Team or Enterprise
        organization.

        The export is limited to the last 100,000 events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/organizations/{name}/audit-log/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"q": q}, audit_log_export_params.AuditLogExportParams),
            ),
            cast_to=AuditLogExportResponse,
        )


class AsyncAuditLogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncAuditLogResourceWithStreamingResponse(self)

    async def export(
        self,
        name: str,
        *,
        q: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuditLogExportResponse:
        """Export the audit log events in JSON format for a Team or Enterprise
        organization.

        The export is limited to the last 100,000 events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/organizations/{name}/audit-log/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"q": q}, audit_log_export_params.AuditLogExportParams),
            ),
            cast_to=AuditLogExportResponse,
        )


class AuditLogResourceWithRawResponse:
    def __init__(self, audit_log: AuditLogResource) -> None:
        self._audit_log = audit_log

        self.export = to_raw_response_wrapper(
            audit_log.export,
        )


class AsyncAuditLogResourceWithRawResponse:
    def __init__(self, audit_log: AsyncAuditLogResource) -> None:
        self._audit_log = audit_log

        self.export = async_to_raw_response_wrapper(
            audit_log.export,
        )


class AuditLogResourceWithStreamingResponse:
    def __init__(self, audit_log: AuditLogResource) -> None:
        self._audit_log = audit_log

        self.export = to_streamed_response_wrapper(
            audit_log.export,
        )


class AsyncAuditLogResourceWithStreamingResponse:
    def __init__(self, audit_log: AsyncAuditLogResource) -> None:
        self._audit_log = audit_log

        self.export = async_to_streamed_response_wrapper(
            audit_log.export,
        )
