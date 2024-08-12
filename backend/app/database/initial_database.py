"""
This module provides functionality for initializing and setting up database connections
and ORM components using SQLAlchemy with asynchronous support.

Arguments:
 - url_params
https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.URL.create

 - create_async_engine_params:
https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#sqlalchemy.ext.asyncio.create_async_engine

 - session_maker_params: 
https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.__init__


Use:
    from backend.app.core.config import settings

    init_db = InitialDatabase(settings)

    SyncSessionLocal = init_db.make_session()
    Base = init_db.generate_base()
"""
from typing import Dict, Any
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base



class InitialDatabase():
    """
    A class to initialize and set up the database connection and ORM components.
    """
    def __init__(self, settings: Any) -> None:
        """
        Initialize the InitialDatabase instance.
        """
        self.settings: Any = settings
        self.url_params: Dict[str, str] = {
            "drivername":   f"{self.settings.DB_DIALECT}+{self.settings.DB_DRIVERNAME}",
            "username":     self.settings.DB_USERNAME,
            "password":     self.settings.DB_PASSWORD,
            "host":         self.settings.DB_HOST,
            "port":         self.settings.DB_PORT,
            "database":     self.settings.DB_NAME
        }
        self.create_async_engine_params: Dict[str, bool] = {
            "echo":         self.settings.DB_ECHO
        }
        self.sessionmaker_params: Dict[str, bool] = {
            "expire_on_commit": self.settings.DB_EXPIRE_ON_COMMIT
        }

    def __create_url(self, url_params: Dict[str, str]) -> URL:
        """
        Create a SQLAlchemy URL object for database connection.
        """
        url = URL.create(**url_params)
        return url

    def __create_engine(self, url: str,
                        create_async_engine_params: Dict[str, bool]) -> AsyncEngine:
        """
        Create an asynchronous SQLAlchemy engine.
        """
        sync_engine = create_async_engine(
            url,
            **create_async_engine_params
            )
        return sync_engine

    def __create_session(self, sync_engine: AsyncEngine, 
                         sessionmaker_params: Dict[str, Any]) -> sessionmaker:
        """
        Create a sync_session_local by sessionmaker for asynchronous database.
        """
        sync_session_local = sessionmaker(
            **sessionmaker_params,
            class_= AsyncSession,
            bind=sync_engine,
        )
        return sync_session_local

    def make_session(self) -> sessionmaker:
        """
        Create and configure a session for database operations.
        """
        url = self.__create_url(self.url_params)
        sync_engine = self.__create_engine(url, self.create_async_engine_params)
        sync_session_local = self.__create_session(sync_engine, self.sessionmaker_params)
        return sync_session_local

    def generate_base(self) -> Any:
        """
        Generate a declarative base for ORM models.
        """
        base = declarative_base()
        return base
