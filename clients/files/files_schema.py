import pydantic
from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class  CreateFileResponseSchema(BaseModel):
    file: FileSchema

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: pydantic.FilePath = Field(default_factory=lambda: f"{fake.uuid4()}.png")  #
    directory: str = Field(default= "tests")
    upload_file: str

class GetFileResponseSchema(BaseModel):
      file: FileSchema


