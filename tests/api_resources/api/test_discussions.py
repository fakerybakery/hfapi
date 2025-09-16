# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi._utils import parse_datetime
from pyhfapi.types.api import (
    DiscussionListResponse,
    DiscussionCreateResponse,
    DiscussionRetrieveResponse,
    DiscussionAddCommentResponse,
    DiscussionChangeTitleResponse,
    DiscussionChangeStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiscussions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
        )
        assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
            pull_request=True,
        )
        assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.create(
                repo="repo",
                repo_type="models",
                namespace="",
                description="description",
                title="xxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.create(
                repo="",
                repo_type="models",
                namespace="namespace",
                description="description",
                title="xxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.retrieve(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(DiscussionRetrieveResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.retrieve(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert_matches_type(DiscussionRetrieveResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.retrieve(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert_matches_type(DiscussionRetrieveResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.retrieve(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.retrieve(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            client.api.discussions.with_raw_response.retrieve(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
        )
        assert_matches_type(DiscussionListResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            author="author",
            p=-9007199254740991,
            search="search",
            sort="recently-created",
            status="all",
            type="all",
        )
        assert_matches_type(DiscussionListResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert_matches_type(DiscussionListResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert_matches_type(DiscussionListResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.list(
                repo="repo",
                repo_type="models",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.list(
                repo="",
                repo_type="models",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.delete(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.delete(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.delete(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.delete(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.delete(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            client.api.discussions.with_raw_response.delete(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_comment(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.add_comment(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="x",
        )
        assert_matches_type(DiscussionAddCommentResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_comment(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.add_comment(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert_matches_type(DiscussionAddCommentResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_comment(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.add_comment(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert_matches_type(DiscussionAddCommentResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_comment(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.add_comment(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.add_comment(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            client.api.discussions.with_raw_response.add_comment(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                comment="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_status(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
        )
        assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_status_with_all_params(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
            comment="comment",
        )
        assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_change_status(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_change_status(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_change_status(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.change_status(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                status="open",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.change_status(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                status="open",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            client.api.discussions.with_raw_response.change_status(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                status="open",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_title(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.change_title(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            title="xxx",
        )
        assert_matches_type(DiscussionChangeTitleResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_change_title(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.change_title(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            title="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert_matches_type(DiscussionChangeTitleResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_change_title(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.change_title(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            title="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert_matches_type(DiscussionChangeTitleResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_change_title(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.change_title(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                title="xxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.change_title(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                title="xxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            client.api.discussions.with_raw_response.change_title(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                title="xxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mark_as_read(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.mark_as_read()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mark_as_read_with_all_params(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.mark_as_read(
            apply_to_all={},
            article_id="articleId",
            last_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mention="all",
            p=0,
            paper_id="paperId",
            post_author="postAuthor",
            read_status="all",
            repo_name="repoName",
            repo_type="dataset",
            discussion_ids=["string"],
            read=True,
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_mark_as_read(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.mark_as_read()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_mark_as_read(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.mark_as_read() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_merge(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_merge_with_all_params(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="comment",
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_merge(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_merge(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_merge(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.merge(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.merge(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            client.api.discussions.with_raw_response.merge(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pin(self, client: HuggingFace) -> None:
        discussion = client.api.discussions.pin(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            pinned=True,
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_pin(self, client: HuggingFace) -> None:
        response = client.api.discussions.with_raw_response.pin(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            pinned=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_pin(self, client: HuggingFace) -> None:
        with client.api.discussions.with_streaming_response.pin(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            pinned=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_pin(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.discussions.with_raw_response.pin(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                pinned=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.discussions.with_raw_response.pin(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                pinned=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            client.api.discussions.with_raw_response.pin(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                pinned=True,
            )


class TestAsyncDiscussions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
        )
        assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
            pull_request=True,
        )
        assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.create(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            description="description",
            title="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert_matches_type(DiscussionCreateResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.create(
                repo="repo",
                repo_type="models",
                namespace="",
                description="description",
                title="xxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.create(
                repo="",
                repo_type="models",
                namespace="namespace",
                description="description",
                title="xxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.retrieve(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(DiscussionRetrieveResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.retrieve(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert_matches_type(DiscussionRetrieveResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.retrieve(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert_matches_type(DiscussionRetrieveResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.retrieve(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.retrieve(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            await async_client.api.discussions.with_raw_response.retrieve(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
        )
        assert_matches_type(DiscussionListResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
            author="author",
            p=-9007199254740991,
            search="search",
            sort="recently-created",
            status="all",
            type="all",
        )
        assert_matches_type(DiscussionListResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert_matches_type(DiscussionListResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.list(
            repo="repo",
            repo_type="models",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert_matches_type(DiscussionListResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.list(
                repo="repo",
                repo_type="models",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.list(
                repo="",
                repo_type="models",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.delete(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.delete(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.delete(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.delete(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.delete(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            await async_client.api.discussions.with_raw_response.delete(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_comment(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.add_comment(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="x",
        )
        assert_matches_type(DiscussionAddCommentResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_comment(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.add_comment(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert_matches_type(DiscussionAddCommentResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_comment(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.add_comment(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert_matches_type(DiscussionAddCommentResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_comment(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.add_comment(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.add_comment(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            await async_client.api.discussions.with_raw_response.add_comment(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                comment="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_status(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
        )
        assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_status_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
            comment="comment",
        )
        assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_change_status(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_change_status(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.change_status(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            status="open",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert_matches_type(DiscussionChangeStatusResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_change_status(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.change_status(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                status="open",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.change_status(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                status="open",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            await async_client.api.discussions.with_raw_response.change_status(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                status="open",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_title(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.change_title(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            title="xxx",
        )
        assert_matches_type(DiscussionChangeTitleResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_change_title(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.change_title(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            title="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert_matches_type(DiscussionChangeTitleResponse, discussion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_change_title(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.change_title(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            title="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert_matches_type(DiscussionChangeTitleResponse, discussion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_change_title(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.change_title(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                title="xxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.change_title(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                title="xxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            await async_client.api.discussions.with_raw_response.change_title(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                title="xxx",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mark_as_read(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.mark_as_read()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mark_as_read_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.mark_as_read(
            apply_to_all={},
            article_id="articleId",
            last_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mention="all",
            p=0,
            paper_id="paperId",
            post_author="postAuthor",
            read_status="all",
            repo_name="repoName",
            repo_type="dataset",
            discussion_ids=["string"],
            read=True,
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_mark_as_read(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.mark_as_read()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_mark_as_read(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.mark_as_read() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_merge(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_merge_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            comment="comment",
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.merge(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_merge(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.merge(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.merge(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            await async_client.api.discussions.with_raw_response.merge(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pin(self, async_client: AsyncHuggingFace) -> None:
        discussion = await async_client.api.discussions.pin(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            pinned=True,
        )
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_pin(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.discussions.with_raw_response.pin(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            pinned=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discussion = await response.parse()
        assert discussion is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_pin(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.discussions.with_streaming_response.pin(
            num="num",
            repo_type="models",
            namespace="namespace",
            repo="repo",
            pinned=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discussion = await response.parse()
            assert discussion is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_pin(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.discussions.with_raw_response.pin(
                num="num",
                repo_type="models",
                namespace="",
                repo="repo",
                pinned=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.discussions.with_raw_response.pin(
                num="num",
                repo_type="models",
                namespace="namespace",
                repo="",
                pinned=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `num` but received ''"):
            await async_client.api.discussions.with_raw_response.pin(
                num="",
                repo_type="models",
                namespace="namespace",
                repo="repo",
                pinned=True,
            )
