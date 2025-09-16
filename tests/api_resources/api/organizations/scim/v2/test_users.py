# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.organizations.scim.v2 import (
    UserListResponse,
    UserCreateResponse,
    UserUpdateResponse,
    UserRetrieveResponse,
    UserUpdateAttributesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
            active=True,
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.users.with_raw_response.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.users.with_streaming_response.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.create(
                path_name="",
                emails=[{"value": "dev@stainless.com"}],
                external_id="externalId",
                body_name={
                    "family_name": "x",
                    "given_name": "x",
                },
                schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
                user_name="userName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.retrieve(
            user_id="userId",
            name="name",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.users.with_raw_response.retrieve(
            user_id="userId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.users.with_streaming_response.retrieve(
            user_id="userId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.retrieve(
                user_id="userId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.retrieve(
                user_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
            active=True,
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.users.with_raw_response.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.users.with_streaming_response.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.update(
                user_id="userId",
                path_name="",
                emails=[{"value": "dev@stainless.com"}],
                external_id="externalId",
                body_name={
                    "family_name": "x",
                    "given_name": "x",
                },
                schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
                user_name="userName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.update(
                user_id="",
                path_name="name",
                emails=[{"value": "dev@stainless.com"}],
                external_id="externalId",
                body_name={
                    "family_name": "x",
                    "given_name": "x",
                },
                schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
                user_name="userName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.list(
            name="name",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.list(
            name="name",
            count=1,
            filter="filter",
            start_index=1,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.users.with_raw_response.list(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.users.with_streaming_response.list(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.list(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.delete(
            user_id="userId",
            name="name",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.users.with_raw_response.delete(
            user_id="userId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.users.with_streaming_response.delete(
            user_id="userId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.delete(
                user_id="userId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.delete(
                user_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_attributes(self, client: HuggingFace) -> None:
        user = client.api.organizations.scim.v2.users.update_attributes(
            user_id="userId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "value": {},
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )
        assert_matches_type(UserUpdateAttributesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_attributes(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.users.with_raw_response.update_attributes(
            user_id="userId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "value": {},
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateAttributesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_attributes(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.users.with_streaming_response.update_attributes(
            user_id="userId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "value": {},
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateAttributesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_attributes(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.update_attributes(
                user_id="userId",
                name="",
                operations=[
                    {
                        "op": "op",
                        "value": {},
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.organizations.scim.v2.users.with_raw_response.update_attributes(
                user_id="",
                name="name",
                operations=[
                    {
                        "op": "op",
                        "value": {},
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
            active=True,
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.users.with_raw_response.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.users.with_streaming_response.create(
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.create(
                path_name="",
                emails=[{"value": "dev@stainless.com"}],
                external_id="externalId",
                body_name={
                    "family_name": "x",
                    "given_name": "x",
                },
                schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
                user_name="userName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.retrieve(
            user_id="userId",
            name="name",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.users.with_raw_response.retrieve(
            user_id="userId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.users.with_streaming_response.retrieve(
            user_id="userId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.retrieve(
                user_id="userId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.retrieve(
                user_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
            active=True,
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.users.with_raw_response.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.users.with_streaming_response.update(
            user_id="userId",
            path_name="name",
            emails=[{"value": "dev@stainless.com"}],
            external_id="externalId",
            body_name={
                "family_name": "x",
                "given_name": "x",
            },
            schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
            user_name="userName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.update(
                user_id="userId",
                path_name="",
                emails=[{"value": "dev@stainless.com"}],
                external_id="externalId",
                body_name={
                    "family_name": "x",
                    "given_name": "x",
                },
                schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
                user_name="userName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.update(
                user_id="",
                path_name="name",
                emails=[{"value": "dev@stainless.com"}],
                external_id="externalId",
                body_name={
                    "family_name": "x",
                    "given_name": "x",
                },
                schemas=["urn:ietf:params:scim:schemas:core:2.0:User"],
                user_name="userName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.list(
            name="name",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.list(
            name="name",
            count=1,
            filter="filter",
            start_index=1,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.users.with_raw_response.list(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.users.with_streaming_response.list(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.list(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.delete(
            user_id="userId",
            name="name",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.users.with_raw_response.delete(
            user_id="userId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.users.with_streaming_response.delete(
            user_id="userId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.delete(
                user_id="userId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.delete(
                user_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        user = await async_client.api.organizations.scim.v2.users.update_attributes(
            user_id="userId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "value": {},
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )
        assert_matches_type(UserUpdateAttributesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.users.with_raw_response.update_attributes(
            user_id="userId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "value": {},
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateAttributesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.users.with_streaming_response.update_attributes(
            user_id="userId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "value": {},
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateAttributesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.update_attributes(
                user_id="userId",
                name="",
                operations=[
                    {
                        "op": "op",
                        "value": {},
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.organizations.scim.v2.users.with_raw_response.update_attributes(
                user_id="",
                name="name",
                operations=[
                    {
                        "op": "op",
                        "value": {},
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )
