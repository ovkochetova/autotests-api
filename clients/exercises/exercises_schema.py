from pydantic import BaseModel, Field, ConfigDict


class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    course_id: str = Field(alias = "courseId")


class CreateExerciseSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    description: str
    course_id: str = Field(alias = "courseId")
    max_score: int = Field(alias = "maxScore")
    min_score: int = Field(alias = "minScore")
    order_index: int | None = Field(alias = "orderIndex")
    estimated_time: str = Field(alias = "estimatedTime")


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    description: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercises: list[ExerciseSchema]

class UpdateExerciseSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    description: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    estimated_time: str = Field(alias="estimatedTime")
