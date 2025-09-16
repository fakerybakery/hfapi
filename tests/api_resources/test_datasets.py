# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from hfpy.types import DatasetResolveFileResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_access_report(self, client: HuggingFace) -> None:
        dataset = client.datasets.export_access_report(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(str, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export_access_report(self, client: HuggingFace) -> None:
        response = client.datasets.with_raw_response.export_access_report(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(str, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export_access_report(self, client: HuggingFace) -> None:
        with client.datasets.with_streaming_response.export_access_report(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(str, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_export_access_report(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.datasets.with_raw_response.export_access_report(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.datasets.with_raw_response.export_access_report(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_request_access(self, client: HuggingFace) -> None:
        dataset = client.datasets.request_access(
            repo="repo",
            namespace="namespace",
        )
        assert dataset is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_request_access_with_all_params(self, client: HuggingFace) -> None:
        dataset = client.datasets.request_access(
            repo="repo",
            namespace="namespace",
            body={"foo": "bar"},
        )
        assert dataset is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_raw_response_request_access(self, client: HuggingFace) -> None:
        response = client.datasets.with_raw_response.request_access(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_streaming_response_request_access(self, client: HuggingFace) -> None:
        with client.datasets.with_streaming_response.request_access(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_path_params_request_access(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.datasets.with_raw_response.request_access(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.datasets.with_raw_response.request_access(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_file(self, client: HuggingFace) -> None:
        dataset = client.datasets.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resolve_file_with_all_params(self, client: HuggingFace) -> None:
        dataset = client.datasets.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resolve_file(self, client: HuggingFace) -> None:
        response = client.datasets.with_raw_response.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resolve_file(self, client: HuggingFace) -> None:
        with client.datasets.with_streaming_response.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resolve_file(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.datasets.with_raw_response.resolve_file(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.datasets.with_raw_response.resolve_file(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.datasets.with_raw_response.resolve_file(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.datasets.with_raw_response.resolve_file(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_access_report(self, async_client: AsyncHuggingFace) -> None:
        dataset = await async_client.datasets.export_access_report(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(str, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export_access_report(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.datasets.with_raw_response.export_access_report(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(str, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export_access_report(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.datasets.with_streaming_response.export_access_report(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(str, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_export_access_report(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.datasets.with_raw_response.export_access_report(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.datasets.with_raw_response.export_access_report(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_request_access(self, async_client: AsyncHuggingFace) -> None:
        dataset = await async_client.datasets.request_access(
            repo="repo",
            namespace="namespace",
        )
        assert dataset is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_request_access_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        dataset = await async_client.datasets.request_access(
            repo="repo",
            namespace="namespace",
            body={"foo": "bar"},
        )
        assert dataset is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_raw_response_request_access(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.datasets.with_raw_response.request_access(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_streaming_response_request_access(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.datasets.with_streaming_response.request_access(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_path_params_request_access(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.datasets.with_raw_response.request_access(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.datasets.with_raw_response.request_access(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_file(self, async_client: AsyncHuggingFace) -> None:
        dataset = await async_client.datasets.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resolve_file_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        dataset = await async_client.datasets.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resolve_file(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.datasets.with_raw_response.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resolve_file(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.datasets.with_streaming_response.resolve_file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetResolveFileResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resolve_file(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.datasets.with_raw_response.resolve_file(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.datasets.with_raw_response.resolve_file(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.datasets.with_raw_response.resolve_file(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.datasets.with_raw_response.resolve_file(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )
