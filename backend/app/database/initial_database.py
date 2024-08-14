'''
This module provides functionality for initializing and setting up database connections
and ORM components using SQLAlchemy with asynchronous support.

Usage:

    from backend.app.core.config import settings
    from backend.app.database.initial_database import InitialDatabase

    init_db = InitialDatabase(settings)

    SyncSessionLocal = init_db.make_sync_session() # or init_db.make_session()

    Base = init_db.generate_base()

Note:
 - url_params
https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.URL.create

 - create_async_engine_params:
https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#sqlalchemy.ext.asyncio.create_async_engine

 - session_maker_params: 
https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.__init__

'''
from contextlib import contextmanager
from typing import Dict, Any, Iterator
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.app.core.config import settings

class InitialDatabase():
    """
    A class to initialize and set up the database connection and ORM components.
    """
    def __init__(self, settings: Any) -> None:
        """
        Initialize the InitialDatabase instance.
        """
        self.url_params = settings.url_params
        self.engine_params = settings.engine_params
        self.sessionmaker_params = settings.sessionmaker_params

    def __create_url(self, url_params: Dict[str, str]) -> URL:
        """
        Create a SQLAlchemy URL object for database connection.
        """
        url = URL.create(**url_params)
        return url

    def __create_sync_engine(self, url: str,
                        engine_params: Dict[str, bool]) -> AsyncEngine:
        """
        Create an asynchronous SQLAlchemy engine.
        """
        sync_engine = create_async_engine(
            url,
            **engine_params
            )
        return sync_engine

    def __create_sync_session(self, sync_engine: AsyncEngine,
                         sessionmaker_params: Dict[str, Any]) -> Iterator[AsyncSession]:
        """
        Create new database sync session.

        Yields:
            Database session.
        """
        sync_session_local = sessionmaker(
            **sessionmaker_params,
            class_= AsyncSession,
            bind=sync_engine,
        )
        try:
            yield sync_session_local
            sync_session_local.commit()
        except Exception:
            sync_session_local.rollback()
            raise
        finally:
            sync_session_local.close()


    @contextmanager
    def open_sync_session(self) -> Iterator[AsyncEngine]:
        """
        Create new database sync session with context manager.

        Yields:
            Database session.
        """
        url = self.__create_url(self.url_params)
        sync_engine = self.__create_sync_engine(url, self.engine_params)
        return self.__create_sync_session(sync_engine, self.sessionmaker_params)
    

    def generate_base(self) -> Any:
        """
        Generate a declarative base for ORM models.
        """
        base = declarative_base()
        return base

Base = InitialDatabase(settings).generate_base()