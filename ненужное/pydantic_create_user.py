import uuid

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя
    """
    email: EmailStr
    password: str = Field(min_length=8, max_length=64 )
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(UserSchema):
    """
    Ответ с данными созданного пользователя
    """
    user: UserSchema


