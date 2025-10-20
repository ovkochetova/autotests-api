from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake

class GetExerciseQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры запроса на получение списка заданий.
    """
    course_id: str = Field(alias = "courseId")


class CreateExerciseSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory= fake.sentence)
    description: str = Field(default_factory= fake.text)
    course_id: str = Field(alias = "courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias = "maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias = "minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias = "orderIndex", default_factory=fake.integer)
    estimated_time: str = Field(alias = "estimatedTime", default_factory=fake.estimated_time)


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
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос задания по ид курса.
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос задания по ид задания.
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    description: str = Field(default_factory=fake.text)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema