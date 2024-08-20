'''
Configuration Module

This module contains configuration settings and parameters for the backend application.
It may include environment variables, database settings, API keys, and other configuration options.

Usage:
    Import this module to access various configuration settings throughout the application.

Note:
    Ensure that sensitive information is properly secured and not exposed in the codebase.
'''
from os import getenv as get
from typing import Dict
from pathlib import Path
import urllib.parse
from pydantic_settings import BaseSettings

class DatabaseSettings(BaseSettings):

    DIALECT:             str     =   get("DB_DIALECT", "postgresql")
    DRIVERNAME:          str     =   get("DB_DRIVERNAME", "asyncpg")
    USERNAME:            str     =   get("DB_USERNAME", "postgres")
    PASSWORD:            str     =   get("DB_PASSWORD", "postgres")
    HOST:                str     =   get("DB_HOST", "localhost")
    PORT:                int     =   get("DB_PORT", "5432")
    NAME:                str     =   get("DB_NAME", "db_sethub")

    
    @property
    def params(self) -> Dict[str, str]:
        return {
            "drivername": f"{self.DIALECT}+{self.DRIVERNAME}",
            "username": self.USERNAME,
            "password": urllib.parse.quote_plus(self.PASSWORD),
            "host": self.HOST,
            "port": self.PORT,
            "database": self.NAME
        }

class EngineSettings(BaseSettings):

    ECHO: bool = True

    @property
    def params(self) -> Dict[str, bool]:
        return {"echo": self.ECHO}
    
class SessionSettings(BaseSettings):

    AUTOCOMMIT: bool = False
    AUTOFLUSH: bool = False
    EXPIRE_ON_COMMIT: bool = False

    @property
    def params(self) -> Dict[str, bool]:
        return {
            "autocommit": self.AUTOCOMMIT,
            "autoflush": self.AUTOFLUSH,
            "expire_on_commit": self.EXPIRE_ON_COMMIT
        }

class PathSettings(BaseSettings):

    ENV_PRODUCTION_FILE: Path = Path('.env')
    ENV_DEVELOPMENT_FILE: Path = Path('.env.dev')
    ENV_TEST_FILE: Path = Path('.env.test')

    # Folder names
    BACKEND_FOLDER_NAME:    Path    =   Path('backend')
    FRONTEND_FOLDER_NAME:   Path    =   Path('frontend/src')
    APP_FOLDER_NAME:        Path    =   Path('app')
    MEDIA_FOLDER_NAME:      Path    =   Path('media')
    ASSETS_FOLDER_NAME:     Path    =   Path('assets')
    # TEMPLATES_FOLDER_NAME:  Path    =   Path('templates')

    # Paths
    MAIN_PATH:              Path    =   Path(__file__).resolve().parents[3]
    ENV_PATH:               Path    =   MAIN_PATH
    BACKEND_PATH:           Path    =   MAIN_PATH / BACKEND_FOLDER_NAME
    FRONTEND_PATH:          Path    =   MAIN_PATH / FRONTEND_FOLDER_NAME
    MEDIA_PATH:             Path    =   MAIN_PATH / MEDIA_FOLDER_NAME
    APP_PATH:               Path    =   BACKEND_PATH / APP_FOLDER_NAME
    ASSETS_PATH:            Path    =   FRONTEND_PATH / ASSETS_FOLDER_NAME
    # TEMPLATES_PATH:         Path    =   FRONTEND_PATH / TEMPLATES_FOLDER_NAME

class Settings(BaseSettings):

    db: DatabaseSettings = DatabaseSettings()
    engine: EngineSettings = EngineSettings()
    session: SessionSettings = SessionSettings()
    paths: PathSettings = PathSettings()
    
    token_key:  str =   get("TOKEN_KEY", "secret")
    class Config:
        paths: PathSettings = PathSettings()
        env_file = paths.ENV_PATH / paths.ENV_DEVELOPMENT_FILE
        env_file_encoding = "utf-8"

settings = Settings()
