import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Read environment variables"""
    DAILY_EXPENSES: str
    USER_BEHAVIOR_URL: str
    WEEKLY_EXPENSES: str
    MONTHLY_EXPENSES: str
    CATEGORY_EXPENSES: str
    
    class Config:
        env_file = ".env"

settings = Settings()
print(settings) # debug