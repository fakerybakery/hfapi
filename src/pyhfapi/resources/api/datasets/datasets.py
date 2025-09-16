# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, cast
from typing_extensions import Literal

import httpx

from .tag import (
    TagResource,
    AsyncTagResource,
    TagResourceWithRawResponse,
    AsyncTagResourceWithRawResponse,
    TagResourceWithStreamingResponse,
    AsyncTagResourceWithStreamingResponse,
)
from .branch import (
    BranchResource,
    AsyncBranchResource,
    BranchResourceWithRawResponse,
    AsyncBranchResourceWithRawResponse,
    BranchResourceWithStreamingResponse,
    AsyncBranchResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ...._utils import maybe_transform, async_maybe_transform
from .lfs_files import (
    LFSFilesResource,
    AsyncLFSFilesResource,
    LFSFilesResourceWithRawResponse,
    AsyncLFSFilesResourceWithRawResponse,
    LFSFilesResourceWithStreamingResponse,
    AsyncLFSFilesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import (
    dataset_commit_params,
    dataset_compare_params,
    dataset_list_refs_params,
    dataset_list_commits_params,
    dataset_super_squash_params,
    dataset_check_preupload_params,
    dataset_list_paths_info_params,
    dataset_update_settings_params,
    dataset_list_tree_content_params,
)
from .resource_group import (
    ResourceGroupResource,
    AsyncResourceGroupResource,
    ResourceGroupResourceWithRawResponse,
    AsyncResourceGroupResourceWithRawResponse,
    ResourceGroupResourceWithStreamingResponse,
    AsyncResourceGroupResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .user_access_request import (
    UserAccessRequestResource,
    AsyncUserAccessRequestResource,
    UserAccessRequestResourceWithRawResponse,
    AsyncUserAccessRequestResourceWithRawResponse,
    UserAccessRequestResourceWithStreamingResponse,
    AsyncUserAccessRequestResourceWithStreamingResponse,
)
from ....types.api.dataset_commit_response import DatasetCommitResponse
from ....types.api.dataset_list_refs_response import DatasetListRefsResponse
from ....types.api.dataset_list_commits_response import DatasetListCommitsResponse
from ....types.api.dataset_super_squash_response import DatasetSuperSquashResponse
from ....types.api.dataset_check_preupload_response import DatasetCheckPreuploadResponse
from ....types.api.dataset_list_paths_info_response import DatasetListPathsInfoResponse
from ....types.api.dataset_update_settings_response import DatasetUpdateSettingsResponse
from ....types.api.dataset_get_notebook_url_response import DatasetGetNotebookURLResponse
from ....types.api.dataset_list_tree_content_response import DatasetListTreeContentResponse
from ....types.api.dataset_get_xet_read_token_response import DatasetGetXetReadTokenResponse
from ....types.api.dataset_get_security_status_response import DatasetGetSecurityStatusResponse
from ....types.api.dataset_get_xet_write_token_response import DatasetGetXetWriteTokenResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def lfs_files(self) -> LFSFilesResource:
        return LFSFilesResource(self._client)

    @cached_property
    def tag(self) -> TagResource:
        return TagResource(self._client)

    @cached_property
    def branch(self) -> BranchResource:
        return BranchResource(self._client)

    @cached_property
    def resource_group(self) -> ResourceGroupResource:
        return ResourceGroupResource(self._client)

    @cached_property
    def user_access_request(self) -> UserAccessRequestResource:
        return UserAccessRequestResource(self._client)

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

    def check_preupload(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        files: Iterable[dataset_check_preupload_params.File],
        git_attributes: str | NotGiven = NOT_GIVEN,
        git_ignore: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCheckPreuploadResponse:
        """
        Check if a file should be uploaded through the Large File mechanism or directly.

        Args:
          git_attributes: Provide this parameter if you plan to modify `.gitattributes` yourself at the
              same time as uploading LFS files. Note that this is not needed if you solely
              rely on automatic LFS detection from HF: the commit endpoint will automatically
              edit the `.gitattributes` file to track the files passed to its `lfsFiles`
              param.

          git_ignore: Content of the .gitignore file for the revision. Optional, otherwise takes the
              existing content of `.gitignore` for the revision.

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
        return self._post(
            f"/api/datasets/{namespace}/{repo}/preupload/{rev}",
            body=maybe_transform(
                {
                    "files": files,
                    "git_attributes": git_attributes,
                    "git_ignore": git_ignore,
                },
                dataset_check_preupload_params.DatasetCheckPreuploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCheckPreuploadResponse,
        )

    def commit(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        create_pr: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCommitResponse:
        """
        For legacy reason, we support both `application/json` and `application/x-ndjson`
        but we recommend using `application/x-ndjson` to create a commit.

        JSON-lines payload:

        ```json
        {
          "key": "header",
          "value": {
            "summary": "string (REQUIRED)",
            "description": "string (OPTIONAL - defaults to empty string)",
            "parentCommit": "string (OPTIONAL - 40-character hex SHA)"
          }
        }
        {
          "key": "file",
          "value": {
            "path": "string (REQUIRED)",
            "content": "string (OPTIONAL - required if oldPath not set)",
            "encoding": "utf-8 | base64 (OPTIONAL - defaults to utf-8)",
            "oldPath": "string (OPTIONAL - for move/rename operations)"
          }
        }
        {
          "key": "deletedEntry",
          "value": {
            "path": "string (REQUIRED)"
          }
        }
        {
          "key": "lfsFile",
          "value": {
            "path": "string (REQUIRED - max 1000 chars)",
            "oid": "string (OPTIONAL - required if oldPath not set, 64 hex chars)",
            "algo": "sha256 (OPTIONAL - only sha256 supported)",
            "size": "number (OPTIONAL - required if oldPath is set)",
            "oldPath": "string (OPTIONAL - for move/rename operations)"
          }
        }
        ```

        JSON payload:

        ```json
        {
          "summary": "string (REQUIRED)",
          "description": "string (OPTIONAL - defaults to empty string)",
          "parentCommit": "string (OPTIONAL - 40-character hex SHA)"
          "files": [
            {
              "path": "string (REQUIRED)",
              "content": "string (OPTIONAL - required if oldPath not set)",
              "encoding": "utf-8 | base64 (OPTIONAL - defaults to utf-8)",
              "oldPath": "string (OPTIONAL - for move/rename operations)"
            }
          ],
          "deletedEntries": [
            {
              "path": "string (REQUIRED)"
            }
          ],
          "lfsFiles": [
            {
              "path": "string (REQUIRED - max 1000 chars)",
              "oid": "string (OPTIONAL - required if oldPath not set, 64 hex chars)",
              "algo": "sha256 (OPTIONAL - only sha256 supported)",
              "size": "number (OPTIONAL - required if oldPath is set)",
              "oldPath": "string (OPTIONAL - for move/rename operations)"
            }
          ]
        }
        ```

        Args:
          create_pr: Whether to create a pull request from the commit

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
        return self._post(
            f"/api/datasets/{namespace}/{repo}/commit/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"create_pr": create_pr}, dataset_commit_params.DatasetCommitParams),
            ),
            cast_to=DatasetCommitResponse,
        )

    def compare(
        self,
        compare: str,
        *,
        namespace: str,
        repo: str,
        raw: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get a compare rev

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
        if not compare:
            raise ValueError(f"Expected a non-empty value for `compare` but received {compare!r}")
        return self._get(
            f"/api/datasets/{namespace}/{repo}/compare/{compare}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"raw": raw}, dataset_compare_params.DatasetCompareParams),
            ),
            cast_to=str,
        )

    def get_notebook_url(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetNotebookURLResponse:
        """
        Get a jupyter notebook URL

        Args:
          path: Wildcard path parameter

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
        return cast(
            DatasetGetNotebookURLResponse,
            self._get(
                f"/api/datasets/{namespace}/{repo}/notebook/{rev}/{path}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, DatasetGetNotebookURLResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get_security_status(
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
    ) -> DatasetGetSecurityStatusResponse:
        """
        Get the security status of a repo

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
            f"/api/datasets/{namespace}/{repo}/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetSecurityStatusResponse,
        )

    def get_xet_read_token(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetXetReadTokenResponse:
        """
        Get a read short-lived access token for XET

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return self._get(
            f"/api/datasets/{namespace}/{repo}/xet-read-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetXetReadTokenResponse,
        )

    def get_xet_write_token(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetXetWriteTokenResponse:
        """
        Get a write short-lived access token for XET

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return self._get(
            f"/api/datasets/{namespace}/{repo}/xet-write-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetXetWriteTokenResponse,
        )

    def list_commits(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        expand: List[Literal["formatted"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListCommitsResponse:
        """
        List commits

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return self._get(
            f"/api/datasets/{namespace}/{repo}/commits/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "limit": limit,
                        "p": p,
                    },
                    dataset_list_commits_params.DatasetListCommitsParams,
                ),
            ),
            cast_to=DatasetListCommitsResponse,
        )

    def list_paths_info(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        expand: Union[bool, object],
        paths: Union[SequenceNotStr[str], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListPathsInfoResponse:
        """
        List paths info

        Args:
          expand: Expand the response with the last commit and security file status

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
        return self._post(
            f"/api/datasets/{namespace}/{repo}/paths-info/{rev}",
            body=maybe_transform(
                {
                    "expand": expand,
                    "paths": paths,
                },
                dataset_list_paths_info_params.DatasetListPathsInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListPathsInfoResponse,
        )

    def list_refs(
        self,
        repo: str,
        *,
        namespace: str,
        include_prs: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListRefsResponse:
        """
        List references

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
            f"/api/datasets/{namespace}/{repo}/refs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_prs": include_prs}, dataset_list_refs_params.DatasetListRefsParams),
            ),
            cast_to=DatasetListRefsResponse,
        )

    def list_tree_content(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: object | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        recursive: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListTreeContentResponse:
        """
        List the content of a repository tree, with pagination support.

        Args:
          path: Wildcard path parameter

          expand: If true, returns returns associated commit data for each entry and security
              scanner metadata.

          limit: 1.000 by default, 100 by default for expand=true

          recursive: If true, returns the tree recursively.

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
        return self._get(
            f"/api/datasets/{namespace}/{repo}/tree/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "expand": expand,
                        "limit": limit,
                        "recursive": recursive,
                    },
                    dataset_list_tree_content_params.DatasetListTreeContentParams,
                ),
            ),
            cast_to=DatasetListTreeContentResponse,
        )

    def super_squash(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetSuperSquashResponse:
        """
        This will squash all commits in the current ref into a single commit with the
        given message. Action is irreversible.

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return self._post(
            f"/api/datasets/{namespace}/{repo}/super-squash/{rev}",
            body=maybe_transform({"message": message}, dataset_super_squash_params.DatasetSuperSquashParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetSuperSquashResponse,
        )

    def update_settings(
        self,
        repo: str,
        *,
        namespace: str,
        discussions_disabled: bool | NotGiven = NOT_GIVEN,
        gated: Union[Literal["auto", "manual"], object] | NotGiven = NOT_GIVEN,
        gated_notifications_email: str | NotGiven = NOT_GIVEN,
        gated_notifications_mode: Literal["bulk", "real-time"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        xet_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetUpdateSettingsResponse:
        """
        Update the settings of a repo

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
        return self._put(
            f"/api/datasets/{namespace}/{repo}/settings",
            body=maybe_transform(
                {
                    "discussions_disabled": discussions_disabled,
                    "gated": gated,
                    "gated_notifications_email": gated_notifications_email,
                    "gated_notifications_mode": gated_notifications_mode,
                    "private": private,
                    "xet_enabled": xet_enabled,
                },
                dataset_update_settings_params.DatasetUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetUpdateSettingsResponse,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def lfs_files(self) -> AsyncLFSFilesResource:
        return AsyncLFSFilesResource(self._client)

    @cached_property
    def tag(self) -> AsyncTagResource:
        return AsyncTagResource(self._client)

    @cached_property
    def branch(self) -> AsyncBranchResource:
        return AsyncBranchResource(self._client)

    @cached_property
    def resource_group(self) -> AsyncResourceGroupResource:
        return AsyncResourceGroupResource(self._client)

    @cached_property
    def user_access_request(self) -> AsyncUserAccessRequestResource:
        return AsyncUserAccessRequestResource(self._client)

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

    async def check_preupload(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        files: Iterable[dataset_check_preupload_params.File],
        git_attributes: str | NotGiven = NOT_GIVEN,
        git_ignore: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCheckPreuploadResponse:
        """
        Check if a file should be uploaded through the Large File mechanism or directly.

        Args:
          git_attributes: Provide this parameter if you plan to modify `.gitattributes` yourself at the
              same time as uploading LFS files. Note that this is not needed if you solely
              rely on automatic LFS detection from HF: the commit endpoint will automatically
              edit the `.gitattributes` file to track the files passed to its `lfsFiles`
              param.

          git_ignore: Content of the .gitignore file for the revision. Optional, otherwise takes the
              existing content of `.gitignore` for the revision.

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
        return await self._post(
            f"/api/datasets/{namespace}/{repo}/preupload/{rev}",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "git_attributes": git_attributes,
                    "git_ignore": git_ignore,
                },
                dataset_check_preupload_params.DatasetCheckPreuploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCheckPreuploadResponse,
        )

    async def commit(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        create_pr: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCommitResponse:
        """
        For legacy reason, we support both `application/json` and `application/x-ndjson`
        but we recommend using `application/x-ndjson` to create a commit.

        JSON-lines payload:

        ```json
        {
          "key": "header",
          "value": {
            "summary": "string (REQUIRED)",
            "description": "string (OPTIONAL - defaults to empty string)",
            "parentCommit": "string (OPTIONAL - 40-character hex SHA)"
          }
        }
        {
          "key": "file",
          "value": {
            "path": "string (REQUIRED)",
            "content": "string (OPTIONAL - required if oldPath not set)",
            "encoding": "utf-8 | base64 (OPTIONAL - defaults to utf-8)",
            "oldPath": "string (OPTIONAL - for move/rename operations)"
          }
        }
        {
          "key": "deletedEntry",
          "value": {
            "path": "string (REQUIRED)"
          }
        }
        {
          "key": "lfsFile",
          "value": {
            "path": "string (REQUIRED - max 1000 chars)",
            "oid": "string (OPTIONAL - required if oldPath not set, 64 hex chars)",
            "algo": "sha256 (OPTIONAL - only sha256 supported)",
            "size": "number (OPTIONAL - required if oldPath is set)",
            "oldPath": "string (OPTIONAL - for move/rename operations)"
          }
        }
        ```

        JSON payload:

        ```json
        {
          "summary": "string (REQUIRED)",
          "description": "string (OPTIONAL - defaults to empty string)",
          "parentCommit": "string (OPTIONAL - 40-character hex SHA)"
          "files": [
            {
              "path": "string (REQUIRED)",
              "content": "string (OPTIONAL - required if oldPath not set)",
              "encoding": "utf-8 | base64 (OPTIONAL - defaults to utf-8)",
              "oldPath": "string (OPTIONAL - for move/rename operations)"
            }
          ],
          "deletedEntries": [
            {
              "path": "string (REQUIRED)"
            }
          ],
          "lfsFiles": [
            {
              "path": "string (REQUIRED - max 1000 chars)",
              "oid": "string (OPTIONAL - required if oldPath not set, 64 hex chars)",
              "algo": "sha256 (OPTIONAL - only sha256 supported)",
              "size": "number (OPTIONAL - required if oldPath is set)",
              "oldPath": "string (OPTIONAL - for move/rename operations)"
            }
          ]
        }
        ```

        Args:
          create_pr: Whether to create a pull request from the commit

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
        return await self._post(
            f"/api/datasets/{namespace}/{repo}/commit/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"create_pr": create_pr}, dataset_commit_params.DatasetCommitParams),
            ),
            cast_to=DatasetCommitResponse,
        )

    async def compare(
        self,
        compare: str,
        *,
        namespace: str,
        repo: str,
        raw: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get a compare rev

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
        if not compare:
            raise ValueError(f"Expected a non-empty value for `compare` but received {compare!r}")
        return await self._get(
            f"/api/datasets/{namespace}/{repo}/compare/{compare}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"raw": raw}, dataset_compare_params.DatasetCompareParams),
            ),
            cast_to=str,
        )

    async def get_notebook_url(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetNotebookURLResponse:
        """
        Get a jupyter notebook URL

        Args:
          path: Wildcard path parameter

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
        return cast(
            DatasetGetNotebookURLResponse,
            await self._get(
                f"/api/datasets/{namespace}/{repo}/notebook/{rev}/{path}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, DatasetGetNotebookURLResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get_security_status(
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
    ) -> DatasetGetSecurityStatusResponse:
        """
        Get the security status of a repo

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
            f"/api/datasets/{namespace}/{repo}/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetSecurityStatusResponse,
        )

    async def get_xet_read_token(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetXetReadTokenResponse:
        """
        Get a read short-lived access token for XET

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return await self._get(
            f"/api/datasets/{namespace}/{repo}/xet-read-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetXetReadTokenResponse,
        )

    async def get_xet_write_token(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetXetWriteTokenResponse:
        """
        Get a write short-lived access token for XET

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return await self._get(
            f"/api/datasets/{namespace}/{repo}/xet-write-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetXetWriteTokenResponse,
        )

    async def list_commits(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        expand: List[Literal["formatted"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListCommitsResponse:
        """
        List commits

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return await self._get(
            f"/api/datasets/{namespace}/{repo}/commits/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "limit": limit,
                        "p": p,
                    },
                    dataset_list_commits_params.DatasetListCommitsParams,
                ),
            ),
            cast_to=DatasetListCommitsResponse,
        )

    async def list_paths_info(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        expand: Union[bool, object],
        paths: Union[SequenceNotStr[str], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListPathsInfoResponse:
        """
        List paths info

        Args:
          expand: Expand the response with the last commit and security file status

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
        return await self._post(
            f"/api/datasets/{namespace}/{repo}/paths-info/{rev}",
            body=await async_maybe_transform(
                {
                    "expand": expand,
                    "paths": paths,
                },
                dataset_list_paths_info_params.DatasetListPathsInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListPathsInfoResponse,
        )

    async def list_refs(
        self,
        repo: str,
        *,
        namespace: str,
        include_prs: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListRefsResponse:
        """
        List references

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
            f"/api/datasets/{namespace}/{repo}/refs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_prs": include_prs}, dataset_list_refs_params.DatasetListRefsParams
                ),
            ),
            cast_to=DatasetListRefsResponse,
        )

    async def list_tree_content(
        self,
        path: str,
        *,
        namespace: str,
        repo: str,
        rev: str,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: object | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        recursive: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListTreeContentResponse:
        """
        List the content of a repository tree, with pagination support.

        Args:
          path: Wildcard path parameter

          expand: If true, returns returns associated commit data for each entry and security
              scanner metadata.

          limit: 1.000 by default, 100 by default for expand=true

          recursive: If true, returns the tree recursively.

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
        return await self._get(
            f"/api/datasets/{namespace}/{repo}/tree/{rev}/{path}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "expand": expand,
                        "limit": limit,
                        "recursive": recursive,
                    },
                    dataset_list_tree_content_params.DatasetListTreeContentParams,
                ),
            ),
            cast_to=DatasetListTreeContentResponse,
        )

    async def super_squash(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetSuperSquashResponse:
        """
        This will squash all commits in the current ref into a single commit with the
        given message. Action is irreversible.

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
        if not rev:
            raise ValueError(f"Expected a non-empty value for `rev` but received {rev!r}")
        return await self._post(
            f"/api/datasets/{namespace}/{repo}/super-squash/{rev}",
            body=await async_maybe_transform(
                {"message": message}, dataset_super_squash_params.DatasetSuperSquashParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetSuperSquashResponse,
        )

    async def update_settings(
        self,
        repo: str,
        *,
        namespace: str,
        discussions_disabled: bool | NotGiven = NOT_GIVEN,
        gated: Union[Literal["auto", "manual"], object] | NotGiven = NOT_GIVEN,
        gated_notifications_email: str | NotGiven = NOT_GIVEN,
        gated_notifications_mode: Literal["bulk", "real-time"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        xet_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetUpdateSettingsResponse:
        """
        Update the settings of a repo

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
        return await self._put(
            f"/api/datasets/{namespace}/{repo}/settings",
            body=await async_maybe_transform(
                {
                    "discussions_disabled": discussions_disabled,
                    "gated": gated,
                    "gated_notifications_email": gated_notifications_email,
                    "gated_notifications_mode": gated_notifications_mode,
                    "private": private,
                    "xet_enabled": xet_enabled,
                },
                dataset_update_settings_params.DatasetUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetUpdateSettingsResponse,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.check_preupload = to_raw_response_wrapper(
            datasets.check_preupload,
        )
        self.commit = to_raw_response_wrapper(
            datasets.commit,
        )
        self.compare = to_raw_response_wrapper(
            datasets.compare,
        )
        self.get_notebook_url = to_raw_response_wrapper(
            datasets.get_notebook_url,
        )
        self.get_security_status = to_raw_response_wrapper(
            datasets.get_security_status,
        )
        self.get_xet_read_token = to_raw_response_wrapper(
            datasets.get_xet_read_token,
        )
        self.get_xet_write_token = to_raw_response_wrapper(
            datasets.get_xet_write_token,
        )
        self.list_commits = to_raw_response_wrapper(
            datasets.list_commits,
        )
        self.list_paths_info = to_raw_response_wrapper(
            datasets.list_paths_info,
        )
        self.list_refs = to_raw_response_wrapper(
            datasets.list_refs,
        )
        self.list_tree_content = to_raw_response_wrapper(
            datasets.list_tree_content,
        )
        self.super_squash = to_raw_response_wrapper(
            datasets.super_squash,
        )
        self.update_settings = to_raw_response_wrapper(
            datasets.update_settings,
        )

    @cached_property
    def lfs_files(self) -> LFSFilesResourceWithRawResponse:
        return LFSFilesResourceWithRawResponse(self._datasets.lfs_files)

    @cached_property
    def tag(self) -> TagResourceWithRawResponse:
        return TagResourceWithRawResponse(self._datasets.tag)

    @cached_property
    def branch(self) -> BranchResourceWithRawResponse:
        return BranchResourceWithRawResponse(self._datasets.branch)

    @cached_property
    def resource_group(self) -> ResourceGroupResourceWithRawResponse:
        return ResourceGroupResourceWithRawResponse(self._datasets.resource_group)

    @cached_property
    def user_access_request(self) -> UserAccessRequestResourceWithRawResponse:
        return UserAccessRequestResourceWithRawResponse(self._datasets.user_access_request)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.check_preupload = async_to_raw_response_wrapper(
            datasets.check_preupload,
        )
        self.commit = async_to_raw_response_wrapper(
            datasets.commit,
        )
        self.compare = async_to_raw_response_wrapper(
            datasets.compare,
        )
        self.get_notebook_url = async_to_raw_response_wrapper(
            datasets.get_notebook_url,
        )
        self.get_security_status = async_to_raw_response_wrapper(
            datasets.get_security_status,
        )
        self.get_xet_read_token = async_to_raw_response_wrapper(
            datasets.get_xet_read_token,
        )
        self.get_xet_write_token = async_to_raw_response_wrapper(
            datasets.get_xet_write_token,
        )
        self.list_commits = async_to_raw_response_wrapper(
            datasets.list_commits,
        )
        self.list_paths_info = async_to_raw_response_wrapper(
            datasets.list_paths_info,
        )
        self.list_refs = async_to_raw_response_wrapper(
            datasets.list_refs,
        )
        self.list_tree_content = async_to_raw_response_wrapper(
            datasets.list_tree_content,
        )
        self.super_squash = async_to_raw_response_wrapper(
            datasets.super_squash,
        )
        self.update_settings = async_to_raw_response_wrapper(
            datasets.update_settings,
        )

    @cached_property
    def lfs_files(self) -> AsyncLFSFilesResourceWithRawResponse:
        return AsyncLFSFilesResourceWithRawResponse(self._datasets.lfs_files)

    @cached_property
    def tag(self) -> AsyncTagResourceWithRawResponse:
        return AsyncTagResourceWithRawResponse(self._datasets.tag)

    @cached_property
    def branch(self) -> AsyncBranchResourceWithRawResponse:
        return AsyncBranchResourceWithRawResponse(self._datasets.branch)

    @cached_property
    def resource_group(self) -> AsyncResourceGroupResourceWithRawResponse:
        return AsyncResourceGroupResourceWithRawResponse(self._datasets.resource_group)

    @cached_property
    def user_access_request(self) -> AsyncUserAccessRequestResourceWithRawResponse:
        return AsyncUserAccessRequestResourceWithRawResponse(self._datasets.user_access_request)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.check_preupload = to_streamed_response_wrapper(
            datasets.check_preupload,
        )
        self.commit = to_streamed_response_wrapper(
            datasets.commit,
        )
        self.compare = to_streamed_response_wrapper(
            datasets.compare,
        )
        self.get_notebook_url = to_streamed_response_wrapper(
            datasets.get_notebook_url,
        )
        self.get_security_status = to_streamed_response_wrapper(
            datasets.get_security_status,
        )
        self.get_xet_read_token = to_streamed_response_wrapper(
            datasets.get_xet_read_token,
        )
        self.get_xet_write_token = to_streamed_response_wrapper(
            datasets.get_xet_write_token,
        )
        self.list_commits = to_streamed_response_wrapper(
            datasets.list_commits,
        )
        self.list_paths_info = to_streamed_response_wrapper(
            datasets.list_paths_info,
        )
        self.list_refs = to_streamed_response_wrapper(
            datasets.list_refs,
        )
        self.list_tree_content = to_streamed_response_wrapper(
            datasets.list_tree_content,
        )
        self.super_squash = to_streamed_response_wrapper(
            datasets.super_squash,
        )
        self.update_settings = to_streamed_response_wrapper(
            datasets.update_settings,
        )

    @cached_property
    def lfs_files(self) -> LFSFilesResourceWithStreamingResponse:
        return LFSFilesResourceWithStreamingResponse(self._datasets.lfs_files)

    @cached_property
    def tag(self) -> TagResourceWithStreamingResponse:
        return TagResourceWithStreamingResponse(self._datasets.tag)

    @cached_property
    def branch(self) -> BranchResourceWithStreamingResponse:
        return BranchResourceWithStreamingResponse(self._datasets.branch)

    @cached_property
    def resource_group(self) -> ResourceGroupResourceWithStreamingResponse:
        return ResourceGroupResourceWithStreamingResponse(self._datasets.resource_group)

    @cached_property
    def user_access_request(self) -> UserAccessRequestResourceWithStreamingResponse:
        return UserAccessRequestResourceWithStreamingResponse(self._datasets.user_access_request)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.check_preupload = async_to_streamed_response_wrapper(
            datasets.check_preupload,
        )
        self.commit = async_to_streamed_response_wrapper(
            datasets.commit,
        )
        self.compare = async_to_streamed_response_wrapper(
            datasets.compare,
        )
        self.get_notebook_url = async_to_streamed_response_wrapper(
            datasets.get_notebook_url,
        )
        self.get_security_status = async_to_streamed_response_wrapper(
            datasets.get_security_status,
        )
        self.get_xet_read_token = async_to_streamed_response_wrapper(
            datasets.get_xet_read_token,
        )
        self.get_xet_write_token = async_to_streamed_response_wrapper(
            datasets.get_xet_write_token,
        )
        self.list_commits = async_to_streamed_response_wrapper(
            datasets.list_commits,
        )
        self.list_paths_info = async_to_streamed_response_wrapper(
            datasets.list_paths_info,
        )
        self.list_refs = async_to_streamed_response_wrapper(
            datasets.list_refs,
        )
        self.list_tree_content = async_to_streamed_response_wrapper(
            datasets.list_tree_content,
        )
        self.super_squash = async_to_streamed_response_wrapper(
            datasets.super_squash,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            datasets.update_settings,
        )

    @cached_property
    def lfs_files(self) -> AsyncLFSFilesResourceWithStreamingResponse:
        return AsyncLFSFilesResourceWithStreamingResponse(self._datasets.lfs_files)

    @cached_property
    def tag(self) -> AsyncTagResourceWithStreamingResponse:
        return AsyncTagResourceWithStreamingResponse(self._datasets.tag)

    @cached_property
    def branch(self) -> AsyncBranchResourceWithStreamingResponse:
        return AsyncBranchResourceWithStreamingResponse(self._datasets.branch)

    @cached_property
    def resource_group(self) -> AsyncResourceGroupResourceWithStreamingResponse:
        return AsyncResourceGroupResourceWithStreamingResponse(self._datasets.resource_group)

    @cached_property
    def user_access_request(self) -> AsyncUserAccessRequestResourceWithStreamingResponse:
        return AsyncUserAccessRequestResourceWithStreamingResponse(self._datasets.user_access_request)
