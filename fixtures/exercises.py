import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture

class ExerciseFixture(BaseModel):
    request: CreateExerciseSchema
    response: CreateExerciseResponseSchema

@pytest.fixture(scope = "function")
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture(scope = "function")
def function_exercise(function_user: UserFixture, function_course: CourseFixture) -> ExerciseFixture:
    request: CreateExerciseSchema
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request,response=response)