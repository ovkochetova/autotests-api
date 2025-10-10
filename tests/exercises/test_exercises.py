from http import HTTPStatus

import pytest
from httpx import request

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseSchema, CreateExerciseResponseSchema, \
     GetExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response
from tools.assertions.schema import validate_json_schema

@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
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

    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        # Отправляем GET-запрос на запрос курса по его ид
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список данные, переданные при создании совпадают с данными, возвращенными от сервера
        assert_get_exercise_response(response_data, function_exercise.response)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
