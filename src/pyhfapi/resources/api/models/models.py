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
    model_commit_params,
    model_compare_params,
    model_list_refs_params,
    model_list_commits_params,
    model_super_squash_params,
    model_check_preupload_params,
    model_list_paths_info_params,
    model_update_settings_params,
    model_list_tree_content_params,
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
from ....types.api.model_commit_response import ModelCommitResponse
from ....types.api.model_list_refs_response import ModelListRefsResponse
from ....types.api.model_list_commits_response import ModelListCommitsResponse
from ....types.api.model_super_squash_response import ModelSuperSquashResponse
from ....types.api.model_check_preupload_response import ModelCheckPreuploadResponse
from ....types.api.model_list_paths_info_response import ModelListPathsInfoResponse
from ....types.api.model_update_settings_response import ModelUpdateSettingsResponse
from ....types.api.model_get_notebook_url_response import ModelGetNotebookURLResponse
from ....types.api.model_list_tree_content_response import ModelListTreeContentResponse
from ....types.api.model_get_xet_read_token_response import ModelGetXetReadTokenResponse
from ....types.api.model_get_security_status_response import ModelGetSecurityStatusResponse
from ....types.api.model_get_xet_write_token_response import ModelGetXetWriteTokenResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
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
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)

    def check_preupload(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        files: Iterable[model_check_preupload_params.File],
        git_attributes: str | NotGiven = NOT_GIVEN,
        git_ignore: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelCheckPreuploadResponse:
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
            f"/api/models/{namespace}/{repo}/preupload/{rev}",
            body=maybe_transform(
                {
                    "files": files,
                    "git_attributes": git_attributes,
                    "git_ignore": git_ignore,
                },
                model_check_preupload_params.ModelCheckPreuploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelCheckPreuploadResponse,
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
    ) -> ModelCommitResponse:
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
            f"/api/models/{namespace}/{repo}/commit/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"create_pr": create_pr}, model_commit_params.ModelCommitParams),
            ),
            cast_to=ModelCommitResponse,
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
            f"/api/models/{namespace}/{repo}/compare/{compare}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"raw": raw}, model_compare_params.ModelCompareParams),
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
    ) -> ModelGetNotebookURLResponse:
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
            ModelGetNotebookURLResponse,
            self._get(
                f"/api/models/{namespace}/{repo}/notebook/{rev}/{path}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelGetNotebookURLResponse
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
    ) -> ModelGetSecurityStatusResponse:
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
            f"/api/models/{namespace}/{repo}/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetSecurityStatusResponse,
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
    ) -> ModelGetXetReadTokenResponse:
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
            f"/api/models/{namespace}/{repo}/xet-read-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetXetReadTokenResponse,
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
    ) -> ModelGetXetWriteTokenResponse:
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
            f"/api/models/{namespace}/{repo}/xet-write-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetXetWriteTokenResponse,
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
    ) -> ModelListCommitsResponse:
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
            f"/api/models/{namespace}/{repo}/commits/{rev}",
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
                    model_list_commits_params.ModelListCommitsParams,
                ),
            ),
            cast_to=ModelListCommitsResponse,
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
    ) -> ModelListPathsInfoResponse:
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
            f"/api/models/{namespace}/{repo}/paths-info/{rev}",
            body=maybe_transform(
                {
                    "expand": expand,
                    "paths": paths,
                },
                model_list_paths_info_params.ModelListPathsInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelListPathsInfoResponse,
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
    ) -> ModelListRefsResponse:
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
            f"/api/models/{namespace}/{repo}/refs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_prs": include_prs}, model_list_refs_params.ModelListRefsParams),
            ),
            cast_to=ModelListRefsResponse,
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
    ) -> ModelListTreeContentResponse:
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
            f"/api/models/{namespace}/{repo}/tree/{rev}/{path}",
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
                    model_list_tree_content_params.ModelListTreeContentParams,
                ),
            ),
            cast_to=ModelListTreeContentResponse,
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
    ) -> ModelSuperSquashResponse:
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
            f"/api/models/{namespace}/{repo}/super-squash/{rev}",
            body=maybe_transform({"message": message}, model_super_squash_params.ModelSuperSquashParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelSuperSquashResponse,
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
    ) -> ModelUpdateSettingsResponse:
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
            f"/api/models/{namespace}/{repo}/settings",
            body=maybe_transform(
                {
                    "discussions_disabled": discussions_disabled,
                    "gated": gated,
                    "gated_notifications_email": gated_notifications_email,
                    "gated_notifications_mode": gated_notifications_mode,
                    "private": private,
                    "xet_enabled": xet_enabled,
                },
                model_update_settings_params.ModelUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelUpdateSettingsResponse,
        )


class AsyncModelsResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)

    async def check_preupload(
        self,
        rev: str,
        *,
        namespace: str,
        repo: str,
        files: Iterable[model_check_preupload_params.File],
        git_attributes: str | NotGiven = NOT_GIVEN,
        git_ignore: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelCheckPreuploadResponse:
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
            f"/api/models/{namespace}/{repo}/preupload/{rev}",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "git_attributes": git_attributes,
                    "git_ignore": git_ignore,
                },
                model_check_preupload_params.ModelCheckPreuploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelCheckPreuploadResponse,
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
    ) -> ModelCommitResponse:
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
            f"/api/models/{namespace}/{repo}/commit/{rev}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"create_pr": create_pr}, model_commit_params.ModelCommitParams),
            ),
            cast_to=ModelCommitResponse,
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
            f"/api/models/{namespace}/{repo}/compare/{compare}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"raw": raw}, model_compare_params.ModelCompareParams),
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
    ) -> ModelGetNotebookURLResponse:
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
            ModelGetNotebookURLResponse,
            await self._get(
                f"/api/models/{namespace}/{repo}/notebook/{rev}/{path}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelGetNotebookURLResponse
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
    ) -> ModelGetSecurityStatusResponse:
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
            f"/api/models/{namespace}/{repo}/scan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetSecurityStatusResponse,
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
    ) -> ModelGetXetReadTokenResponse:
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
            f"/api/models/{namespace}/{repo}/xet-read-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetXetReadTokenResponse,
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
    ) -> ModelGetXetWriteTokenResponse:
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
            f"/api/models/{namespace}/{repo}/xet-write-token/{rev}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetXetWriteTokenResponse,
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
    ) -> ModelListCommitsResponse:
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
            f"/api/models/{namespace}/{repo}/commits/{rev}",
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
                    model_list_commits_params.ModelListCommitsParams,
                ),
            ),
            cast_to=ModelListCommitsResponse,
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
    ) -> ModelListPathsInfoResponse:
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
            f"/api/models/{namespace}/{repo}/paths-info/{rev}",
            body=await async_maybe_transform(
                {
                    "expand": expand,
                    "paths": paths,
                },
                model_list_paths_info_params.ModelListPathsInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelListPathsInfoResponse,
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
    ) -> ModelListRefsResponse:
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
            f"/api/models/{namespace}/{repo}/refs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_prs": include_prs}, model_list_refs_params.ModelListRefsParams
                ),
            ),
            cast_to=ModelListRefsResponse,
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
    ) -> ModelListTreeContentResponse:
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
            f"/api/models/{namespace}/{repo}/tree/{rev}/{path}",
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
                    model_list_tree_content_params.ModelListTreeContentParams,
                ),
            ),
            cast_to=ModelListTreeContentResponse,
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
    ) -> ModelSuperSquashResponse:
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
            f"/api/models/{namespace}/{repo}/super-squash/{rev}",
            body=await async_maybe_transform({"message": message}, model_super_squash_params.ModelSuperSquashParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelSuperSquashResponse,
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
    ) -> ModelUpdateSettingsResponse:
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
            f"/api/models/{namespace}/{repo}/settings",
            body=await async_maybe_transform(
                {
                    "discussions_disabled": discussions_disabled,
                    "gated": gated,
                    "gated_notifications_email": gated_notifications_email,
                    "gated_notifications_mode": gated_notifications_mode,
                    "private": private,
                    "xet_enabled": xet_enabled,
                },
                model_update_settings_params.ModelUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelUpdateSettingsResponse,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.check_preupload = to_raw_response_wrapper(
            models.check_preupload,
        )
        self.commit = to_raw_response_wrapper(
            models.commit,
        )
        self.compare = to_raw_response_wrapper(
            models.compare,
        )
        self.get_notebook_url = to_raw_response_wrapper(
            models.get_notebook_url,
        )
        self.get_security_status = to_raw_response_wrapper(
            models.get_security_status,
        )
        self.get_xet_read_token = to_raw_response_wrapper(
            models.get_xet_read_token,
        )
        self.get_xet_write_token = to_raw_response_wrapper(
            models.get_xet_write_token,
        )
        self.list_commits = to_raw_response_wrapper(
            models.list_commits,
        )
        self.list_paths_info = to_raw_response_wrapper(
            models.list_paths_info,
        )
        self.list_refs = to_raw_response_wrapper(
            models.list_refs,
        )
        self.list_tree_content = to_raw_response_wrapper(
            models.list_tree_content,
        )
        self.super_squash = to_raw_response_wrapper(
            models.super_squash,
        )
        self.update_settings = to_raw_response_wrapper(
            models.update_settings,
        )

    @cached_property
    def lfs_files(self) -> LFSFilesResourceWithRawResponse:
        return LFSFilesResourceWithRawResponse(self._models.lfs_files)

    @cached_property
    def tag(self) -> TagResourceWithRawResponse:
        return TagResourceWithRawResponse(self._models.tag)

    @cached_property
    def branch(self) -> BranchResourceWithRawResponse:
        return BranchResourceWithRawResponse(self._models.branch)

    @cached_property
    def resource_group(self) -> ResourceGroupResourceWithRawResponse:
        return ResourceGroupResourceWithRawResponse(self._models.resource_group)

    @cached_property
    def user_access_request(self) -> UserAccessRequestResourceWithRawResponse:
        return UserAccessRequestResourceWithRawResponse(self._models.user_access_request)


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.check_preupload = async_to_raw_response_wrapper(
            models.check_preupload,
        )
        self.commit = async_to_raw_response_wrapper(
            models.commit,
        )
        self.compare = async_to_raw_response_wrapper(
            models.compare,
        )
        self.get_notebook_url = async_to_raw_response_wrapper(
            models.get_notebook_url,
        )
        self.get_security_status = async_to_raw_response_wrapper(
            models.get_security_status,
        )
        self.get_xet_read_token = async_to_raw_response_wrapper(
            models.get_xet_read_token,
        )
        self.get_xet_write_token = async_to_raw_response_wrapper(
            models.get_xet_write_token,
        )
        self.list_commits = async_to_raw_response_wrapper(
            models.list_commits,
        )
        self.list_paths_info = async_to_raw_response_wrapper(
            models.list_paths_info,
        )
        self.list_refs = async_to_raw_response_wrapper(
            models.list_refs,
        )
        self.list_tree_content = async_to_raw_response_wrapper(
            models.list_tree_content,
        )
        self.super_squash = async_to_raw_response_wrapper(
            models.super_squash,
        )
        self.update_settings = async_to_raw_response_wrapper(
            models.update_settings,
        )

    @cached_property
    def lfs_files(self) -> AsyncLFSFilesResourceWithRawResponse:
        return AsyncLFSFilesResourceWithRawResponse(self._models.lfs_files)

    @cached_property
    def tag(self) -> AsyncTagResourceWithRawResponse:
        return AsyncTagResourceWithRawResponse(self._models.tag)

    @cached_property
    def branch(self) -> AsyncBranchResourceWithRawResponse:
        return AsyncBranchResourceWithRawResponse(self._models.branch)

    @cached_property
    def resource_group(self) -> AsyncResourceGroupResourceWithRawResponse:
        return AsyncResourceGroupResourceWithRawResponse(self._models.resource_group)

    @cached_property
    def user_access_request(self) -> AsyncUserAccessRequestResourceWithRawResponse:
        return AsyncUserAccessRequestResourceWithRawResponse(self._models.user_access_request)


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.check_preupload = to_streamed_response_wrapper(
            models.check_preupload,
        )
        self.commit = to_streamed_response_wrapper(
            models.commit,
        )
        self.compare = to_streamed_response_wrapper(
            models.compare,
        )
        self.get_notebook_url = to_streamed_response_wrapper(
            models.get_notebook_url,
        )
        self.get_security_status = to_streamed_response_wrapper(
            models.get_security_status,
        )
        self.get_xet_read_token = to_streamed_response_wrapper(
            models.get_xet_read_token,
        )
        self.get_xet_write_token = to_streamed_response_wrapper(
            models.get_xet_write_token,
        )
        self.list_commits = to_streamed_response_wrapper(
            models.list_commits,
        )
        self.list_paths_info = to_streamed_response_wrapper(
            models.list_paths_info,
        )
        self.list_refs = to_streamed_response_wrapper(
            models.list_refs,
        )
        self.list_tree_content = to_streamed_response_wrapper(
            models.list_tree_content,
        )
        self.super_squash = to_streamed_response_wrapper(
            models.super_squash,
        )
        self.update_settings = to_streamed_response_wrapper(
            models.update_settings,
        )

    @cached_property
    def lfs_files(self) -> LFSFilesResourceWithStreamingResponse:
        return LFSFilesResourceWithStreamingResponse(self._models.lfs_files)

    @cached_property
    def tag(self) -> TagResourceWithStreamingResponse:
        return TagResourceWithStreamingResponse(self._models.tag)

    @cached_property
    def branch(self) -> BranchResourceWithStreamingResponse:
        return BranchResourceWithStreamingResponse(self._models.branch)

    @cached_property
    def resource_group(self) -> ResourceGroupResourceWithStreamingResponse:
        return ResourceGroupResourceWithStreamingResponse(self._models.resource_group)

    @cached_property
    def user_access_request(self) -> UserAccessRequestResourceWithStreamingResponse:
        return UserAccessRequestResourceWithStreamingResponse(self._models.user_access_request)


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.check_preupload = async_to_streamed_response_wrapper(
            models.check_preupload,
        )
        self.commit = async_to_streamed_response_wrapper(
            models.commit,
        )
        self.compare = async_to_streamed_response_wrapper(
            models.compare,
        )
        self.get_notebook_url = async_to_streamed_response_wrapper(
            models.get_notebook_url,
        )
        self.get_security_status = async_to_streamed_response_wrapper(
            models.get_security_status,
        )
        self.get_xet_read_token = async_to_streamed_response_wrapper(
            models.get_xet_read_token,
        )
        self.get_xet_write_token = async_to_streamed_response_wrapper(
            models.get_xet_write_token,
        )
        self.list_commits = async_to_streamed_response_wrapper(
            models.list_commits,
        )
        self.list_paths_info = async_to_streamed_response_wrapper(
            models.list_paths_info,
        )
        self.list_refs = async_to_streamed_response_wrapper(
            models.list_refs,
        )
        self.list_tree_content = async_to_streamed_response_wrapper(
            models.list_tree_content,
        )
        self.super_squash = async_to_streamed_response_wrapper(
            models.super_squash,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            models.update_settings,
        )

    @cached_property
    def lfs_files(self) -> AsyncLFSFilesResourceWithStreamingResponse:
        return AsyncLFSFilesResourceWithStreamingResponse(self._models.lfs_files)

    @cached_property
    def tag(self) -> AsyncTagResourceWithStreamingResponse:
        return AsyncTagResourceWithStreamingResponse(self._models.tag)

    @cached_property
    def branch(self) -> AsyncBranchResourceWithStreamingResponse:
        return AsyncBranchResourceWithStreamingResponse(self._models.branch)

    @cached_property
    def resource_group(self) -> AsyncResourceGroupResourceWithStreamingResponse:
        return AsyncResourceGroupResourceWithStreamingResponse(self._models.resource_group)

    @cached_property
    def user_access_request(self) -> AsyncUserAccessRequestResourceWithStreamingResponse:
        return AsyncUserAccessRequestResourceWithStreamingResponse(self._models.user_access_request)
