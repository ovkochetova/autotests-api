from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

class GetExerciseQueryDict(TypedDict):
    course_id: str

class CreateExerciseDict(TypedDict):
        title: str
        courseId: str
        maxScore: int
        minScore: int
        orderIndex: int
        description: str
        estimatedTime: str

class UpdateExerciseDict(TypedDict):
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

    def create_exercises_api(self, request: CreateExerciseDict) -> Response:
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