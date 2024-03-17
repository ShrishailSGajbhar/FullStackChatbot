import logging
import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "dev"
    is_testing: bool = bool(0)
    openai_api_key:str 
    # Load the sensetive configs from config..the return variable name must be `model_config`
    model_config = SettingsConfigDict(env_file =DOTENV)

# Let us use lru_cache to cache the settings so that get_settings is only called once.
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()


