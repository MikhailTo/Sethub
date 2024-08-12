from os import getenv as get
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DB_DIALECT:     str     =   get("DB_DIALECT", "postgresql")
    DB_DRIVERNAME:  str     =   get("DB_DRIVERNAME", "asyncpg")
    DB_USERNAME:    str     =   get("DB_USERNAME", "postgres") 
    DB_PASSWORD:    str     =   get("DB_PASSWORD", "postgres")
    DB_HOST:        str     =   get("DB_HOST", "localhost")
    DB_PORT:        int     =   get("DB_PORT", 5432)
    DB_NAME:        str     =   get("DB_NAME", "db_sethub")
    DB_ECHO:        bool    =   get("DB_ECHO", True)


    # Folder names
    BACKEND_FOLDER_NAME:    Path = Path('backend')
    FRONTEND_FOLDER_NAME:   Path = Path('frontend')
    APP_FOLDER_NAME:        Path = Path('app')
    MEDIA_FOLDER_NAME:      Path = Path('media')
    STATIC_FOLDER_NAME:     Path = Path('static')
    TEMPLATES_FOLDER_NAME:  Path = Path('templates')
    
    # Paths
    MAIN_PATH:          Path = Path(__file__).resolve().parents[3]
    BACKEND_PATH:       Path = MAIN_PATH / BACKEND_FOLDER_NAME
    FRONTEND_PATH:      Path = MAIN_PATH / FRONTEND_FOLDER_NAME
    APP_PATH:           Path = BACKEND_PATH / APP_FOLDER_NAME
    MEDIA_PATH:         Path = FRONTEND_PATH / MEDIA_FOLDER_NAME
    STATIC_FOLDER:      Path = FRONTEND_PATH / STATIC_FOLDER_NAME
    TEMPLATES_FOLDER:   Path = FRONTEND_PATH / TEMPLATES_FOLDER_NAME

settings = Settings()