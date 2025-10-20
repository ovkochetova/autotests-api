from clients.api_client import APIClient
from httpx import Response

from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import allure

from tools.routes import APIRoutes


class PublicUsersClient(APIClient):
    """
    Публичный клиент для работы с api/v1/users
        """
    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
    Метод выполняет создание пользователя.

    :param request: Словарь с email, password, lastName, firstName, middleName
    :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.USERS, json = request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())