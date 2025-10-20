import pytest
from pydantic import BaseModel,Field, ConfigDict,EmailStr

from tools.fakers import fake


class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    last_name: str =Field(alias="lastName")
    middle_name: str =Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    first_name: str  = Field(alias="firstName", default_factory=fake.first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.first_name)


class CreateUserResponseSchema(BaseModel):
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    emai: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.first_name)

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа бновления пользователя.
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    user: UserSchema

