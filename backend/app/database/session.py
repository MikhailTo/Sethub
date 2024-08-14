'''
This module provides functionality for initializing and setting up database connections
and ORM components using SQLAlchemy with asynchronous support.

Usage:

    from backend.app.core.config import settings
    from backend.app.database.session import DatabaseSession

    AsyncSessionLocal: Iterator[AsyncEngine] = DatabaseSession(settings).open_async_session()


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
from sqlalchemy.orm import sessionmaker

class DatabaseSession():
    """
    A class to initialize and set up the database connection and ORM components.
    """
    def __init__(self, settings: Any) -> None:
        """
        Initialize the InitialDatabase instance.
        """
        self.url_params = settings.db.params

        self.engine_params = settings.engine.params

        self.sessionmaker_params = settings.session.params


    def __create_url(self, url_params: Dict[str, str]) -> URL:
        """
        Create a SQLAlchemy URL object for database connection.
        """
        url = URL.create(**url_params)

        return url


    def __create_async_engine(self, url: str,
                        engine_params: Dict[str, bool]) -> AsyncEngine:
        """
        Create an asynchronous SQLAlchemy engine.
        """
        async_engine = create_async_engine(url, **engine_params)

        return async_engine


    def __create_async_session(self, async_engine: AsyncEngine,
                         sessionmaker_params: Dict[str, Any]) -> Iterator[AsyncSession]:
        """
        Create new database async session.

        Yields:
            Database session.
        """
        async_session_local = sessionmaker(
            **sessionmaker_params,
            class_= AsyncSession,
            bind=async_engine,
        )
        
        # This pattern ensures that database transactions are handled safely:
        #   - Changes are committed only if everything succeeds
        #   - Changes are rolled back if an error occurs
        #   - The session is properly managed and cleaned up in all scenarios

        session = async_session_local()

        try:
            yield session

            session.commit()

        except Exception:
            session.rollback()
            
            raise

        finally:
            session.close()


    @contextmanager
    def open_async_session(self) -> Iterator[AsyncEngine]:
        """
        Open database async session with context manager.

        Yields:
            Database session.
        """
        url = self.__create_url(self.url_params)
 
        async_engine = self.__create_async_engine(url, self.engine_params)
 
        return self.__create_async_session(async_engine, self.sessionmaker_params)
