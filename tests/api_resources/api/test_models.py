# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types.api import (
    ModelCommitResponse,
    ModelListRefsResponse,
    ModelListCommitsResponse,
    ModelSuperSquashResponse,
    ModelListPathsInfoResponse,
    ModelCheckPreuploadResponse,
    ModelGetNotebookURLResponse,
    ModelUpdateSettingsResponse,
    ModelGetXetReadTokenResponse,
    ModelListTreeContentResponse,
    ModelGetXetWriteTokenResponse,
    ModelGetSecurityStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_preupload(self, client: HuggingFace) -> None:
        model = client.api.models.check_preupload(
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
        assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_preupload_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.check_preupload(
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
        assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_preupload(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.check_preupload(
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
        model = response.parse()
        assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_preupload(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.check_preupload(
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

            model = response.parse()
            assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_check_preupload(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.check_preupload(
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
            client.api.models.with_raw_response.check_preupload(
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
            client.api.models.with_raw_response.check_preupload(
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
        model = client.api.models.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelCommitResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_commit_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
            create_pr={},
        )
        assert_matches_type(ModelCommitResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_commit(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelCommitResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_commit(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelCommitResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_commit(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.commit(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.commit(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.commit(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare(self, client: HuggingFace) -> None:
        model = client.api.models.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
            raw={},
        )
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compare(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compare(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(str, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_compare(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.compare(
                compare="compare",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.compare(
                compare="compare",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `compare` but received ''"):
            client.api.models.with_raw_response.compare(
                compare="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_notebook_url(self, client: HuggingFace) -> None:
        model = client.api.models.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ModelGetNotebookURLResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_notebook_url(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelGetNotebookURLResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_notebook_url(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelGetNotebookURLResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_notebook_url(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.get_notebook_url(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.api.models.with_raw_response.get_notebook_url(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_security_status(self, client: HuggingFace) -> None:
        model = client.api.models.get_security_status(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ModelGetSecurityStatusResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_security_status(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.get_security_status(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelGetSecurityStatusResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_security_status(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.get_security_status(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelGetSecurityStatusResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_security_status(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.get_security_status(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.get_security_status(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_xet_read_token(self, client: HuggingFace) -> None:
        model = client.api.models.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelGetXetReadTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_xet_read_token(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelGetXetReadTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_xet_read_token(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelGetXetReadTokenResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_xet_read_token(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.get_xet_read_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_xet_write_token(self, client: HuggingFace) -> None:
        model = client.api.models.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelGetXetWriteTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_xet_write_token(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelGetXetWriteTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_xet_write_token(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelGetXetWriteTokenResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_xet_write_token(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.get_xet_write_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_commits(self, client: HuggingFace) -> None:
        model = client.api.models.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelListCommitsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_commits_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=["formatted"],
            limit=1,
            p=-9007199254740991,
        )
        assert_matches_type(ModelListCommitsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_commits(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListCommitsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_commits(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListCommitsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_commits(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.list_commits(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.list_commits(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.list_commits(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_paths_info(self, client: HuggingFace) -> None:
        model = client.api.models.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )
        assert_matches_type(ModelListPathsInfoResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_paths_info(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListPathsInfoResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_paths_info(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListPathsInfoResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_paths_info(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.list_paths_info(
                rev="rev",
                namespace="",
                repo="repo",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.list_paths_info(
                rev="rev",
                namespace="namespace",
                repo="",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.list_paths_info(
                rev="",
                namespace="namespace",
                repo="repo",
                expand=True,
                paths=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_refs(self, client: HuggingFace) -> None:
        model = client.api.models.list_refs(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ModelListRefsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_refs_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.list_refs(
            repo="repo",
            namespace="namespace",
            include_prs={},
        )
        assert_matches_type(ModelListRefsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_refs(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.list_refs(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListRefsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_refs(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.list_refs(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListRefsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_refs(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.list_refs(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.list_refs(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tree_content(self, client: HuggingFace) -> None:
        model = client.api.models.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tree_content_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            cursor="cursor",
            expand={},
            limit=1,
            recursive={},
        )
        assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_tree_content(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_tree_content(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_tree_content(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.list_tree_content(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.api.models.with_raw_response.list_tree_content(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_super_squash(self, client: HuggingFace) -> None:
        model = client.api.models.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_super_squash_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
            message="message",
        )
        assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_super_squash(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_super_squash(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_super_squash(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.super_squash(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.super_squash(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.models.with_raw_response.super_squash(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: HuggingFace) -> None:
        model = client.api.models.update_settings(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_settings_with_all_params(self, client: HuggingFace) -> None:
        model = client.api.models.update_settings(
            repo="repo",
            namespace="namespace",
            discussions_disabled=True,
            gated="auto",
            gated_notifications_email="dev@stainless.com",
            gated_notifications_mode="bulk",
            private=True,
            xet_enabled=True,
        )
        assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: HuggingFace) -> None:
        response = client.api.models.with_raw_response.update_settings(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: HuggingFace) -> None:
        with client.api.models.with_streaming_response.update_settings(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_settings(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.models.with_raw_response.update_settings(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.models.with_raw_response.update_settings(
                repo="",
                namespace="namespace",
            )


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.check_preupload(
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
        assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_preupload_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.check_preupload(
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
        assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.check_preupload(
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
        model = await response.parse()
        assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.check_preupload(
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

            model = await response.parse()
            assert_matches_type(ModelCheckPreuploadResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_check_preupload(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.check_preupload(
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
            await async_client.api.models.with_raw_response.check_preupload(
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
            await async_client.api.models.with_raw_response.check_preupload(
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
        model = await async_client.api.models.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelCommitResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_commit_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
            create_pr={},
        )
        assert_matches_type(ModelCommitResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_commit(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelCommitResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_commit(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.commit(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelCommitResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_commit(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.commit(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.commit(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.commit(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
            raw={},
        )
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.compare(
            compare="compare",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(str, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_compare(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.compare(
                compare="compare",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.compare(
                compare="compare",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `compare` but received ''"):
            await async_client.api.models.with_raw_response.compare(
                compare="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ModelGetNotebookURLResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelGetNotebookURLResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.get_notebook_url(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelGetNotebookURLResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_notebook_url(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.get_notebook_url(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.get_notebook_url(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.api.models.with_raw_response.get_notebook_url(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.get_security_status(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ModelGetSecurityStatusResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.get_security_status(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelGetSecurityStatusResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.get_security_status(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelGetSecurityStatusResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_security_status(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.get_security_status(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.get_security_status(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelGetXetReadTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelGetXetReadTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.get_xet_read_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelGetXetReadTokenResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_xet_read_token(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.get_xet_read_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.get_xet_read_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelGetXetWriteTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelGetXetWriteTokenResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.get_xet_write_token(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelGetXetWriteTokenResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_xet_write_token(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.get_xet_write_token(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.get_xet_write_token(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_commits(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelListCommitsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_commits_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=["formatted"],
            limit=1,
            p=-9007199254740991,
        )
        assert_matches_type(ModelListCommitsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_commits(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListCommitsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_commits(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.list_commits(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListCommitsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_commits(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.list_commits(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.list_commits(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.list_commits(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )
        assert_matches_type(ModelListPathsInfoResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListPathsInfoResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.list_paths_info(
            rev="rev",
            namespace="namespace",
            repo="repo",
            expand=True,
            paths=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListPathsInfoResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_paths_info(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.list_paths_info(
                rev="rev",
                namespace="",
                repo="repo",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.list_paths_info(
                rev="rev",
                namespace="namespace",
                repo="",
                expand=True,
                paths=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.list_paths_info(
                rev="",
                namespace="namespace",
                repo="repo",
                expand=True,
                paths=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_refs(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.list_refs(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ModelListRefsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_refs_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.list_refs(
            repo="repo",
            namespace="namespace",
            include_prs={},
        )
        assert_matches_type(ModelListRefsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_refs(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.list_refs(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListRefsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_refs(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.list_refs(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListRefsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_refs(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.list_refs(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.list_refs(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tree_content_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            cursor="cursor",
            expand={},
            limit=1,
            recursive={},
        )
        assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.list_tree_content(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListTreeContentResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_tree_content(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.list_tree_content(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.list_tree_content(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.api.models.with_raw_response.list_tree_content(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_super_squash(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_super_squash_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
            message="message",
        )
        assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_super_squash(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_super_squash(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.super_squash(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelSuperSquashResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_super_squash(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.super_squash(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.super_squash(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.models.with_raw_response.super_squash(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.update_settings(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_settings_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        model = await async_client.api.models.update_settings(
            repo="repo",
            namespace="namespace",
            discussions_disabled=True,
            gated="auto",
            gated_notifications_email="dev@stainless.com",
            gated_notifications_mode="bulk",
            private=True,
            xet_enabled=True,
        )
        assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.models.with_raw_response.update_settings(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.models.with_streaming_response.update_settings(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelUpdateSettingsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.models.with_raw_response.update_settings(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.models.with_raw_response.update_settings(
                repo="",
                namespace="namespace",
            )
