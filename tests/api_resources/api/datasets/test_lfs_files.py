# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.datasets import (
    LFSFileListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLFSFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        lfs_file = client.api.datasets.lfs_files.list(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HuggingFace) -> None:
        lfs_file = client.api.datasets.lfs_files.list(
            repo="repo",
            namespace="namespace",
            cursor="cursor",
            limit=1,
            xet={},
        )
        assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.datasets.lfs_files.with_raw_response.list(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lfs_file = response.parse()
        assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.datasets.lfs_files.with_streaming_response.list(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lfs_file = response.parse()
            assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.lfs_files.with_raw_response.list(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.lfs_files.with_raw_response.list(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        lfs_file = client.api.datasets.lfs_files.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HuggingFace) -> None:
        lfs_file = client.api.datasets.lfs_files.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
            rewrite_history={},
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.datasets.lfs_files.with_raw_response.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lfs_file = response.parse()
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.datasets.lfs_files.with_streaming_response.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lfs_file = response.parse()
            assert lfs_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.lfs_files.with_raw_response.delete(
                sha="sha",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.lfs_files.with_raw_response.delete(
                sha="sha",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sha` but received ''"):
            client.api.datasets.lfs_files.with_raw_response.delete(
                sha="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_batch(self, client: HuggingFace) -> None:
        lfs_file = client.api.datasets.lfs_files.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={"sha": ["string"]},
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_batch_with_all_params(self, client: HuggingFace) -> None:
        lfs_file = client.api.datasets.lfs_files.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={
                "sha": ["string"],
                "rewrite_history": True,
            },
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_batch(self, client: HuggingFace) -> None:
        response = client.api.datasets.lfs_files.with_raw_response.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={"sha": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lfs_file = response.parse()
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_batch(self, client: HuggingFace) -> None:
        with client.api.datasets.lfs_files.with_streaming_response.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={"sha": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lfs_file = response.parse()
            assert lfs_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_batch(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.lfs_files.with_raw_response.delete_batch(
                repo="repo",
                namespace="",
                deletions={"sha": ["string"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.lfs_files.with_raw_response.delete_batch(
                repo="",
                namespace="namespace",
                deletions={"sha": ["string"]},
            )


class TestAsyncLFSFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        lfs_file = await async_client.api.datasets.lfs_files.list(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        lfs_file = await async_client.api.datasets.lfs_files.list(
            repo="repo",
            namespace="namespace",
            cursor="cursor",
            limit=1,
            xet={},
        )
        assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.lfs_files.with_raw_response.list(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lfs_file = await response.parse()
        assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.lfs_files.with_streaming_response.list(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lfs_file = await response.parse()
            assert_matches_type(LFSFileListResponse, lfs_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.lfs_files.with_raw_response.list(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.lfs_files.with_raw_response.list(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        lfs_file = await async_client.api.datasets.lfs_files.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        lfs_file = await async_client.api.datasets.lfs_files.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
            rewrite_history={},
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.lfs_files.with_raw_response.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lfs_file = await response.parse()
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.lfs_files.with_streaming_response.delete(
            sha="sha",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lfs_file = await response.parse()
            assert lfs_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.lfs_files.with_raw_response.delete(
                sha="sha",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.lfs_files.with_raw_response.delete(
                sha="sha",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sha` but received ''"):
            await async_client.api.datasets.lfs_files.with_raw_response.delete(
                sha="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_batch(self, async_client: AsyncHuggingFace) -> None:
        lfs_file = await async_client.api.datasets.lfs_files.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={"sha": ["string"]},
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_batch_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        lfs_file = await async_client.api.datasets.lfs_files.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={
                "sha": ["string"],
                "rewrite_history": True,
            },
        )
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_batch(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.lfs_files.with_raw_response.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={"sha": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lfs_file = await response.parse()
        assert lfs_file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_batch(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.lfs_files.with_streaming_response.delete_batch(
            repo="repo",
            namespace="namespace",
            deletions={"sha": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lfs_file = await response.parse()
            assert lfs_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_batch(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.lfs_files.with_raw_response.delete_batch(
                repo="repo",
                namespace="",
                deletions={"sha": ["string"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.lfs_files.with_raw_response.delete_batch(
                repo="",
                namespace="namespace",
                deletions={"sha": ["string"]},
            )
