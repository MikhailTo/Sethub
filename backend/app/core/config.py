'''
Configuration Module

This module contains configuration settings and parameters for the backend application.
It may include environment variables, database settings, API keys, and other configuration options.

Usage:
    Import this module to access various configuration settings throughout the application.

Note:
    Ensure that sensitive information is properly secured and not exposed in the codebase.
'''
from typing import Dict
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field
import urllib.parse
from os import getenv as get
class DatabaseSettings(BaseSettings):
    
    DB_DIALECT:             str     =   get("DB_DIALECT", "postgresql")
    DB_DRIVERNAME:          str     =   get("DB_DRIVERNAME", "asyncpg")
    DB_USERNAME:            str     =   get("DB_USERNAME", "postgres")
    DB_PASSWORD:            str     =   get("DB_PASSWORD", "postgres")
    DB_HOST:                str     =   get("DB_HOST", "localhost")
    DB_PORT:                int     =   get("DB_PORT", "5432")
    DB_NAME:                str     =   get("DB_NAME", "db_sethub")
    
    @property
    def params(self) -> Dict[str, str]:
        return {
            "drivername": f"{self.DB_DIALECT}+{self.DB_DRIVERNAME}",
            "username": self.DB_USERNAME,
            "password": urllib.parse.quote_plus(self.DB_PASSWORD),
            "host": self.DB_HOST,
            "port": self.DB_PORT,
            "database": self.DB_NAME
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

    #  # Folder names
    # BACKEND_FOLDER_NAME:    Path    =   Path('backend')
    # FRONTEND_FOLDER_NAME:   Path    =   Path('frontend')
    # APP_FOLDER_NAME:        Path    =   Path('app')
    # MEDIA_FOLDER_NAME:      Path    =   Path('media')
    # STATIC_FOLDER_NAME:     Path    =   Path('static')
    # TEMPLATES_FOLDER_NAME:  Path    =   Path('templates')

    # # Paths
    # MAIN_PATH:              Path    =   Path(__file__).resolve().parents[3]
    # BACKEND_PATH:           Path    =   MAIN_PATH / BACKEND_FOLDER_NAME
    # FRONTEND_PATH:          Path    =   MAIN_PATH / FRONTEND_FOLDER_NAME
    # APP_PATH:               Path    =   BACKEND_PATH / APP_FOLDER_NAME
    # MEDIA_PATH:             Path    =   FRONTEND_PATH / MEDIA_FOLDER_NAME
    # STATIC_PATH:            Path    =   FRONTEND_PATH / STATIC_FOLDER_NAME
    # TEMPLATES_PATH:         Path    =   FRONTEND_PATH / TEMPLATES_FOLDER_NAME
    BACKEND_FOLDER: Path = Path('backend')
    FRONTEND_FOLDER: Path = Path('frontend')
    APP_FOLDER: Path = Path('app')
    MEDIA_FOLDER: Path = Path('media')
    STATIC_FOLDER: Path = Path('static')
    TEMPLATES_FOLDER: Path = Path('templates')
    
    @property
    def ENV_PATH(self) -> Path:
        return self.MAIN_PATH
    
    @property
    def MAIN_PATH(self) -> Path:
        return Path(__file__).resolve().parents[3]

    @property
    def BACKEND_PATH(self) -> Path:
        return self.MAIN_PATH / self.BACKEND_FOLDER

    @property
    def FRONTEND_PATH(self) -> Path:
        return self.MAIN_PATH / self.FRONTEND_FOLDER

    @property
    def APP_PATH(self) -> Path:
        return self.BACKEND_PATH / self.APP_FOLDER

    @property
    def MEDIA_PATH(self) -> Path:
        return self.FRONTEND_PATH / self.MEDIA_FOLDER

    @property
    def STATIC_PATH(self) -> Path:
        return self.FRONTEND_PATH / self.STATIC_FOLDER

    @property
    def TEMPLATES_PATH(self) -> Path:
        return self.FRONTEND_PATH / self.TEMPLATES_FOLDER

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
