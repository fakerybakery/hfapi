# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.organizations import AuditLogExportResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export(self, client: HuggingFace) -> None:
        audit_log = client.api.organizations.audit_log.export(
            name="name",
        )
        assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: HuggingFace) -> None:
        audit_log = client.api.organizations.audit_log.export(
            name="name",
            q="author:huggingface",
        )
        assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: HuggingFace) -> None:
        response = client.api.organizations.audit_log.with_raw_response.export(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: HuggingFace) -> None:
        with client.api.organizations.audit_log.with_streaming_response.export(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_export(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.audit_log.with_raw_response.export(
                name="",
            )


class TestAsyncAuditLog:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncHuggingFace) -> None:
        audit_log = await async_client.api.organizations.audit_log.export(
            name="name",
        )
        assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        audit_log = await async_client.api.organizations.audit_log.export(
            name="name",
            q="author:huggingface",
        )
        assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.audit_log.with_raw_response.export(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.audit_log.with_streaming_response.export(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AuditLogExportResponse, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.audit_log.with_raw_response.export(
                name="",
            )
