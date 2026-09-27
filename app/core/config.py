from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "KAUSHAL Intelligence & Certification Platform"
    API_V1_STR: str = "/api"
    SECRET_KEY: str = "development-only-change-before-deployment"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 Hours
    DATABASE_URL: str = "sqlite:///./kaushal.db"
    CORS_ORIGINS: str = (
        "http://localhost:3000,http://localhost:5173,"
        "http://127.0.0.1:3000,http://127.0.0.1:5173"
    )

    @property
    def cors_origins_list(self) -> List[str]:
        configured_origins = [
            origin.strip()
            for origin in self.CORS_ORIGINS.split(",")
            if origin.strip()
        ]
        render_frontend_origins = [
            "https://kaushal-frontend.onrender.com",
            "https://kaushal2-0-1.onrender.com",
        ]
        return list(dict.fromkeys(configured_origins + render_frontend_origins))

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()