'''
Configuration Module

This module contains configuration settings and parameters for the backend application.
It may include environment variables, database settings, API keys, and other configuration options.

Usage:
    Import this module to access various configuration settings throughout the application.

Note:
    Ensure that sensitive information is properly secured and not exposed in the codebase.
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import init_env

from os import getenv as get
from typing import Dict
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ValidationError
from pydantic import Field
import urllib.parse


class DatabaseSettings(BaseSettings):
    
    DIALECT:             str     =   get("DB_DIALECT", "postgresql")
    DRIVERNAME:          str     =   get("DB_DRIVERNAME", "asyncpg")
    USERNAME:            str     =   get("DB_USERNAME", "postgres")
    PASSWORD:            str     =   get("DB_PASSWORD", "postgres")
    HOST:                str     =   get("DB_HOST", "localhost")
    PORT:                int     =   get("DB_PORT", "5432")
    NAME:                str     =   get("DB_NAME", "db_sethub")

    # DIALECT: str = Field("postgresql", env="DB_DIALECT")
    # DRIVERNAME: str = Field("asyncpg", env="DB_DRIVERNAME")
    # USERNAME: str = Field("postgres", env="DB_USERNAME")
    # PASSWORD: str = Field("postgres", env="DB_PASSWORD")
    # HOST: str = Field("localhost", env="DB_HOST")
    # PORT: int = Field(5432, env="DB_PORT")
    # NAME: str = Field("db_sethub", env="DB_NAME")
    
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
    ENV_TEST_FILE: Path = Path('.env.example')

    #  # Folder names
    # BACKEND_FOLDER_NAME:    Path    =   Path('backend')
    # FRONTEND_FOLDER_NAME:   Path    =   Path('frontend')
    # APP_FOLDER_NAME:        Path    =   Path('app')
    # MEDIA_FOLDER_NAME:      Path    =   Path('media')
    # STATIC_FOLDER_NAME:     Path    =   Path('static')
    # TEMPLATES_FOLDER_NAME:  Path    =   Path('templates')

    
    BACKEND_FOLDER: Path = Path('backend')
    FRONTEND_FOLDER: Path = Path('frontend')
    APP_FOLDER: Path = Path('app')
    MEDIA_FOLDER: Path = Path('media')
    STATIC_FOLDER: Path = Path('static')
    TEMPLATES_FOLDER: Path = Path('templates')
    # Paths
    MAIN_PATH:              Path    =   Path(__file__).resolve().parents[3]
    ENV_PATH:               Path    =   MAIN_PATH
    BACKEND_PATH:           Path    =   MAIN_PATH / BACKEND_FOLDER
    FRONTEND_PATH:          Path    =   MAIN_PATH / FRONTEND_FOLDER
    APP_PATH:               Path    =   BACKEND_PATH / APP_FOLDER
    MEDIA_PATH:             Path    =   FRONTEND_PATH / MEDIA_FOLDER
    STATIC_PATH:            Path    =   FRONTEND_PATH / STATIC_FOLDER
    TEMPLATES_PATH:         Path    =   FRONTEND_PATH / TEMPLATES_FOLDER
    # @property
    # def ENV_PATH(self) -> Path:
    #     return self.MAIN_PATH
    
    # @property
    # def MAIN_PATH(self) -> Path:
    #     return Path(__file__).resolve().parents[3]

    # @property
    # def BACKEND_PATH(self) -> Path:
    #     return self.MAIN_PATH / self.BACKEND_FOLDER

    # @property
    # def FRONTEND_PATH(self) -> Path:
    #     return self.MAIN_PATH / self.FRONTEND_FOLDER

    # @property
    # def APP_PATH(self) -> Path:
    #     return self.BACKEND_PATH / self.APP_FOLDER

    # @property
    # def MEDIA_PATH(self) -> Path:
    #     return self.FRONTEND_PATH / self.MEDIA_FOLDER

    # @property
    # def STATIC_PATH(self) -> Path:
    #     return self.FRONTEND_PATH / self.STATIC_FOLDER

    # @property
    # def TEMPLATES_PATH(self) -> Path:
    #     return self.FRONTEND_PATH / self.TEMPLATES_FOLDER

class Settings(BaseSettings):
    
    
    db: DatabaseSettings = DatabaseSettings()
    engine: EngineSettings = EngineSettings()
    session: SessionSettings = SessionSettings()
    paths: PathSettings = PathSettings()

    token_key:  str =   get("TOKEN_KEY", "secret")
   
    class Config:
        paths: PathSettings = PathSettings()
        env_file = paths.ENV_PATH / paths.ENV_TEST_FILE
        env_file_encoding = "utf-8"

settings = Settings()

paths= settings.paths
print(type(paths.STATIC_PATH))
print(type(str(paths.STATIC_PATH)))
print(paths.STATIC_PATH)
print(str(paths.STATIC_PATH))
print(str(paths.STATIC_PATH) == paths.STATIC_PATH)
