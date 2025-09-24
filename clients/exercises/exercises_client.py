from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class CreateExerciseDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    description: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    estimatedTime: str


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания.
    """
    exercises: list[Exercise]


class UpdateExerciseDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод получения списка занятий по ид курса.

        :param query: Словарь с course_id.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseDict) -> Response:
        """
        Метод создания занятия.

        :param request: Словарь с title, maxScore, minScore,courseId, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения курса.

        :param exercise_id: Идентификатор занятия.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseDict) -> Response:
        """
        Метод обновления занятия.

        :param exercise_id: Идентификатор занятия.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления занятия.

        :param exercise_id: Идентификатор занятия.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExerciseQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseDict) -> CreateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))