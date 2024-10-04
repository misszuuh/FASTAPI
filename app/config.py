from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_password: str = "localhost"
    database_username: str = "postgres"
    secret_key: str = "2345676tdgfcfgg"
    zubeda: str = "Hellooooo"


settings = Settings()