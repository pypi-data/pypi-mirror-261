import re
from httpx import AsyncClient as HttpClient, Cookies
from httpx._types import ProxyTypes
from brainly_api.constants import Market, GRAPHQL_API_HOST
from .responses import BrainlyGraphqlResponse
from .exceptions import BrainlyGraphqlException


class BrainlyGraphQLAPI:
    """
    Represents the Brainly GraphQL API (https://brainly.com/graphql)
    """

    _client: HttpClient
    _headers: dict[str, str]
    _token: str | None

    def __init__(
        self,
        market: Market,
        host: str = GRAPHQL_API_HOST,
        token: str | None = None,
        timeout: int = 20,
        headers: dict[str, str] | None = None,
        cookies: Cookies | None = None,
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
            raise ValueError(
                f"Invalid market: {market}. Supported markets are {list(map(lambda it: it.value, Market))}")

        self._token = token
        self.market = market
        self.headers = headers

        self._client = HttpClient(
            base_url=host.strip("/") + f"/{market.value}",
            headers=self.headers,
            cookies=cookies,
            timeout=timeout,
            http2=http2,
            proxy=proxy
        )

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value: dict[str, str] | None):
        headers = {}
        value = value or {}

        if self._token:
            headers["X-B-Token-Long"] = self._token
        headers = headers | value

        self._headers = headers

    async def _make_http_request(self, url: str, method: str, body: dict | None = None) -> dict:
        """
        Make an asynchronous HTTP request to the Brainly GraphQL API
        """
        response = await self._client.request(method, url, json=body)
        return response.json()

    @staticmethod
    def _prepare_query(query: str):
        query = query.strip()
        # query = re.sub(r"(?<={)", "__typename ", query)
        return query

    async def query(self, query: str, variables: dict = None) -> BrainlyGraphqlResponse:
        """Execute a GraphQL query/mutation"""
        query = self._prepare_query(query)

        try:
            http_response = await self._make_http_request(
                url="/",
                method="POST",
                body={
                    "query": query,
                    "variables": variables
                }
            )

            response = BrainlyGraphqlResponse(http_response)

            if len(response.errors) > 0:
                raise BrainlyGraphqlException(
                    message="GraphQL errors",
                    response=response,
                    query=query,
                    variables=variables
                )

            return response
        except BrainlyGraphqlException:
            raise
        except Exception as exc:
            raise BrainlyGraphqlException(str(exc)) from exc
