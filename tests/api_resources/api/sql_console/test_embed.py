# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.sql_console import (
    EmbedCreateResponse,
    EmbedUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        embed = client.api.sql_console.embed.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        embed = client.api.sql_console.embed.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
            private=True,
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.sql_console.embed.with_raw_response.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = response.parse()
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.sql_console.embed.with_streaming_response.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = response.parse()
            assert_matches_type(EmbedCreateResponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.sql_console.embed.with_raw_response.create(
                repo="repo",
                repo_type="datasets",
                namespace="",
                sql="sql",
                title="title",
                views=[
                    {
                        "display_name": "displayName",
                        "key": "key",
                        "view_name": "viewName",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.sql_console.embed.with_raw_response.create(
                repo="",
                repo_type="datasets",
                namespace="namespace",
                sql="sql",
                title="title",
                views=[
                    {
                        "display_name": "displayName",
                        "key": "key",
                        "view_name": "viewName",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HuggingFace) -> None:
        embed = client.api.sql_console.embed.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HuggingFace) -> None:
        embed = client.api.sql_console.embed.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
            private=True,
            sql="sql",
            title="title",
        )
        assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HuggingFace) -> None:
        response = client.api.sql_console.embed.with_raw_response.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = response.parse()
        assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HuggingFace) -> None:
        with client.api.sql_console.embed.with_streaming_response.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = response.parse()
            assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.sql_console.embed.with_raw_response.update(
                id="id",
                repo_type="datasets",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.sql_console.embed.with_raw_response.update(
                id="id",
                repo_type="datasets",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.sql_console.embed.with_raw_response.update(
                id="",
                repo_type="datasets",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        embed = client.api.sql_console.embed.delete(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(object, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.sql_console.embed.with_raw_response.delete(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = response.parse()
        assert_matches_type(object, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.sql_console.embed.with_streaming_response.delete(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = response.parse()
            assert_matches_type(object, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.sql_console.embed.with_raw_response.delete(
                id="id",
                repo_type="datasets",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.sql_console.embed.with_raw_response.delete(
                id="id",
                repo_type="datasets",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.sql_console.embed.with_raw_response.delete(
                id="",
                repo_type="datasets",
                namespace="namespace",
                repo="repo",
            )


class TestAsyncEmbed:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        embed = await async_client.api.sql_console.embed.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        embed = await async_client.api.sql_console.embed.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
            private=True,
        )
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.sql_console.embed.with_raw_response.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = await response.parse()
        assert_matches_type(EmbedCreateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.sql_console.embed.with_streaming_response.create(
            repo="repo",
            repo_type="datasets",
            namespace="namespace",
            sql="sql",
            title="title",
            views=[
                {
                    "display_name": "displayName",
                    "key": "key",
                    "view_name": "viewName",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = await response.parse()
            assert_matches_type(EmbedCreateResponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.create(
                repo="repo",
                repo_type="datasets",
                namespace="",
                sql="sql",
                title="title",
                views=[
                    {
                        "display_name": "displayName",
                        "key": "key",
                        "view_name": "viewName",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.create(
                repo="",
                repo_type="datasets",
                namespace="namespace",
                sql="sql",
                title="title",
                views=[
                    {
                        "display_name": "displayName",
                        "key": "key",
                        "view_name": "viewName",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHuggingFace) -> None:
        embed = await async_client.api.sql_console.embed.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        embed = await async_client.api.sql_console.embed.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
            private=True,
            sql="sql",
            title="title",
        )
        assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.sql_console.embed.with_raw_response.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = await response.parse()
        assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.sql_console.embed.with_streaming_response.update(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = await response.parse()
            assert_matches_type(EmbedUpdateResponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.update(
                id="id",
                repo_type="datasets",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.update(
                id="id",
                repo_type="datasets",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.update(
                id="",
                repo_type="datasets",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        embed = await async_client.api.sql_console.embed.delete(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(object, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.sql_console.embed.with_raw_response.delete(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = await response.parse()
        assert_matches_type(object, embed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.sql_console.embed.with_streaming_response.delete(
            id="id",
            repo_type="datasets",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = await response.parse()
            assert_matches_type(object, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.delete(
                id="id",
                repo_type="datasets",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.delete(
                id="id",
                repo_type="datasets",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.sql_console.embed.with_raw_response.delete(
                id="",
                repo_type="datasets",
                namespace="namespace",
                repo="repo",
            )
