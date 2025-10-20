from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema,GetFileResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
import allure
from config import settings
from tools.logger import get_logger

logger = get_logger("FILE_ASSERTIONS")

@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
     Проверяет, что ответ на создание файла соответствует запросу.

     :param request: Исходный запрос на создание файла.
     :param response: Ответ API с данными файла.
     :raises AssertionError: Если хотя бы одно поле не совпадает.
     """
    logger.info("Check create file response")
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    logger.info("Check file")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")

@allure.step("Check get file response")
def assert_get_file_response(get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    logger.info("Check get file response")
    assert_file(get_file_response.file, create_file_response.file)

@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty filename response")

    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "filename"]  # Ошибка возникает в теле запроса, поле "filename".
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check create file with empty direcore response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty directory response")

    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "directory"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    logger.info("Check file not found response")

    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
      Проверяет, что ответ на запрос файла с некорректным значением ид соответствует ожидаемой валидационной ошибке.

      :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
      :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
      """

    logger.info("Check get file with incorrect file id response")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type= "uuid_parsing", # Тип ошибки, связанной с неверным форматом строки
                input= "incorrect-file-id", # Введенное некорретное значение
                context={ "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"}, # Ожидается строка в формате UUID или с префиксом urn:uuid:
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",  # Сообщение об ошибке.
                location=["path", "file_id"]  # Ошибка возникает в пути запроса, поле "file_id"
            )
        ]
    )
    assert_validation_error_response(actual, expected)
