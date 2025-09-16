# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.blog.comment import (
    ReplyCreateResponse,
    ReplyCreateWithNamespaceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReply:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        reply = client.api.blog.comment.reply.create(
            comment_id="commentId",
            slug="slug",
            comment="x",
        )
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.blog.comment.reply.with_raw_response.create(
            comment_id="commentId",
            slug="slug",
            comment="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.blog.comment.reply.with_streaming_response.create(
            comment_id="commentId",
            slug="slug",
            comment="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(ReplyCreateResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.blog.comment.reply.with_raw_response.create(
                comment_id="commentId",
                slug="",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.api.blog.comment.reply.with_raw_response.create(
                comment_id="",
                slug="slug",
                comment="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_namespace(self, client: HuggingFace) -> None:
        reply = client.api.blog.comment.reply.create_with_namespace(
            comment_id="commentId",
            namespace="namespace",
            slug="slug",
            comment="x",
        )
        assert_matches_type(ReplyCreateWithNamespaceResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_with_namespace(self, client: HuggingFace) -> None:
        response = client.api.blog.comment.reply.with_raw_response.create_with_namespace(
            comment_id="commentId",
            namespace="namespace",
            slug="slug",
            comment="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(ReplyCreateWithNamespaceResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_with_namespace(self, client: HuggingFace) -> None:
        with client.api.blog.comment.reply.with_streaming_response.create_with_namespace(
            comment_id="commentId",
            namespace="namespace",
            slug="slug",
            comment="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(ReplyCreateWithNamespaceResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_with_namespace(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.blog.comment.reply.with_raw_response.create_with_namespace(
                comment_id="commentId",
                namespace="",
                slug="slug",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.blog.comment.reply.with_raw_response.create_with_namespace(
                comment_id="commentId",
                namespace="namespace",
                slug="",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.api.blog.comment.reply.with_raw_response.create_with_namespace(
                comment_id="",
                namespace="namespace",
                slug="slug",
                comment="x",
            )


class TestAsyncReply:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        reply = await async_client.api.blog.comment.reply.create(
            comment_id="commentId",
            slug="slug",
            comment="x",
        )
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.blog.comment.reply.with_raw_response.create(
            comment_id="commentId",
            slug="slug",
            comment="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.blog.comment.reply.with_streaming_response.create(
            comment_id="commentId",
            slug="slug",
            comment="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(ReplyCreateResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.blog.comment.reply.with_raw_response.create(
                comment_id="commentId",
                slug="",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.api.blog.comment.reply.with_raw_response.create(
                comment_id="",
                slug="slug",
                comment="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_namespace(self, async_client: AsyncHuggingFace) -> None:
        reply = await async_client.api.blog.comment.reply.create_with_namespace(
            comment_id="commentId",
            namespace="namespace",
            slug="slug",
            comment="x",
        )
        assert_matches_type(ReplyCreateWithNamespaceResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_with_namespace(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.blog.comment.reply.with_raw_response.create_with_namespace(
            comment_id="commentId",
            namespace="namespace",
            slug="slug",
            comment="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(ReplyCreateWithNamespaceResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_with_namespace(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.blog.comment.reply.with_streaming_response.create_with_namespace(
            comment_id="commentId",
            namespace="namespace",
            slug="slug",
            comment="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(ReplyCreateWithNamespaceResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_with_namespace(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.blog.comment.reply.with_raw_response.create_with_namespace(
                comment_id="commentId",
                namespace="",
                slug="slug",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.blog.comment.reply.with_raw_response.create_with_namespace(
                comment_id="commentId",
                namespace="namespace",
                slug="",
                comment="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.api.blog.comment.reply.with_raw_response.create_with_namespace(
                comment_id="",
                namespace="namespace",
                slug="slug",
                comment="x",
            )
