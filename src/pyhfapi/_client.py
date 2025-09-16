# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import spaces, resolve, datasets, ask_access, user_access_report
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, HuggingFaceError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.api import api
from .resources.oauth import oauth

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "HuggingFace",
    "AsyncHuggingFace",
    "Client",
    "AsyncClient",
]


class HuggingFace(SyncAPIClient):
    api: api.APIResource
    oauth: oauth.OAuthResource
    spaces: spaces.SpacesResource
    datasets: datasets.DatasetsResource
    resolve: resolve.ResolveResource
    ask_access: ask_access.AskAccessResource
    user_access_report: user_access_report.UserAccessReportResource
    with_raw_response: HuggingFaceWithRawResponse
    with_streaming_response: HuggingFaceWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous HuggingFace client instance.

        This automatically infers the `api_key` argument from the `HF_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HF_TOKEN")
        if api_key is None:
            raise HuggingFaceError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HF_TOKEN environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("HUGGING_FACE_BASE_URL")
        if base_url is None:
            base_url = f"https://huggingface.co"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api = api.APIResource(self)
        self.oauth = oauth.OAuthResource(self)
        self.spaces = spaces.SpacesResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.resolve = resolve.ResolveResource(self)
        self.ask_access = ask_access.AskAccessResource(self)
        self.user_access_report = user_access_report.UserAccessReportResource(self)
        self.with_raw_response = HuggingFaceWithRawResponse(self)
        self.with_streaming_response = HuggingFaceWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHuggingFace(AsyncAPIClient):
    api: api.AsyncAPIResource
    oauth: oauth.AsyncOAuthResource
    spaces: spaces.AsyncSpacesResource
    datasets: datasets.AsyncDatasetsResource
    resolve: resolve.AsyncResolveResource
    ask_access: ask_access.AsyncAskAccessResource
    user_access_report: user_access_report.AsyncUserAccessReportResource
    with_raw_response: AsyncHuggingFaceWithRawResponse
    with_streaming_response: AsyncHuggingFaceWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHuggingFace client instance.

        This automatically infers the `api_key` argument from the `HF_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("HF_TOKEN")
        if api_key is None:
            raise HuggingFaceError(
                "The api_key client option must be set either by passing api_key to the client or by setting the HF_TOKEN environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("HUGGING_FACE_BASE_URL")
        if base_url is None:
            base_url = f"https://huggingface.co"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api = api.AsyncAPIResource(self)
        self.oauth = oauth.AsyncOAuthResource(self)
        self.spaces = spaces.AsyncSpacesResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.resolve = resolve.AsyncResolveResource(self)
        self.ask_access = ask_access.AsyncAskAccessResource(self)
        self.user_access_report = user_access_report.AsyncUserAccessReportResource(self)
        self.with_raw_response = AsyncHuggingFaceWithRawResponse(self)
        self.with_streaming_response = AsyncHuggingFaceWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HuggingFaceWithRawResponse:
    def __init__(self, client: HuggingFace) -> None:
        self.api = api.APIResourceWithRawResponse(client.api)
        self.oauth = oauth.OAuthResourceWithRawResponse(client.oauth)
        self.spaces = spaces.SpacesResourceWithRawResponse(client.spaces)
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.resolve = resolve.ResolveResourceWithRawResponse(client.resolve)
        self.ask_access = ask_access.AskAccessResourceWithRawResponse(client.ask_access)
        self.user_access_report = user_access_report.UserAccessReportResourceWithRawResponse(client.user_access_report)


class AsyncHuggingFaceWithRawResponse:
    def __init__(self, client: AsyncHuggingFace) -> None:
        self.api = api.AsyncAPIResourceWithRawResponse(client.api)
        self.oauth = oauth.AsyncOAuthResourceWithRawResponse(client.oauth)
        self.spaces = spaces.AsyncSpacesResourceWithRawResponse(client.spaces)
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.resolve = resolve.AsyncResolveResourceWithRawResponse(client.resolve)
        self.ask_access = ask_access.AsyncAskAccessResourceWithRawResponse(client.ask_access)
        self.user_access_report = user_access_report.AsyncUserAccessReportResourceWithRawResponse(
            client.user_access_report
        )


class HuggingFaceWithStreamedResponse:
    def __init__(self, client: HuggingFace) -> None:
        self.api = api.APIResourceWithStreamingResponse(client.api)
        self.oauth = oauth.OAuthResourceWithStreamingResponse(client.oauth)
        self.spaces = spaces.SpacesResourceWithStreamingResponse(client.spaces)
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.resolve = resolve.ResolveResourceWithStreamingResponse(client.resolve)
        self.ask_access = ask_access.AskAccessResourceWithStreamingResponse(client.ask_access)
        self.user_access_report = user_access_report.UserAccessReportResourceWithStreamingResponse(
            client.user_access_report
        )


class AsyncHuggingFaceWithStreamedResponse:
    def __init__(self, client: AsyncHuggingFace) -> None:
        self.api = api.AsyncAPIResourceWithStreamingResponse(client.api)
        self.oauth = oauth.AsyncOAuthResourceWithStreamingResponse(client.oauth)
        self.spaces = spaces.AsyncSpacesResourceWithStreamingResponse(client.spaces)
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.resolve = resolve.AsyncResolveResourceWithStreamingResponse(client.resolve)
        self.ask_access = ask_access.AsyncAskAccessResourceWithStreamingResponse(client.ask_access)
        self.user_access_report = user_access_report.AsyncUserAccessReportResourceWithStreamingResponse(
            client.user_access_report
        )


Client = HuggingFace

AsyncClient = AsyncHuggingFace
