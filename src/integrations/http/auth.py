from asyncio import Lock

from httpx import Auth, Request, Response


class HTTPAuth(Auth):
    requires_response_body = True

    def __init__(self, *, login: str, password: str, auth_url: str, client_id: str, scope: str) -> None:
        self.auth_url: str = auth_url
        self.login: str = login
        self.client_id: str = client_id
        self.scope: str = scope
        self._async_lock = Lock()
        self.__password: str = password
        self.__access_token: str = ""
        self.__refresh_token: str = ""

    def _build_auth_request(self):
        request = Request(
            method="POST",
            url=self.auth_url,
            data={
                "grant_type": "password",
                "client_id": self.client_id,
                "scope": self.scope,
                "username": self.login,
                "password": self.__password,
            },
        )

        return request

    async def _update_tokens(self, response: Response) -> None:
        await response.aread()  # Добавлено чтение ответа
        data = response.json()

        self.__access_token = data["access_token"]
        self.__refresh_token = data["refresh_token"]

    async def async_auth_flow(self, request: Request) -> Request:
        async with self._async_lock:
            if not self.__access_token:
                auth_response = yield self._build_auth_request()
                auth_response.raise_for_status()
                await self._update_tokens(auth_response)

        request.headers["Authorization"] = f"Bearer {self.__access_token}"
        yield request

    def sync_auth_flow(self, request):
        raise RuntimeError("Cannot use a async authentication class with httpx.Client")
