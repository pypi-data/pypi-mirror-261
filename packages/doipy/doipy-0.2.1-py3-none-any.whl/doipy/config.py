from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='doipy_')

    ip: str = '141.5.106.77'
    prefix: str = '21.T11967'
    port: int = 9000


settings = Settings()
