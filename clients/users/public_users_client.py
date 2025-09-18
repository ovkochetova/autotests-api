from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateUserRequestDict(TypedDict):
        email: str
        password: str
        lastName: str
        firstName: str
        middleName: str


class PublicUsersClient(APIClient):
    """
    Публичный клиент для работы с api/v1/users
        """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
    Метод выполняет создание пользователя.

    :param request: Словарь с email, password, lastName, firstName, middleName
    :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/users", json = request)

