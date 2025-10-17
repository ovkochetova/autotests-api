from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseSchema, \
    GetExerciseResponseSchema, ExerciseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
import allure
from tools.logger import get_logger

logger = get_logger("EXERCISE_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(request: CreateExerciseSchema, response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    logger.info("Check create exercise response")

    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    logger.info("Check exercise")

    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check get exercise response")
def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema , get_create_exercise: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных задания.
    :param get_create_exercise: Ответ API при создании задания.
    :raises AssertionError: Если данные задания не совпадают.
    """

    logger.info("Check get exercise response")

    assert_exercise(get_exercise_response.exercise, get_create_exercise.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API с обновленными данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    logger.info("Check update exercise response")

    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")
    assert_equal(request.description, response.exercise.description, "description")

@allure.step("Check get deleted exercise response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """

    logger.info("Check get deleted exercise response")

    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(get_exercises_response: GetExercisesResponseSchema, create_exercise_response: list[CreateExerciseResponseSchema]):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка курсов.
    :param create_exercise_response: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """

    logger.info("Check get exercises response")

    assert_length(get_exercises_response.exercises, create_exercise_response, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_response):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)

