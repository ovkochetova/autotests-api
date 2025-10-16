from http import HTTPStatus


import pytest

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from config import settings
from fixtures.files import FileFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema
import allure
from allure_commons.types import Severity


@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSIONS)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.FILES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.FILES)
class TestFiles:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create File")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get File")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.tag("VALIDATE_ENTITY")
    @allure.title("Create File With Empty Filename")
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(filename="", upload_file=settings.test_data.image_png_file)
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.title("Get File With Empty Directory")
    @allure.severity(Severity.NORMAL)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(directory="", upload_file=settings.test_data.image_png_file)
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.title("Get File With deleted File ID")
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        response = files_client.get_file_api(file_id="incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # Проверка, что код ответа соответствует ожиданиям (422 - Unprocessable Entity)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # Проверка, что ответ API соответствует ожидаемой валидационной ошибке
        assert_get_file_with_incorrect_file_id_response(response_data)
        # Дополнительная проверка структуры JSON, чтобы убедиться, что схема валидационного ответа не изменилась
        validate_json_schema(response.json(), response_data.model_json_schema())

