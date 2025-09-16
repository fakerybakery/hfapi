# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types.api import (
    SpaceCommitResponse,
    SpaceListRefsResponse,
    SpaceListCommitsResponse,
    SpaceSuperSquashResponse,
    SpaceListPathsInfoResponse,
    SpaceCheckPreuploadResponse,
    SpaceGetNotebookURLResponse,
    SpaceUpdateSettingsResponse,
    SpaceGetXetReadTokenResponse,
    SpaceListTreeContentResponse,
    SpaceGetXetWriteTokenResponse,
    SpaceGetSecurityStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_preupload(self, client: HuggingFace) -> None:
        space = client.api.spaces.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
        )
        assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_preupload_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
            git_attributes="gitAttributes",
            git_ignore="gitIgnore",
        )
        assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_preupload(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_preupload(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_check_preupload(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.check_preupload(
                rev="rev",
                namespace="",
                repo="repo",
                files=[
                    {
                        "path": "path",
                        "sample": "sample",
                        "size": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.check_preupload(
                rev="rev",
                namespace="namespace",
                repo="",
                files=[
                    {
                        "path": "path",
                        "sample": "sample",
                        "size": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.check_preupload(
                rev="",
                namespace="namespace",
                repo="repo",
                files=[
                    {
                        "path": "path",
                        "sample": "sample",
                        "size": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_commit(self, client: HuggingFace) -> None:
        space = client.api.spaces.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceCommitResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_commit_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
            create_pr={},
        )
        assert_matches_type(SpaceCommitResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_commit(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceCommitResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_commit(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceCommitResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_commit(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.commit(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.commit(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.commit(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare(self, client: HuggingFace) -> None:
        space = client.api.spaces.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(str, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
            raw={},
        )
        assert_matches_type(str, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compare(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(str, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compare(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(str, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_compare(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.compare(
                compare="compare",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.compare(
                compare="compare",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `compare` but received ''"):
            client.api.spaces.with_raw_response.compare(
                compare="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_notebook_url(self, client: HuggingFace) -> None:
        space = client.api.spaces.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(SpaceGetNotebookURLResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_notebook_url(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceGetNotebookURLResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_notebook_url(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceGetNotebookURLResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_notebook_url(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.get_notebook_url(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.api.spaces.with_raw_response.get_notebook_url(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_security_status(self, client: HuggingFace) -> None:
        space = client.api.spaces.get_security_status(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(SpaceGetSecurityStatusResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_security_status(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.get_security_status(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceGetSecurityStatusResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_security_status(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.get_security_status(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceGetSecurityStatusResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_security_status(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.get_security_status(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.get_security_status(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_xet_read_token(self, client: HuggingFace) -> None:
        space = client.api.spaces.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceGetXetReadTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_xet_read_token(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceGetXetReadTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_xet_read_token(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceGetXetReadTokenResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_xet_read_token(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.get_xet_read_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_xet_write_token(self, client: HuggingFace) -> None:
        space = client.api.spaces.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceGetXetWriteTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_xet_write_token(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceGetXetWriteTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_xet_write_token(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceGetXetWriteTokenResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_xet_write_token(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.get_xet_write_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_commits(self, client: HuggingFace) -> None:
        space = client.api.spaces.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_commits_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=["formatted"],
            limit=1,
            p=-9007199254740991,
        )
        assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_commits(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_commits(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_commits(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.list_commits(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.list_commits(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.list_commits(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_paths_info(self, client: HuggingFace) -> None:
        space = client.api.spaces.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )
        assert_matches_type(SpaceListPathsInfoResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_paths_info(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceListPathsInfoResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_paths_info(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceListPathsInfoResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_paths_info(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.list_paths_info(
                rev="rev",
                namespace="",
                repo="repo",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.list_paths_info(
                rev="rev",
                namespace="namespace",
                repo="",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.list_paths_info(
                rev="",
                namespace="namespace",
                repo="repo",
                expand=True,
                paths=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_refs(self, client: HuggingFace) -> None:
        space = client.api.spaces.list_refs(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(SpaceListRefsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_refs_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.list_refs(
            repo="repo",
            namespace="namespace",
            include_prs={},
        )
        assert_matches_type(SpaceListRefsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_refs(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.list_refs(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceListRefsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_refs(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.list_refs(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceListRefsResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_refs(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.list_refs(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.list_refs(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tree_content(self, client: HuggingFace) -> None:
        space = client.api.spaces.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tree_content_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            cursor="cursor",
            expand={},
            limit=1,
            recursive={},
        )
        assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_tree_content(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_tree_content(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_tree_content(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.list_tree_content(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.api.spaces.with_raw_response.list_tree_content(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_events(self, client: HuggingFace) -> None:
        space = client.api.spaces.stream_events(
            repo="repo",
            namespace="namespace",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_events_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.stream_events(
            repo="repo",
            namespace="namespace",
            session_uuid="session_uuid",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_events(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.stream_events(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_events(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.stream_events(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert space is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_events(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.stream_events(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.stream_events(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_logs(self, client: HuggingFace) -> None:
        space = client.api.spaces.stream_logs(
            log_type="build",
            namespace="namespace",
            repo="repo",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_logs(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.stream_logs(
            log_type="build",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_logs(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.stream_logs(
            log_type="build",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert space is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_logs(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.stream_logs(
                log_type="build",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.stream_logs(
                log_type="build",
                namespace="namespace",
                repo="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_metrics(self, client: HuggingFace) -> None:
        space = client.api.spaces.stream_metrics(
            repo="repo",
            namespace="namespace",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_metrics(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.stream_metrics(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_metrics(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.stream_metrics(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert space is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_metrics(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.stream_metrics(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.stream_metrics(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_super_squash(self, client: HuggingFace) -> None:
        space = client.api.spaces.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_super_squash_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
            message="message",
        )
        assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_super_squash(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_super_squash(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_super_squash(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.super_squash(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.super_squash(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.spaces.with_raw_response.super_squash(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: HuggingFace) -> None:
        space = client.api.spaces.update_settings(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_settings_with_all_params(self, client: HuggingFace) -> None:
        space = client.api.spaces.update_settings(
            repo="repo",
            namespace="namespace",
            discussions_disabled=True,
            gated="auto",
            gated_notifications_email="dev@stainless.com",
            gated_notifications_mode="bulk",
            private=True,
            xet_enabled=True,
        )
        assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: HuggingFace) -> None:
        response = client.api.spaces.with_raw_response.update_settings(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: HuggingFace) -> None:
        with client.api.spaces.with_streaming_response.update_settings(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_settings(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.with_raw_response.update_settings(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.with_raw_response.update_settings(
                repo="",
                namespace="namespace",
            )


class TestAsyncSpaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
        )
        assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_preupload_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
            git_attributes="gitAttributes",
            git_ignore="gitIgnore",
        )
        assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.check_preupload(
            rev="rev",
            namespace="namespace",
            repo="repo",
            files=[
                {
                    "path": "path",
                    "sample": "sample",
                    "size": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceCheckPreuploadResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.check_preupload(
                rev="rev",
                namespace="",
                repo="repo",
                files=[
                    {
                        "path": "path",
                        "sample": "sample",
                        "size": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.check_preupload(
                rev="rev",
                namespace="namespace",
                repo="",
                files=[
                    {
                        "path": "path",
                        "sample": "sample",
                        "size": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.check_preupload(
                rev="",
                namespace="namespace",
                repo="repo",
                files=[
                    {
                        "path": "path",
                        "sample": "sample",
                        "size": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_commit(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceCommitResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_commit_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
            create_pr={},
        )
        assert_matches_type(SpaceCommitResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_commit(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceCommitResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_commit(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceCommitResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_commit(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.commit(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.commit(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.commit(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(str, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
            raw={},
        )
        assert_matches_type(str, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(str, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(str, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_compare(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.compare(
                compare="compare",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.compare(
                compare="compare",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `compare` but received ''"):
            await async_client.api.spaces.with_raw_response.compare(
                compare="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(SpaceGetNotebookURLResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceGetNotebookURLResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceGetNotebookURLResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.get_notebook_url(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.api.spaces.with_raw_response.get_notebook_url(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.get_security_status(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(SpaceGetSecurityStatusResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.get_security_status(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceGetSecurityStatusResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.get_security_status(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceGetSecurityStatusResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.get_security_status(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.get_security_status(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceGetXetReadTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceGetXetReadTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceGetXetReadTokenResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.get_xet_read_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceGetXetWriteTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceGetXetWriteTokenResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceGetXetWriteTokenResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.get_xet_write_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_commits(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_commits_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=["formatted"],
            limit=1,
            p=-9007199254740991,
        )
        assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_commits(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_commits(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceListCommitsResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_commits(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.list_commits(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.list_commits(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.list_commits(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )
        assert_matches_type(SpaceListPathsInfoResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceListPathsInfoResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceListPathsInfoResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.list_paths_info(
                rev="rev",
                namespace="",
                repo="repo",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.list_paths_info(
                rev="rev",
                namespace="namespace",
                repo="",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.list_paths_info(
                rev="",
                namespace="namespace",
                repo="repo",
                expand=True,
                paths=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_refs(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.list_refs(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(SpaceListRefsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_refs_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.list_refs(
            repo="repo",
            namespace="namespace",
            include_prs={},
        )
        assert_matches_type(SpaceListRefsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_refs(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.list_refs(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceListRefsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_refs(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.list_refs(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceListRefsResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_refs(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.list_refs(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.list_refs(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tree_content_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            cursor="cursor",
            expand={},
            limit=1,
            recursive={},
        )
        assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceListTreeContentResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.list_tree_content(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.api.spaces.with_raw_response.list_tree_content(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.stream_events(
            repo="repo",
            namespace="namespace",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_events_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.stream_events(
            repo="repo",
            namespace="namespace",
            session_uuid="session_uuid",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.stream_events(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.stream_events(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert space is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.stream_events(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.stream_events(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.stream_logs(
            log_type="build",
            namespace="namespace",
            repo="repo",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.stream_logs(
            log_type="build",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.stream_logs(
            log_type="build",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert space is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.stream_logs(
                log_type="build",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.stream_logs(
                log_type="build",
                namespace="namespace",
                repo="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.stream_metrics(
            repo="repo",
            namespace="namespace",
        )
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.stream_metrics(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert space is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.stream_metrics(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert space is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.stream_metrics(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.stream_metrics(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_super_squash(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_super_squash_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
            message="message",
        )
        assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_super_squash(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_super_squash(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceSuperSquashResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_super_squash(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.super_squash(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.super_squash(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.spaces.with_raw_response.super_squash(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.update_settings(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_settings_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        space = await async_client.api.spaces.update_settings(
            repo="repo",
            namespace="namespace",
            discussions_disabled=True,
            gated="auto",
            gated_notifications_email="dev@stainless.com",
            gated_notifications_mode="bulk",
            private=True,
            xet_enabled=True,
        )
        assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.with_raw_response.update_settings(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.with_streaming_response.update_settings(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceUpdateSettingsResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.with_raw_response.update_settings(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.with_raw_response.update_settings(
                repo="",
                namespace="namespace",
            )
