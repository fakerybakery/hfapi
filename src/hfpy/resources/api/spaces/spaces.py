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
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, SequenceNotStr
from ...._utils import maybe_transform, async_maybe_transform
from .lfs_files import (
    LFSFilesResource,
    AsyncLFSFilesResource,
    LFSFilesResourceWithRawResponse,
    AsyncLFSFilesResourceWithRawResponse,
    LFSFilesResourceWithStreamingResponse,
    AsyncLFSFilesResourceWithStreamingResponse,
)
from .variables import (
    VariablesResource,
    AsyncVariablesResource,
    VariablesResourceWithRawResponse,
    AsyncVariablesResourceWithRawResponse,
    VariablesResourceWithStreamingResponse,
    AsyncVariablesResourceWithStreamingResponse,
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
    space_commit_params,
    space_compare_params,
    space_list_refs_params,
    space_list_commits_params,
    space_super_squash_params,
    space_stream_events_params,
    space_check_preupload_params,
    space_list_paths_info_params,
    space_update_settings_params,
    space_list_tree_content_params,
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
from ....types.api.space_commit_response import SpaceCommitResponse
from ....types.api.space_list_refs_response import SpaceListRefsResponse
from ....types.api.space_list_commits_response import SpaceListCommitsResponse
from ....types.api.space_super_squash_response import SpaceSuperSquashResponse
from ....types.api.space_check_preupload_response import SpaceCheckPreuploadResponse
from ....types.api.space_list_paths_info_response import SpaceListPathsInfoResponse
from ....types.api.space_update_settings_response import SpaceUpdateSettingsResponse
from ....types.api.space_get_notebook_url_response import SpaceGetNotebookURLResponse
from ....types.api.space_list_tree_content_response import SpaceListTreeContentResponse
from ....types.api.space_get_xet_read_token_response import SpaceGetXetReadTokenResponse
from ....types.api.space_get_security_status_response import SpaceGetSecurityStatusResponse
from ....types.api.space_get_xet_write_token_response import SpaceGetXetWriteTokenResponse

__all__ = ["SpacesResource", "AsyncSpacesResource"]


class SpacesResource(SyncAPIResource):
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
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def variables(self) -> VariablesResource:
        return VariablesResource(self._client)

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

    def check_preupload(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        files: Iterable[space_check_preupload_params.File],
        git_attributes: str | NotGiven = NOT_GIVEN,
        git_ignore: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpaceCheckPreuploadResponse:
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
            f"/api/spaces/{namespace}/{repo}/preupload/{rev}",
            body=maybe_transform(
                {
                    "files": files,
                    "git_attributes": git_attributes,
                    "git_ignore": git_ignore,
                },
                space_check_preupload_params.SpaceCheckPreuploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceCheckPreuploadResponse,
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
    ) -> SpaceCommitResponse:
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
            f"/api/spaces/{namespace}/{repo}/commit/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"create_pr": create_pr}, space_commit_params.SpaceCommitParams),
            ),
            cast_to=SpaceCommitResponse,
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
            f"/api/spaces/{namespace}/{repo}/compare/{compare}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"raw": raw}, space_compare_params.SpaceCompareParams),
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
    ) -> SpaceGetNotebookURLResponse:
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
            SpaceGetNotebookURLResponse,
            self._get(
                f"/api/spaces/{namespace}/{repo}/notebook/{rev}/{path}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, SpaceGetNotebookURLResponse
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
    ) -> SpaceGetSecurityStatusResponse:
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
            f"/api/spaces/{namespace}/{repo}/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceGetSecurityStatusResponse,
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
    ) -> SpaceGetXetReadTokenResponse:
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
            f"/api/spaces/{namespace}/{repo}/xet-read-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceGetXetReadTokenResponse,
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
    ) -> SpaceGetXetWriteTokenResponse:
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
            f"/api/spaces/{namespace}/{repo}/xet-write-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceGetXetWriteTokenResponse,
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
    ) -> SpaceListCommitsResponse:
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
            f"/api/spaces/{namespace}/{repo}/commits/{rev}",
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
                    space_list_commits_params.SpaceListCommitsParams,
                ),
            ),
            cast_to=SpaceListCommitsResponse,
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
    ) -> SpaceListPathsInfoResponse:
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
            f"/api/spaces/{namespace}/{repo}/paths-info/{rev}",
            body=maybe_transform(
                {
                    "expand": expand,
                    "paths": paths,
                },
                space_list_paths_info_params.SpaceListPathsInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceListPathsInfoResponse,
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
    ) -> SpaceListRefsResponse:
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
            f"/api/spaces/{namespace}/{repo}/refs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_prs": include_prs}, space_list_refs_params.SpaceListRefsParams),
            ),
            cast_to=SpaceListRefsResponse,
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
    ) -> SpaceListTreeContentResponse:
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
            f"/api/spaces/{namespace}/{repo}/tree/{rev}/{path}",
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
                    space_list_tree_content_params.SpaceListTreeContentParams,
                ),
            ),
            cast_to=SpaceListTreeContentResponse,
        )

    def stream_events(
        self,
        repo: str,
        *,
        namespace: str,
        session_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get status updates for a specific Space in a streaming fashion, with SSE
        protocol

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
        return self._get(
            f"/api/spaces/{namespace}/{repo}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"session_uuid": session_uuid}, space_stream_events_params.SpaceStreamEventsParams
                ),
            ),
            cast_to=NoneType,
        )

    def stream_logs(
        self,
        log_type: Literal["build", "run"],
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get logs for a specific Space in a streaming fashion, with SSE protocol

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
        if not log_type:
            raise ValueError(f"Expected a non-empty value for `log_type` but received {log_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/spaces/{namespace}/{repo}/logs/{log_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stream_metrics(
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
    ) -> None:
        """
        Get live metrics for a specific Space in a streaming fashion, with SSE protocol,
        such as current Zero-GPU usage

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
        return self._get(
            f"/api/spaces/{namespace}/{repo}/metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SpaceSuperSquashResponse:
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
            f"/api/spaces/{namespace}/{repo}/super-squash/{rev}",
            body=maybe_transform({"message": message}, space_super_squash_params.SpaceSuperSquashParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceSuperSquashResponse,
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
    ) -> SpaceUpdateSettingsResponse:
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
            f"/api/spaces/{namespace}/{repo}/settings",
            body=maybe_transform(
                {
                    "discussions_disabled": discussions_disabled,
                    "gated": gated,
                    "gated_notifications_email": gated_notifications_email,
                    "gated_notifications_mode": gated_notifications_mode,
                    "private": private,
                    "xet_enabled": xet_enabled,
                },
                space_update_settings_params.SpaceUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceUpdateSettingsResponse,
        )


class AsyncSpacesResource(AsyncAPIResource):
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
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def variables(self) -> AsyncVariablesResource:
        return AsyncVariablesResource(self._client)

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

    async def check_preupload(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        files: Iterable[space_check_preupload_params.File],
        git_attributes: str | NotGiven = NOT_GIVEN,
        git_ignore: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpaceCheckPreuploadResponse:
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
            f"/api/spaces/{namespace}/{repo}/preupload/{rev}",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "git_attributes": git_attributes,
                    "git_ignore": git_ignore,
                },
                space_check_preupload_params.SpaceCheckPreuploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceCheckPreuploadResponse,
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
    ) -> SpaceCommitResponse:
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
            f"/api/spaces/{namespace}/{repo}/commit/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"create_pr": create_pr}, space_commit_params.SpaceCommitParams),
            ),
            cast_to=SpaceCommitResponse,
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
            f"/api/spaces/{namespace}/{repo}/compare/{compare}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"raw": raw}, space_compare_params.SpaceCompareParams),
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
    ) -> SpaceGetNotebookURLResponse:
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
            SpaceGetNotebookURLResponse,
            await self._get(
                f"/api/spaces/{namespace}/{repo}/notebook/{rev}/{path}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, SpaceGetNotebookURLResponse
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
    ) -> SpaceGetSecurityStatusResponse:
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
            f"/api/spaces/{namespace}/{repo}/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceGetSecurityStatusResponse,
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
    ) -> SpaceGetXetReadTokenResponse:
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
            f"/api/spaces/{namespace}/{repo}/xet-read-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceGetXetReadTokenResponse,
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
    ) -> SpaceGetXetWriteTokenResponse:
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
            f"/api/spaces/{namespace}/{repo}/xet-write-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceGetXetWriteTokenResponse,
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
    ) -> SpaceListCommitsResponse:
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
            f"/api/spaces/{namespace}/{repo}/commits/{rev}",
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
                    space_list_commits_params.SpaceListCommitsParams,
                ),
            ),
            cast_to=SpaceListCommitsResponse,
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
    ) -> SpaceListPathsInfoResponse:
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
            f"/api/spaces/{namespace}/{repo}/paths-info/{rev}",
            body=await async_maybe_transform(
                {
                    "expand": expand,
                    "paths": paths,
                },
                space_list_paths_info_params.SpaceListPathsInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceListPathsInfoResponse,
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
    ) -> SpaceListRefsResponse:
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
            f"/api/spaces/{namespace}/{repo}/refs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_prs": include_prs}, space_list_refs_params.SpaceListRefsParams
                ),
            ),
            cast_to=SpaceListRefsResponse,
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
    ) -> SpaceListTreeContentResponse:
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
            f"/api/spaces/{namespace}/{repo}/tree/{rev}/{path}",
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
                    space_list_tree_content_params.SpaceListTreeContentParams,
                ),
            ),
            cast_to=SpaceListTreeContentResponse,
        )

    async def stream_events(
        self,
        repo: str,
        *,
        namespace: str,
        session_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get status updates for a specific Space in a streaming fashion, with SSE
        protocol

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
        return await self._get(
            f"/api/spaces/{namespace}/{repo}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_uuid": session_uuid}, space_stream_events_params.SpaceStreamEventsParams
                ),
            ),
            cast_to=NoneType,
        )

    async def stream_logs(
        self,
        log_type: Literal["build", "run"],
        *,
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get logs for a specific Space in a streaming fashion, with SSE protocol

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
        if not log_type:
            raise ValueError(f"Expected a non-empty value for `log_type` but received {log_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/spaces/{namespace}/{repo}/logs/{log_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stream_metrics(
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
    ) -> None:
        """
        Get live metrics for a specific Space in a streaming fashion, with SSE protocol,
        such as current Zero-GPU usage

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
        return await self._get(
            f"/api/spaces/{namespace}/{repo}/metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SpaceSuperSquashResponse:
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
            f"/api/spaces/{namespace}/{repo}/super-squash/{rev}",
            body=await async_maybe_transform({"message": message}, space_super_squash_params.SpaceSuperSquashParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceSuperSquashResponse,
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
    ) -> SpaceUpdateSettingsResponse:
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
            f"/api/spaces/{namespace}/{repo}/settings",
            body=await async_maybe_transform(
                {
                    "discussions_disabled": discussions_disabled,
                    "gated": gated,
                    "gated_notifications_email": gated_notifications_email,
                    "gated_notifications_mode": gated_notifications_mode,
                    "private": private,
                    "xet_enabled": xet_enabled,
                },
                space_update_settings_params.SpaceUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpaceUpdateSettingsResponse,
        )


class SpacesResourceWithRawResponse:
    def __init__(self, spaces: SpacesResource) -> None:
        self._spaces = spaces

        self.check_preupload = to_raw_response_wrapper(
            spaces.check_preupload,
        )
        self.commit = to_raw_response_wrapper(
            spaces.commit,
        )
        self.compare = to_raw_response_wrapper(
            spaces.compare,
        )
        self.get_notebook_url = to_raw_response_wrapper(
            spaces.get_notebook_url,
        )
        self.get_security_status = to_raw_response_wrapper(
            spaces.get_security_status,
        )
        self.get_xet_read_token = to_raw_response_wrapper(
            spaces.get_xet_read_token,
        )
        self.get_xet_write_token = to_raw_response_wrapper(
            spaces.get_xet_write_token,
        )
        self.list_commits = to_raw_response_wrapper(
            spaces.list_commits,
        )
        self.list_paths_info = to_raw_response_wrapper(
            spaces.list_paths_info,
        )
        self.list_refs = to_raw_response_wrapper(
            spaces.list_refs,
        )
        self.list_tree_content = to_raw_response_wrapper(
            spaces.list_tree_content,
        )
        self.stream_events = to_raw_response_wrapper(
            spaces.stream_events,
        )
        self.stream_logs = to_raw_response_wrapper(
            spaces.stream_logs,
        )
        self.stream_metrics = to_raw_response_wrapper(
            spaces.stream_metrics,
        )
        self.super_squash = to_raw_response_wrapper(
            spaces.super_squash,
        )
        self.update_settings = to_raw_response_wrapper(
            spaces.update_settings,
        )

    @cached_property
    def lfs_files(self) -> LFSFilesResourceWithRawResponse:
        return LFSFilesResourceWithRawResponse(self._spaces.lfs_files)

    @cached_property
    def tag(self) -> TagResourceWithRawResponse:
        return TagResourceWithRawResponse(self._spaces.tag)

    @cached_property
    def branch(self) -> BranchResourceWithRawResponse:
        return BranchResourceWithRawResponse(self._spaces.branch)

    @cached_property
    def resource_group(self) -> ResourceGroupResourceWithRawResponse:
        return ResourceGroupResourceWithRawResponse(self._spaces.resource_group)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._spaces.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithRawResponse:
        return VariablesResourceWithRawResponse(self._spaces.variables)


class AsyncSpacesResourceWithRawResponse:
    def __init__(self, spaces: AsyncSpacesResource) -> None:
        self._spaces = spaces

        self.check_preupload = async_to_raw_response_wrapper(
            spaces.check_preupload,
        )
        self.commit = async_to_raw_response_wrapper(
            spaces.commit,
        )
        self.compare = async_to_raw_response_wrapper(
            spaces.compare,
        )
        self.get_notebook_url = async_to_raw_response_wrapper(
            spaces.get_notebook_url,
        )
        self.get_security_status = async_to_raw_response_wrapper(
            spaces.get_security_status,
        )
        self.get_xet_read_token = async_to_raw_response_wrapper(
            spaces.get_xet_read_token,
        )
        self.get_xet_write_token = async_to_raw_response_wrapper(
            spaces.get_xet_write_token,
        )
        self.list_commits = async_to_raw_response_wrapper(
            spaces.list_commits,
        )
        self.list_paths_info = async_to_raw_response_wrapper(
            spaces.list_paths_info,
        )
        self.list_refs = async_to_raw_response_wrapper(
            spaces.list_refs,
        )
        self.list_tree_content = async_to_raw_response_wrapper(
            spaces.list_tree_content,
        )
        self.stream_events = async_to_raw_response_wrapper(
            spaces.stream_events,
        )
        self.stream_logs = async_to_raw_response_wrapper(
            spaces.stream_logs,
        )
        self.stream_metrics = async_to_raw_response_wrapper(
            spaces.stream_metrics,
        )
        self.super_squash = async_to_raw_response_wrapper(
            spaces.super_squash,
        )
        self.update_settings = async_to_raw_response_wrapper(
            spaces.update_settings,
        )

    @cached_property
    def lfs_files(self) -> AsyncLFSFilesResourceWithRawResponse:
        return AsyncLFSFilesResourceWithRawResponse(self._spaces.lfs_files)

    @cached_property
    def tag(self) -> AsyncTagResourceWithRawResponse:
        return AsyncTagResourceWithRawResponse(self._spaces.tag)

    @cached_property
    def branch(self) -> AsyncBranchResourceWithRawResponse:
        return AsyncBranchResourceWithRawResponse(self._spaces.branch)

    @cached_property
    def resource_group(self) -> AsyncResourceGroupResourceWithRawResponse:
        return AsyncResourceGroupResourceWithRawResponse(self._spaces.resource_group)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._spaces.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithRawResponse:
        return AsyncVariablesResourceWithRawResponse(self._spaces.variables)


class SpacesResourceWithStreamingResponse:
    def __init__(self, spaces: SpacesResource) -> None:
        self._spaces = spaces

        self.check_preupload = to_streamed_response_wrapper(
            spaces.check_preupload,
        )
        self.commit = to_streamed_response_wrapper(
            spaces.commit,
        )
        self.compare = to_streamed_response_wrapper(
            spaces.compare,
        )
        self.get_notebook_url = to_streamed_response_wrapper(
            spaces.get_notebook_url,
        )
        self.get_security_status = to_streamed_response_wrapper(
            spaces.get_security_status,
        )
        self.get_xet_read_token = to_streamed_response_wrapper(
            spaces.get_xet_read_token,
        )
        self.get_xet_write_token = to_streamed_response_wrapper(
            spaces.get_xet_write_token,
        )
        self.list_commits = to_streamed_response_wrapper(
            spaces.list_commits,
        )
        self.list_paths_info = to_streamed_response_wrapper(
            spaces.list_paths_info,
        )
        self.list_refs = to_streamed_response_wrapper(
            spaces.list_refs,
        )
        self.list_tree_content = to_streamed_response_wrapper(
            spaces.list_tree_content,
        )
        self.stream_events = to_streamed_response_wrapper(
            spaces.stream_events,
        )
        self.stream_logs = to_streamed_response_wrapper(
            spaces.stream_logs,
        )
        self.stream_metrics = to_streamed_response_wrapper(
            spaces.stream_metrics,
        )
        self.super_squash = to_streamed_response_wrapper(
            spaces.super_squash,
        )
        self.update_settings = to_streamed_response_wrapper(
            spaces.update_settings,
        )

    @cached_property
    def lfs_files(self) -> LFSFilesResourceWithStreamingResponse:
        return LFSFilesResourceWithStreamingResponse(self._spaces.lfs_files)

    @cached_property
    def tag(self) -> TagResourceWithStreamingResponse:
        return TagResourceWithStreamingResponse(self._spaces.tag)

    @cached_property
    def branch(self) -> BranchResourceWithStreamingResponse:
        return BranchResourceWithStreamingResponse(self._spaces.branch)

    @cached_property
    def resource_group(self) -> ResourceGroupResourceWithStreamingResponse:
        return ResourceGroupResourceWithStreamingResponse(self._spaces.resource_group)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._spaces.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithStreamingResponse:
        return VariablesResourceWithStreamingResponse(self._spaces.variables)


class AsyncSpacesResourceWithStreamingResponse:
    def __init__(self, spaces: AsyncSpacesResource) -> None:
        self._spaces = spaces

        self.check_preupload = async_to_streamed_response_wrapper(
            spaces.check_preupload,
        )
        self.commit = async_to_streamed_response_wrapper(
            spaces.commit,
        )
        self.compare = async_to_streamed_response_wrapper(
            spaces.compare,
        )
        self.get_notebook_url = async_to_streamed_response_wrapper(
            spaces.get_notebook_url,
        )
        self.get_security_status = async_to_streamed_response_wrapper(
            spaces.get_security_status,
        )
        self.get_xet_read_token = async_to_streamed_response_wrapper(
            spaces.get_xet_read_token,
        )
        self.get_xet_write_token = async_to_streamed_response_wrapper(
            spaces.get_xet_write_token,
        )
        self.list_commits = async_to_streamed_response_wrapper(
            spaces.list_commits,
        )
        self.list_paths_info = async_to_streamed_response_wrapper(
            spaces.list_paths_info,
        )
        self.list_refs = async_to_streamed_response_wrapper(
            spaces.list_refs,
        )
        self.list_tree_content = async_to_streamed_response_wrapper(
            spaces.list_tree_content,
        )
        self.stream_events = async_to_streamed_response_wrapper(
            spaces.stream_events,
        )
        self.stream_logs = async_to_streamed_response_wrapper(
            spaces.stream_logs,
        )
        self.stream_metrics = async_to_streamed_response_wrapper(
            spaces.stream_metrics,
        )
        self.super_squash = async_to_streamed_response_wrapper(
            spaces.super_squash,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            spaces.update_settings,
        )

    @cached_property
    def lfs_files(self) -> AsyncLFSFilesResourceWithStreamingResponse:
        return AsyncLFSFilesResourceWithStreamingResponse(self._spaces.lfs_files)

    @cached_property
    def tag(self) -> AsyncTagResourceWithStreamingResponse:
        return AsyncTagResourceWithStreamingResponse(self._spaces.tag)

    @cached_property
    def branch(self) -> AsyncBranchResourceWithStreamingResponse:
        return AsyncBranchResourceWithStreamingResponse(self._spaces.branch)

    @cached_property
    def resource_group(self) -> AsyncResourceGroupResourceWithStreamingResponse:
        return AsyncResourceGroupResourceWithStreamingResponse(self._spaces.resource_group)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._spaces.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithStreamingResponse:
        return AsyncVariablesResourceWithStreamingResponse(self._spaces.variables)
