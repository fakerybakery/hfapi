# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ... import _resource
from .docs import (
    DocsResource,
    AsyncDocsResource,
    DocsResourceWithRawResponse,
    AsyncDocsResourceWithRawResponse,
    DocsResourceWithStreamingResponse,
    AsyncDocsResourceWithStreamingResponse,
)
from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .repos import (
    ReposResource,
    AsyncReposResource,
    ReposResourceWithRawResponse,
    AsyncReposResourceWithRawResponse,
    ReposResourceWithStreamingResponse,
    AsyncReposResourceWithStreamingResponse,
)
from ...types import api_get_model_tags_params, api_get_daily_papers_params, api_get_dataset_tags_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .blog.blog import (
    BlogResource,
    AsyncBlogResource,
    BlogResourceWithRawResponse,
    AsyncBlogResourceWithRawResponse,
    BlogResourceWithStreamingResponse,
    AsyncBlogResourceWithStreamingResponse,
)
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .discussions import (
    DiscussionsResource,
    AsyncDiscussionsResource,
    DiscussionsResourceWithRawResponse,
    AsyncDiscussionsResourceWithRawResponse,
    DiscussionsResourceWithStreamingResponse,
    AsyncDiscussionsResourceWithStreamingResponse,
)
from .posts.posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .models.models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from .notifications import (
    NotificationsResource,
    AsyncNotificationsResource,
    NotificationsResourceWithRawResponse,
    AsyncNotificationsResourceWithRawResponse,
    NotificationsResourceWithStreamingResponse,
    AsyncNotificationsResourceWithStreamingResponse,
)
from .papers.papers import (
    PapersResource,
    AsyncPapersResource,
    PapersResourceWithRawResponse,
    AsyncPapersResourceWithRawResponse,
    PapersResourceWithStreamingResponse,
    AsyncPapersResourceWithStreamingResponse,
)
from .resolve_cache import (
    ResolveCacheResource,
    AsyncResolveCacheResource,
    ResolveCacheResourceWithRawResponse,
    AsyncResolveCacheResourceWithRawResponse,
    ResolveCacheResourceWithStreamingResponse,
    AsyncResolveCacheResourceWithStreamingResponse,
)
from .spaces.spaces import (
    SpacesResource,
    AsyncSpacesResource,
    SpacesResourceWithRawResponse,
    AsyncSpacesResourceWithRawResponse,
    SpacesResourceWithStreamingResponse,
    AsyncSpacesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .scheduled_jobs import (
    ScheduledJobsResource,
    AsyncScheduledJobsResource,
    ScheduledJobsResourceWithRawResponse,
    AsyncScheduledJobsResourceWithRawResponse,
    ScheduledJobsResourceWithStreamingResponse,
    AsyncScheduledJobsResourceWithStreamingResponse,
)
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .settings.settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .collections.collections import (
    CollectionsResource,
    AsyncCollectionsResource,
    CollectionsResourceWithRawResponse,
    AsyncCollectionsResourceWithRawResponse,
    CollectionsResourceWithStreamingResponse,
    AsyncCollectionsResourceWithStreamingResponse,
)
from .sql_console.sql_console import (
    SqlConsoleResource,
    AsyncSqlConsoleResource,
    SqlConsoleResourceWithRawResponse,
    AsyncSqlConsoleResourceWithRawResponse,
    SqlConsoleResourceWithStreamingResponse,
    AsyncSqlConsoleResourceWithStreamingResponse,
)
from .organizations.organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from ...types.api_get_user_info_response import APIGetUserInfoResponse
from ...types.api_get_model_tags_response import APIGetModelTagsResponse
from ...types.api_get_daily_papers_response import APIGetDailyPapersResponse
from ...types.api_get_dataset_tags_response import APIGetDatasetTagsResponse

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(_resource.SyncAPIResource):
    @cached_property
    def notifications(self) -> NotificationsResource:
        return NotificationsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def blog(self) -> BlogResource:
        return BlogResource(self._client)

    @cached_property
    def docs(self) -> DocsResource:
        return DocsResource(self._client)

    @cached_property
    def discussions(self) -> DiscussionsResource:
        return DiscussionsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def spaces(self) -> SpacesResource:
        return SpacesResource(self._client)

    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def sql_console(self) -> SqlConsoleResource:
        return SqlConsoleResource(self._client)

    @cached_property
    def resolve_cache(self) -> ResolveCacheResource:
        return ResolveCacheResource(self._client)

    @cached_property
    def papers(self) -> PapersResource:
        return PapersResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def collections(self) -> CollectionsResource:
        return CollectionsResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def scheduled_jobs(self) -> ScheduledJobsResource:
        return ScheduledJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)

    def get_daily_papers(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        sort: Literal["publishedAt", "trending"] | NotGiven = NOT_GIVEN,
        submitter: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetDailyPapersResponse:
        """
        Get Daily Papers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/daily_papers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "p": p,
                        "sort": sort,
                        "submitter": submitter,
                    },
                    api_get_daily_papers_params.APIGetDailyPapersParams,
                ),
            ),
            cast_to=APIGetDailyPapersResponse,
        )

    def get_dataset_tags(
        self,
        *,
        type: Literal[
            "task_categories",
            "size_categories",
            "modality",
            "format",
            "library",
            "language",
            "license",
            "arxiv",
            "doi",
            "region",
            "other",
            "task_ids",
            "annotations_creators",
            "language_creators",
            "multilinguality",
            "source_datasets",
            "benchmark",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetDatasetTagsResponse:
        """Get all possible tags used for datasets, grouped by tag type.

        Optionally
        restrict to only one tag type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/datasets-tags-by-type",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, api_get_dataset_tags_params.APIGetDatasetTagsParams),
            ),
            cast_to=APIGetDatasetTagsResponse,
        )

    def get_model_tags(
        self,
        *,
        type: Literal["pipeline_tag", "library", "dataset", "language", "license", "arxiv", "doi", "region", "other"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetModelTagsResponse:
        """Get all possible tags used for models, grouped by tag type.

        Optionally restrict
        to only one tag type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/models-tags-by-type",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, api_get_model_tags_params.APIGetModelTagsParams),
            ),
            cast_to=APIGetModelTagsResponse,
        )

    def get_user_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetUserInfoResponse:
        """Get information about the user and auth method use"""
        return self._get(
            "/api/whoami-v2",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIGetUserInfoResponse,
        )


class AsyncAPIResource(_resource.AsyncAPIResource):
    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        return AsyncNotificationsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def blog(self) -> AsyncBlogResource:
        return AsyncBlogResource(self._client)

    @cached_property
    def docs(self) -> AsyncDocsResource:
        return AsyncDocsResource(self._client)

    @cached_property
    def discussions(self) -> AsyncDiscussionsResource:
        return AsyncDiscussionsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def spaces(self) -> AsyncSpacesResource:
        return AsyncSpacesResource(self._client)

    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def sql_console(self) -> AsyncSqlConsoleResource:
        return AsyncSqlConsoleResource(self._client)

    @cached_property
    def resolve_cache(self) -> AsyncResolveCacheResource:
        return AsyncResolveCacheResource(self._client)

    @cached_property
    def papers(self) -> AsyncPapersResource:
        return AsyncPapersResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        return AsyncCollectionsResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def scheduled_jobs(self) -> AsyncScheduledJobsResource:
        return AsyncScheduledJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)

    async def get_daily_papers(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        sort: Literal["publishedAt", "trending"] | NotGiven = NOT_GIVEN,
        submitter: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetDailyPapersResponse:
        """
        Get Daily Papers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/daily_papers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "p": p,
                        "sort": sort,
                        "submitter": submitter,
                    },
                    api_get_daily_papers_params.APIGetDailyPapersParams,
                ),
            ),
            cast_to=APIGetDailyPapersResponse,
        )

    async def get_dataset_tags(
        self,
        *,
        type: Literal[
            "task_categories",
            "size_categories",
            "modality",
            "format",
            "library",
            "language",
            "license",
            "arxiv",
            "doi",
            "region",
            "other",
            "task_ids",
            "annotations_creators",
            "language_creators",
            "multilinguality",
            "source_datasets",
            "benchmark",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetDatasetTagsResponse:
        """Get all possible tags used for datasets, grouped by tag type.

        Optionally
        restrict to only one tag type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/datasets-tags-by-type",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, api_get_dataset_tags_params.APIGetDatasetTagsParams),
            ),
            cast_to=APIGetDatasetTagsResponse,
        )

    async def get_model_tags(
        self,
        *,
        type: Literal["pipeline_tag", "library", "dataset", "language", "license", "arxiv", "doi", "region", "other"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetModelTagsResponse:
        """Get all possible tags used for models, grouped by tag type.

        Optionally restrict
        to only one tag type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/models-tags-by-type",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, api_get_model_tags_params.APIGetModelTagsParams),
            ),
            cast_to=APIGetModelTagsResponse,
        )

    async def get_user_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIGetUserInfoResponse:
        """Get information about the user and auth method use"""
        return await self._get(
            "/api/whoami-v2",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIGetUserInfoResponse,
        )


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.get_daily_papers = to_raw_response_wrapper(
            api.get_daily_papers,
        )
        self.get_dataset_tags = to_raw_response_wrapper(
            api.get_dataset_tags,
        )
        self.get_model_tags = to_raw_response_wrapper(
            api.get_model_tags,
        )
        self.get_user_info = to_raw_response_wrapper(
            api.get_user_info,
        )

    @cached_property
    def notifications(self) -> NotificationsResourceWithRawResponse:
        return NotificationsResourceWithRawResponse(self._api.notifications)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._api.settings)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._api.organizations)

    @cached_property
    def blog(self) -> BlogResourceWithRawResponse:
        return BlogResourceWithRawResponse(self._api.blog)

    @cached_property
    def docs(self) -> DocsResourceWithRawResponse:
        return DocsResourceWithRawResponse(self._api.docs)

    @cached_property
    def discussions(self) -> DiscussionsResourceWithRawResponse:
        return DiscussionsResourceWithRawResponse(self._api.discussions)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._api.users)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._api.models)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._api.datasets)

    @cached_property
    def spaces(self) -> SpacesResourceWithRawResponse:
        return SpacesResourceWithRawResponse(self._api.spaces)

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._api.repos)

    @cached_property
    def sql_console(self) -> SqlConsoleResourceWithRawResponse:
        return SqlConsoleResourceWithRawResponse(self._api.sql_console)

    @cached_property
    def resolve_cache(self) -> ResolveCacheResourceWithRawResponse:
        return ResolveCacheResourceWithRawResponse(self._api.resolve_cache)

    @cached_property
    def papers(self) -> PapersResourceWithRawResponse:
        return PapersResourceWithRawResponse(self._api.papers)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._api.posts)

    @cached_property
    def collections(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self._api.collections)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._api.jobs)

    @cached_property
    def scheduled_jobs(self) -> ScheduledJobsResourceWithRawResponse:
        return ScheduledJobsResourceWithRawResponse(self._api.scheduled_jobs)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.get_daily_papers = async_to_raw_response_wrapper(
            api.get_daily_papers,
        )
        self.get_dataset_tags = async_to_raw_response_wrapper(
            api.get_dataset_tags,
        )
        self.get_model_tags = async_to_raw_response_wrapper(
            api.get_model_tags,
        )
        self.get_user_info = async_to_raw_response_wrapper(
            api.get_user_info,
        )

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithRawResponse:
        return AsyncNotificationsResourceWithRawResponse(self._api.notifications)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._api.settings)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._api.organizations)

    @cached_property
    def blog(self) -> AsyncBlogResourceWithRawResponse:
        return AsyncBlogResourceWithRawResponse(self._api.blog)

    @cached_property
    def docs(self) -> AsyncDocsResourceWithRawResponse:
        return AsyncDocsResourceWithRawResponse(self._api.docs)

    @cached_property
    def discussions(self) -> AsyncDiscussionsResourceWithRawResponse:
        return AsyncDiscussionsResourceWithRawResponse(self._api.discussions)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._api.users)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._api.models)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._api.datasets)

    @cached_property
    def spaces(self) -> AsyncSpacesResourceWithRawResponse:
        return AsyncSpacesResourceWithRawResponse(self._api.spaces)

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._api.repos)

    @cached_property
    def sql_console(self) -> AsyncSqlConsoleResourceWithRawResponse:
        return AsyncSqlConsoleResourceWithRawResponse(self._api.sql_console)

    @cached_property
    def resolve_cache(self) -> AsyncResolveCacheResourceWithRawResponse:
        return AsyncResolveCacheResourceWithRawResponse(self._api.resolve_cache)

    @cached_property
    def papers(self) -> AsyncPapersResourceWithRawResponse:
        return AsyncPapersResourceWithRawResponse(self._api.papers)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._api.posts)

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self._api.collections)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._api.jobs)

    @cached_property
    def scheduled_jobs(self) -> AsyncScheduledJobsResourceWithRawResponse:
        return AsyncScheduledJobsResourceWithRawResponse(self._api.scheduled_jobs)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.get_daily_papers = to_streamed_response_wrapper(
            api.get_daily_papers,
        )
        self.get_dataset_tags = to_streamed_response_wrapper(
            api.get_dataset_tags,
        )
        self.get_model_tags = to_streamed_response_wrapper(
            api.get_model_tags,
        )
        self.get_user_info = to_streamed_response_wrapper(
            api.get_user_info,
        )

    @cached_property
    def notifications(self) -> NotificationsResourceWithStreamingResponse:
        return NotificationsResourceWithStreamingResponse(self._api.notifications)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._api.settings)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._api.organizations)

    @cached_property
    def blog(self) -> BlogResourceWithStreamingResponse:
        return BlogResourceWithStreamingResponse(self._api.blog)

    @cached_property
    def docs(self) -> DocsResourceWithStreamingResponse:
        return DocsResourceWithStreamingResponse(self._api.docs)

    @cached_property
    def discussions(self) -> DiscussionsResourceWithStreamingResponse:
        return DiscussionsResourceWithStreamingResponse(self._api.discussions)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._api.users)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._api.models)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._api.datasets)

    @cached_property
    def spaces(self) -> SpacesResourceWithStreamingResponse:
        return SpacesResourceWithStreamingResponse(self._api.spaces)

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._api.repos)

    @cached_property
    def sql_console(self) -> SqlConsoleResourceWithStreamingResponse:
        return SqlConsoleResourceWithStreamingResponse(self._api.sql_console)

    @cached_property
    def resolve_cache(self) -> ResolveCacheResourceWithStreamingResponse:
        return ResolveCacheResourceWithStreamingResponse(self._api.resolve_cache)

    @cached_property
    def papers(self) -> PapersResourceWithStreamingResponse:
        return PapersResourceWithStreamingResponse(self._api.papers)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._api.posts)

    @cached_property
    def collections(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self._api.collections)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._api.jobs)

    @cached_property
    def scheduled_jobs(self) -> ScheduledJobsResourceWithStreamingResponse:
        return ScheduledJobsResourceWithStreamingResponse(self._api.scheduled_jobs)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.get_daily_papers = async_to_streamed_response_wrapper(
            api.get_daily_papers,
        )
        self.get_dataset_tags = async_to_streamed_response_wrapper(
            api.get_dataset_tags,
        )
        self.get_model_tags = async_to_streamed_response_wrapper(
            api.get_model_tags,
        )
        self.get_user_info = async_to_streamed_response_wrapper(
            api.get_user_info,
        )

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithStreamingResponse:
        return AsyncNotificationsResourceWithStreamingResponse(self._api.notifications)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._api.settings)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._api.organizations)

    @cached_property
    def blog(self) -> AsyncBlogResourceWithStreamingResponse:
        return AsyncBlogResourceWithStreamingResponse(self._api.blog)

    @cached_property
    def docs(self) -> AsyncDocsResourceWithStreamingResponse:
        return AsyncDocsResourceWithStreamingResponse(self._api.docs)

    @cached_property
    def discussions(self) -> AsyncDiscussionsResourceWithStreamingResponse:
        return AsyncDiscussionsResourceWithStreamingResponse(self._api.discussions)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._api.users)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._api.models)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._api.datasets)

    @cached_property
    def spaces(self) -> AsyncSpacesResourceWithStreamingResponse:
        return AsyncSpacesResourceWithStreamingResponse(self._api.spaces)

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._api.repos)

    @cached_property
    def sql_console(self) -> AsyncSqlConsoleResourceWithStreamingResponse:
        return AsyncSqlConsoleResourceWithStreamingResponse(self._api.sql_console)

    @cached_property
    def resolve_cache(self) -> AsyncResolveCacheResourceWithStreamingResponse:
        return AsyncResolveCacheResourceWithStreamingResponse(self._api.resolve_cache)

    @cached_property
    def papers(self) -> AsyncPapersResourceWithStreamingResponse:
        return AsyncPapersResourceWithStreamingResponse(self._api.papers)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._api.posts)

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self._api.collections)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._api.jobs)

    @cached_property
    def scheduled_jobs(self) -> AsyncScheduledJobsResourceWithStreamingResponse:
        return AsyncScheduledJobsResourceWithStreamingResponse(self._api.scheduled_jobs)
