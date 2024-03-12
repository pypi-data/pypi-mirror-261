from typing import Any
from http import HTTPStatus
from httpx import AsyncClient as HttpClient, HTTPError, Cookies
from httpx._types import ProxyTypes
from brainly_api.constants import Market, LEGACY_API_PROTOCOL
from .responses import LegacyApiResponse
from .exceptions import BrainlyLegacyAPIException, RequestFailedException


class BrainlyLegacyAPI:
    """
    Represents the legacy API (REST API) of Brainly.com
    This API Will be replaced with the GraphQL API in the future.
    """

    _client: HttpClient

    headers: dict[str, str]
    cookies: Cookies
    host: str
    protocol_version: int
    token: str | None

    def __init__(
        self,
        market: Market,
        host: str,
        protocol_version: int = LEGACY_API_PROTOCOL,
        token: str | None = None,
        timeout: int = 20,
        headers: dict[str, str] | None = None,
        proxy: ProxyTypes | None = None,
        http2: bool = False
    ):
        if isinstance(token, str):
            assert 10 < len(token) < 50, "Invalid token length"

        try:
            if isinstance(market, Market):
                self.market = market
            elif isinstance(market, str):
                market = Market(market)
            else:
                raise
        except ValueError:
            raise ValueError(f"Invalid market: {market}. Supported markets are {list(map(lambda it: it.value, Market))}")

        self.token = token
        self.market = market
        self.headers = headers or {}
        self.protocol_version = protocol_version
        self.host = host

        self._client = HttpClient(
            base_url=self._base_url,
            headers=self._headers,
            cookies=self._cookies,
            timeout=timeout,
            http2=http2,
            proxy=proxy
        )

    @property
    def _base_url(self):
        url = self.host.replace("{market}", self.market.value)
        url += f"/api/{self.protocol_version}"
        return url

    @property
    def _headers(self):
        return {
            "X-B-Token-Long": self.token
        } | self.headers

    @property
    def _cookies(self):
        cookies = Cookies()
        cookies.set("Zadanepl_cookie[Token][Long]", self.token)
        return cookies

    async def _request(
        self,
        path: str,
        http_method: str | None = "GET",
        data: Any | None = None
    ) -> LegacyApiResponse:
        """Make a request to the API"""
        # response = await self._client.request(
        #     method=http_method,
        #     url=path,
        #     json=data
        # )
        #
        # print(response.url)
        #
        # return response
        try:
            r = await self._client.request(
                method=http_method,
                url=path,
                json=data
            )

            if r.status_code == HTTPStatus.BAD_GATEWAY:
                raise RequestFailedException(f"Response status is {r.status_code}")
            if r.status_code == HTTPStatus.FORBIDDEN and "captcha" in r.text:
                raise RequestFailedException("403 Forbidden error")

            data = r.json()
            if not isinstance(data, dict):
                raise RequestFailedException(f"Unknown response data format: {data}")

            if data.get("success") is False:
                raise BrainlyLegacyAPIException(data)

            return LegacyApiResponse(data)
        except (ValueError, HTTPError) as exc:
            raise RequestFailedException(str(exc))

    async def get_me(self):
        """Get information about the authenticated user."""
        return await self._request("api_users/me")
