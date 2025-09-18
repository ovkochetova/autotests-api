from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class LoginRequestDict(TypedDict):
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    refreshToken: str


class AuthenticationClient(APIClient):
    """
       Клиент для работы с /api/v1/authentication
       """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post("/api/v1/authentication/refresh", json=request)