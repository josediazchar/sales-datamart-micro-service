from pydantic import (
    PostgresDsn,
    computed_field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    """
    """

    SECRET_KEY: str

    PROJECT_NAME: str = 'CELES Sales datamart'
    API_V1_STR: str = "/api/v1"

    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""

    FIREBASE_APIKEY: str
    FIREBASE_AUTHDOMAIN: str
    FIREBASE_PROJECTID: str
    FIREBASE_STORAGEBUCKET: str
    FIREBASE_MESSAGINGSENDERID: str
    FIREBASE_APPID: str
    FIREBASE_CREDENTIALS_PATH: str


    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

settings = Settings()  # type: ignore