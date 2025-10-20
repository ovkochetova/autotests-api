from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
import pytest

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import  fake
import allure
from allure_commons.types import Severity

@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSIONS)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.USERS)
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    @allure.tag("CREATE_ENTITY")
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_user(self,domain: str, public_users_client: PublicUsersClient):
        allure.dynamic.title(f"Create User: {domain}")
        create_request = CreateUserRequestSchema(email=fake.email(domain=domain))
        create_response = public_users_client.create_user_api(create_request)
        create_response_data = CreateUserResponseSchema.model_validate_json(create_response.text)

        assert_status_code(create_response.status_code, HTTPStatus.OK)
        assert_create_user_response(create_response_data, create_request)

        validate_json_schema(create_response.json(), create_response_data.model_json_schema())

    @allure.tag("GET_ENTITY")
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get user me")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_user_me(self,private_users_client: PrivateUsersClient, function_user):
        get_me_response = private_users_client.get_user_me_api()
        get_me_response_data = GetUserResponseSchema.model_validate_json(get_me_response.text)

        assert_status_code(get_me_response.status_code, HTTPStatus.OK)
        assert_get_user_response(get_me_response_data, function_user.response)

        validate_json_schema(get_me_response.json(), get_me_response_data.model_json_schema())