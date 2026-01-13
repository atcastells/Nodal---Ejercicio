from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_URL_SYNC: str
    
    RESEARCH_TASK_DELAY: float
    DFM_TASK_DELAY: float
    
    INITIAL_CREDITS: int
    RESEARCH_COST: int
    DFM_COST: int
    
    MINOR_CHANGE_THRESHOLD: float
    
    class Config:
        env_file = ".env"
        