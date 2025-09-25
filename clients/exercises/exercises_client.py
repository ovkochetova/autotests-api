from httpx import Response
from clients.api_client import APIClient


from clients.exercises.exercises_schema import GetExerciseQuerySchema, UpdateExerciseSchema, CreateExerciseSchema, \
    GetExercisesResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client



class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExerciseQuerySchema) -> Response:
        """
        Метод получения списка занятий по ид курса.

        :param query: Словарь с course_id.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseSchema) -> Response:
        """
        Метод создания занятия.

        :param request: Словарь с title, maxScore, minScore,courseId, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения курса.

        :param exercise_id: Идентификатор занятия.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseSchema) -> Response:
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

    def get_exercises(self, query: GetExerciseQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseSchema) -> CreateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))