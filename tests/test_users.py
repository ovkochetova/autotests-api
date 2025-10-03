from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
import pytest
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import  fake


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
def test_create_user(domain: str,  public_users_client: PublicUsersClient):
    create_request = CreateUserRequestSchema(email=fake.email(domain=domain))
    create_response = public_users_client.create_user_api(create_request)
    create_response_data = CreateUserResponseSchema.model_validate_json(create_response.text)

    print('create_response_data:', create_response_data)

    assert_status_code(create_response.status_code, HTTPStatus.OK)
    assert_create_user_response(create_response_data, create_request)

    validate_json_schema(create_response.json(), create_response_data.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client: PrivateUsersClient, function_user):
    get_me_response = private_users_client.get_user_me_api()
    get_me_response_data = GetUserResponseSchema.model_validate_json(get_me_response.text)

    print('get_me_response_data:', get_me_response_data)
    print('function_user:', function_user)
    assert_status_code(get_me_response.status_code, HTTPStatus.OK)
    assert_get_user_response(get_me_response_data, function_user.response)

    validate_json_schema(get_me_response.json(), get_me_response_data.model_json_schema())

