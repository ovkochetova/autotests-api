from typing import Self

from pydantic import BaseModel, HttpUrl, FilePath,DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow", # допускаются зависимости сверх комплекта
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_result_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:
        allure_result_dir = DirectoryPath("./allure-results")
        allure_result_dir.mkdir(exist_ok=True)

        return Settings(allure_result_dir=allure_result_dir)

settings = Settings.initialize()
print(settings.model_dump().items())






