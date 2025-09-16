# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types.api import (
    ResolveCacheResolveModelResponse,
    ResolveCacheResolveSpaceResponse,
    ResolveCacheResolveDatasetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResolveCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_dataset(self, client: HuggingFace) -> None:
        resolve_cache = client.api.resolve_cache.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_dataset_with_all_params(self, client: HuggingFace) -> None:
        resolve_cache = client.api.resolve_cache.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resolve_dataset(self, client: HuggingFace) -> None:
        response = client.api.resolve_cache.with_raw_response.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve_cache = response.parse()
        assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resolve_dataset(self, client: HuggingFace) -> None:
        with client.api.resolve_cache.with_streaming_response.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve_cache = response.parse()
            assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resolve_dataset(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_model(self, client: HuggingFace) -> None:
        resolve_cache = client.api.resolve_cache.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_model_with_all_params(self, client: HuggingFace) -> None:
        resolve_cache = client.api.resolve_cache.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resolve_model(self, client: HuggingFace) -> None:
        response = client.api.resolve_cache.with_raw_response.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve_cache = response.parse()
        assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resolve_model(self, client: HuggingFace) -> None:
        with client.api.resolve_cache.with_streaming_response.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve_cache = response.parse()
            assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resolve_model(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_model(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_model(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_model(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_model(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_space(self, client: HuggingFace) -> None:
        resolve_cache = client.api.resolve_cache.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_space_with_all_params(self, client: HuggingFace) -> None:
        resolve_cache = client.api.resolve_cache.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resolve_space(self, client: HuggingFace) -> None:
        response = client.api.resolve_cache.with_raw_response.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve_cache = response.parse()
        assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resolve_space(self, client: HuggingFace) -> None:
        with client.api.resolve_cache.with_streaming_response.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve_cache = response.parse()
            assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resolve_space(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_space(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_space(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_space(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.api.resolve_cache.with_raw_response.resolve_space(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )


class TestAsyncResolveCache:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_dataset(self, async_client: AsyncHuggingFace) -> None:
        resolve_cache = await async_client.api.resolve_cache.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_dataset_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        resolve_cache = await async_client.api.resolve_cache.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resolve_dataset(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.resolve_cache.with_raw_response.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve_cache = await response.parse()
        assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resolve_dataset(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.resolve_cache.with_streaming_response.resolve_dataset(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve_cache = await response.parse()
            assert_matches_type(ResolveCacheResolveDatasetResponse, resolve_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resolve_dataset(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_dataset(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_model(self, async_client: AsyncHuggingFace) -> None:
        resolve_cache = await async_client.api.resolve_cache.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_model_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        resolve_cache = await async_client.api.resolve_cache.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resolve_model(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.resolve_cache.with_raw_response.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve_cache = await response.parse()
        assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resolve_model(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.resolve_cache.with_streaming_response.resolve_model(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve_cache = await response.parse()
            assert_matches_type(ResolveCacheResolveModelResponse, resolve_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resolve_model(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_model(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_model(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_model(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_model(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_space(self, async_client: AsyncHuggingFace) -> None:
        resolve_cache = await async_client.api.resolve_cache.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_space_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        resolve_cache = await async_client.api.resolve_cache.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resolve_space(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.resolve_cache.with_raw_response.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve_cache = await response.parse()
        assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resolve_space(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.resolve_cache.with_streaming_response.resolve_space(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve_cache = await response.parse()
            assert_matches_type(ResolveCacheResolveSpaceResponse, resolve_cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resolve_space(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_space(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_space(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_space(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.api.resolve_cache.with_raw_response.resolve_space(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )
