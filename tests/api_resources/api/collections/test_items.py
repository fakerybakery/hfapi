# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types.api.collections import ItemAddResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        item = client.api.collections.items.delete(
            item_id="itemId",
            namespace="namespace",
            slug="slug",
            id="id",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.collections.items.with_raw_response.delete(
            item_id="itemId",
            namespace="namespace",
            slug="slug",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.collections.items.with_streaming_response.delete(
            item_id="itemId",
            namespace="namespace",
            slug="slug",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.collections.items.with_raw_response.delete(
                item_id="itemId",
                namespace="",
                slug="slug",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.collections.items.with_raw_response.delete(
                item_id="itemId",
                namespace="namespace",
                slug="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.collections.items.with_raw_response.delete(
                item_id="itemId",
                namespace="namespace",
                slug="slug",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.api.collections.items.with_raw_response.delete(
                item_id="",
                namespace="namespace",
                slug="slug",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: HuggingFace) -> None:
        item = client.api.collections.items.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
        )
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: HuggingFace) -> None:
        item = client.api.collections.items.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
            note="note",
        )
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: HuggingFace) -> None:
        response = client.api.collections.items.with_raw_response.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: HuggingFace) -> None:
        with client.api.collections.items.with_streaming_response.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemAddResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.collections.items.with_raw_response.add(
                id="id",
                namespace="",
                slug="slug",
                item={
                    "id": "id",
                    "type": "paper",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.collections.items.with_raw_response.add(
                id="id",
                namespace="namespace",
                slug="",
                item={
                    "id": "id",
                    "type": "paper",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.collections.items.with_raw_response.add(
                id="",
                namespace="namespace",
                slug="slug",
                item={
                    "id": "id",
                    "type": "paper",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_update(self, client: HuggingFace) -> None:
        item = client.api.collections.items.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_update_with_all_params(self, client: HuggingFace) -> None:
        item = client.api.collections.items.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
            body=[
                {
                    "_id": "ecc2efdd09bd231a9ad9bd2a",
                    "action": "update",
                    "data": {
                        "gallery": ["https://example.com"],
                        "note": "note",
                        "position": 0,
                    },
                }
            ],
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_update(self, client: HuggingFace) -> None:
        response = client.api.collections.items.with_raw_response.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_update(self, client: HuggingFace) -> None:
        with client.api.collections.items.with_streaming_response.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_batch_update(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.collections.items.with_raw_response.batch_update(
                id="id",
                namespace="",
                slug="slug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.collections.items.with_raw_response.batch_update(
                id="id",
                namespace="namespace",
                slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.collections.items.with_raw_response.batch_update(
                id="",
                namespace="namespace",
                slug="slug",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        item = await async_client.api.collections.items.delete(
            item_id="itemId",
            namespace="namespace",
            slug="slug",
            id="id",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.collections.items.with_raw_response.delete(
            item_id="itemId",
            namespace="namespace",
            slug="slug",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.collections.items.with_streaming_response.delete(
            item_id="itemId",
            namespace="namespace",
            slug="slug",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.collections.items.with_raw_response.delete(
                item_id="itemId",
                namespace="",
                slug="slug",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.collections.items.with_raw_response.delete(
                item_id="itemId",
                namespace="namespace",
                slug="",
                id="id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.collections.items.with_raw_response.delete(
                item_id="itemId",
                namespace="namespace",
                slug="slug",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.api.collections.items.with_raw_response.delete(
                item_id="",
                namespace="namespace",
                slug="slug",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncHuggingFace) -> None:
        item = await async_client.api.collections.items.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
        )
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        item = await async_client.api.collections.items.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
            note="note",
        )
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.collections.items.with_raw_response.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.collections.items.with_streaming_response.add(
            id="id",
            namespace="namespace",
            slug="slug",
            item={
                "id": "id",
                "type": "paper",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemAddResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.collections.items.with_raw_response.add(
                id="id",
                namespace="",
                slug="slug",
                item={
                    "id": "id",
                    "type": "paper",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.collections.items.with_raw_response.add(
                id="id",
                namespace="namespace",
                slug="",
                item={
                    "id": "id",
                    "type": "paper",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.collections.items.with_raw_response.add(
                id="",
                namespace="namespace",
                slug="slug",
                item={
                    "id": "id",
                    "type": "paper",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_update(self, async_client: AsyncHuggingFace) -> None:
        item = await async_client.api.collections.items.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_update_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        item = await async_client.api.collections.items.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
            body=[
                {
                    "_id": "ecc2efdd09bd231a9ad9bd2a",
                    "action": "update",
                    "data": {
                        "gallery": ["https://example.com"],
                        "note": "note",
                        "position": 0,
                    },
                }
            ],
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_update(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.collections.items.with_raw_response.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_update(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.collections.items.with_streaming_response.batch_update(
            id="id",
            namespace="namespace",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_batch_update(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.collections.items.with_raw_response.batch_update(
                id="id",
                namespace="",
                slug="slug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.collections.items.with_raw_response.batch_update(
                id="id",
                namespace="namespace",
                slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.collections.items.with_raw_response.batch_update(
                id="",
                namespace="namespace",
                slug="slug",
            )
