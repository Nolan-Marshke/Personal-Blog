import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Personal Blog API"
    PROJECT_VERSION: str = "1.0.0"
    
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "article")
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "articles")
    
    # API settings
    API_PREFIX: str = "/api"
    
    # CORS settings
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:3000",  # React default
        "http://localhost:8000",  # FastAPI
        "http://localhost"
    ]
    
    # JWT settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings() 