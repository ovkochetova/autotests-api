from http import HTTPStatus

import allure
import pytest
from httpx import request

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExerciseQuerySchema, \
    GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema
from allure_commons.types import Severity


@pytest.mark.exercises
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.EXERCISES)
class TestExercises:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create Exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        # Формируем параметры запроса, передавая course_id
        request = CreateExerciseSchema(course_id = function_course.response.course.id)
        # Отправляем POST-запрос на создание задания
        response = exercises_client.create_exercise_api(request)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список данные, переданные при создании совпадают с данными, возвращенными от сервера
        assert_create_exercise_response(request, response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

        # Отправляем GET-запрос на запрос курса по его ид

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get Exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список данные, переданные при создании совпадают с данными, возвращенными от сервера
        assert_get_exercise_response(response_data, function_exercise.response)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update Exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        # Формируем модель запроса
        request = UpdateExerciseRequestSchema()
        # Отправляем PATCH-запрос на обновление задания
        response = exercises_client.update_exercise_api(exercise_id=function_exercise.response.exercise.id, request=request)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список данные, переданные при создании совпадают с данными, возвращенными от сервера
        assert_update_exercise_response(request, response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete Exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        # Удаляем задание
        delete_response = exercises_client.delete_exercise_api(exercise_id=function_exercise.response.exercise.id)
        # Проверяем, что файл успешно удален (статус 200 OK)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        # Пытаемся получить удаленный файл
        get_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        # Проверяем, что сервер вернул 404 Not Found
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        # Проверяем, что ответ соответствует схеме
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get Exercises")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    def test_get_exercises(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture, function_course: CourseFixture):
        # Формируем структуру запроса
        query = GetExerciseQuerySchema(course_id=function_course.response.course.id)
        # Отправляем GET-запрос на получение списка заданий
        response = exercises_client.get_exercises_api(query)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список данные, переданные при создании совпадают с данными, возвращенными от сервера
        assert_get_exercises_response(response_data, [function_exercise.response])

        # Проверяем, что ответ соответствует схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

