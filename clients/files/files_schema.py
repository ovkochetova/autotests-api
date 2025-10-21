import pydantic
from pydantic import BaseModel, HttpUrl, Field, FilePath
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
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")  #
    directory: str = Field(default= "tests")
    upload_file: FilePath

class GetFileResponseSchema(BaseModel):
      file: FileSchema


