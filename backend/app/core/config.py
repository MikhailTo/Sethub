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

class DatabaseSettings(BaseSettings):
    
    
    DIALECT: str = Field("postgresql", env="DB_DIALECT")
    DRIVERNAME: str = Field("asyncpg", env="DB_DRIVERNAME")
    USERNAME: str = Field("postgres", env="DB_USERNAME")
    PASSWORD: str = Field("postgres", env="DB_PASSWORD")
    HOST: str = Field("localhost", env="DB_HOST")
    PORT: int = Field(5432, env="DB_PORT")
    NAME: str = Field("db_sethub", env="DB_NAME")
    

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

    BACKEND_FOLDER: Path = Path('backend')
    FRONTEND_FOLDER: Path = Path('frontend')
    APP_FOLDER: Path = Path('app')
    MEDIA_FOLDER: Path = Path('media')
    STATIC_FOLDER: Path = Path('static')
    TEMPLATES_FOLDER: Path = Path('templates')
    
    @property
    def ENV_PATH(self, ENV_FILE) -> Path:
        return self.MAIN_PATH / ENV_FILE
    
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

    token_key: str = Field("", env="TOKEN_KEY")
    
    class Config:
        
        
        paths: PathSettings = PathSettings()
        env_file =  paths.ENV_PATH(paths.ENV_DEVELOPMENT_FILE)
        env_file_encoding = "utf-8"

settings = Settings()
