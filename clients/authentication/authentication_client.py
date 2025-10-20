from clients.api_client import APIClient
from httpx import Response
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema, RefreshRequestSchema

from clients.public_http_builder import get_public_http_client
import allure

from tools.routes import APIRoutes


class AuthenticationClient(APIClient):
    """
       Клиент для работы с /api/v1/authentication
       """
    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.AUTHENTICATION}/login", json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post(f"{APIRoutes.AUTHENTICATION}/refresh", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        # return LoginResponseSchema(**response.json())
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())