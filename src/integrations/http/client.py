from httpx import AsyncClient, Auth, Headers, Request, Response, Timeout
from loguru import logger


class HTTPClient:
    def __init__(
        self,
        *,
        base_url: str | None = "",
        headers: dict | None = None,
        timeout: float = 10.0,
        connection_timeout: float = 60.0,
        auth: "Auth" = None,
        client: AsyncClient | None = None,
    ) -> None:
        self.base_url: str = base_url
        self.headers: Headers = self._get_default_headers()
        if headers:
            self.headers.update(headers)
        self.timeout: Timeout = Timeout(timeout, connect=connection_timeout)
        self.auth: Auth = auth
        self.client: AsyncClient = client or AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            timeout=self.timeout,
            default_encoding="utf-8",
            auth=self.auth,
        )

    @staticmethod
    def _get_default_headers() -> Headers:
        return Headers({"Content-Type": "application/json"})

    @staticmethod
    def _remove_in_headers(headers: dict | None) -> dict | None:
        forbidden_headers = ["content-length", "host", "content-type"]
        if headers:
            headers = {k: v for k, v in headers.items() if k.lower() not in forbidden_headers}
        return headers

    async def send(
        self, method: str, url: str, *, data: dict = None, json: dict = None, params: dict = None, headers: dict = None
    ) -> Response:
        headers = self._remove_in_headers(headers)
        request: Request = self.client.build_request(method=method, url=url, headers=headers, json=json, data=data, params=params)

        try:
            response: Response = await self.client.send(request, auth=self.auth)
            response.raise_for_status()
            logger.info("HTTP Request", status_code=response.status_code, method=request.method, url=request.url)
            return response

        except Exception as exc:
            logger.exception(exc)
            raise

    async def close(self) -> None:
        await self.client.aclose()
