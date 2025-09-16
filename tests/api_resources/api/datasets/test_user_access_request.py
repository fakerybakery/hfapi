# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.datasets import (
    UserAccessRequestListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserAccessRequest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        user_access_request = client.api.datasets.user_access_request.list(
            status="pending",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(UserAccessRequestListResponse, user_access_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.datasets.user_access_request.with_raw_response.list(
            status="pending",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = response.parse()
        assert_matches_type(UserAccessRequestListResponse, user_access_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.datasets.user_access_request.with_streaming_response.list(
            status="pending",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = response.parse()
            assert_matches_type(UserAccessRequestListResponse, user_access_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.list(
                status="pending",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.list(
                status="pending",
                namespace="namespace",
                repo="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: HuggingFace) -> None:
        user_access_request = client.api.datasets.user_access_request.cancel(
            repo="repo",
            namespace="namespace",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: HuggingFace) -> None:
        response = client.api.datasets.user_access_request.with_raw_response.cancel(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = response.parse()
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: HuggingFace) -> None:
        with client.api.datasets.user_access_request.with_streaming_response.cancel(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = response.parse()
            assert user_access_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.cancel(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.cancel(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_grant(self, client: HuggingFace) -> None:
        user_access_request = client.api.datasets.user_access_request.grant(
            repo="repo",
            namespace="namespace",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_grant_with_all_params(self, client: HuggingFace) -> None:
        user_access_request = client.api.datasets.user_access_request.grant(
            repo="repo",
            namespace="namespace",
            user="user",
            user_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_grant(self, client: HuggingFace) -> None:
        response = client.api.datasets.user_access_request.with_raw_response.grant(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = response.parse()
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_grant(self, client: HuggingFace) -> None:
        with client.api.datasets.user_access_request.with_streaming_response.grant(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = response.parse()
            assert user_access_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_grant(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.grant(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.grant(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_handle(self, client: HuggingFace) -> None:
        user_access_request = client.api.datasets.user_access_request.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_handle_with_all_params(self, client: HuggingFace) -> None:
        user_access_request = client.api.datasets.user_access_request.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
            rejection_reason="rejectionReason",
            user="user",
            user_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_handle(self, client: HuggingFace) -> None:
        response = client.api.datasets.user_access_request.with_raw_response.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = response.parse()
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_handle(self, client: HuggingFace) -> None:
        with client.api.datasets.user_access_request.with_streaming_response.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = response.parse()
            assert user_access_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_handle(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.handle(
                repo="repo",
                namespace="",
                status="accepted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.user_access_request.with_raw_response.handle(
                repo="",
                namespace="namespace",
                status="accepted",
            )


class TestAsyncUserAccessRequest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        user_access_request = await async_client.api.datasets.user_access_request.list(
            status="pending",
            namespace="namespace",
            repo="repo",
        )
        assert_matches_type(UserAccessRequestListResponse, user_access_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.user_access_request.with_raw_response.list(
            status="pending",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = await response.parse()
        assert_matches_type(UserAccessRequestListResponse, user_access_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.user_access_request.with_streaming_response.list(
            status="pending",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = await response.parse()
            assert_matches_type(UserAccessRequestListResponse, user_access_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.list(
                status="pending",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.list(
                status="pending",
                namespace="namespace",
                repo="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncHuggingFace) -> None:
        user_access_request = await async_client.api.datasets.user_access_request.cancel(
            repo="repo",
            namespace="namespace",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.user_access_request.with_raw_response.cancel(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = await response.parse()
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.user_access_request.with_streaming_response.cancel(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = await response.parse()
            assert user_access_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.cancel(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.cancel(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_grant(self, async_client: AsyncHuggingFace) -> None:
        user_access_request = await async_client.api.datasets.user_access_request.grant(
            repo="repo",
            namespace="namespace",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_grant_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        user_access_request = await async_client.api.datasets.user_access_request.grant(
            repo="repo",
            namespace="namespace",
            user="user",
            user_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_grant(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.user_access_request.with_raw_response.grant(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = await response.parse()
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_grant(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.user_access_request.with_streaming_response.grant(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = await response.parse()
            assert user_access_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_grant(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.grant(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.grant(
                repo="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_handle(self, async_client: AsyncHuggingFace) -> None:
        user_access_request = await async_client.api.datasets.user_access_request.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_handle_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        user_access_request = await async_client.api.datasets.user_access_request.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
            rejection_reason="rejectionReason",
            user="user",
            user_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_handle(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.user_access_request.with_raw_response.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_request = await response.parse()
        assert user_access_request is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_handle(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.user_access_request.with_streaming_response.handle(
            repo="repo",
            namespace="namespace",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_request = await response.parse()
            assert user_access_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_handle(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.handle(
                repo="repo",
                namespace="",
                status="accepted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.user_access_request.with_raw_response.handle(
                repo="",
                namespace="namespace",
                status="accepted",
            )
