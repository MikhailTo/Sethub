'''
This module provides functionality for initializing and setting up database connections
and ORM components using SQLAlchemy with asynchronous support.

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
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, async_sessionmaker, create_async_engine
# from sqlalchemy.orm import sessionmaker

from app.core.config import settings
class DatabaseSession():
    """
    A class to initialize and set up the database connection and ORM components.
    """
    def __init__(self, settings: Any = settings) -> None:
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
    
    def __create_async_session_factory(self, async_engine: AsyncEngine, sessionmaker_params: Dict[str, Any]) -> AsyncSession:
        """
        Create a configured session factory.
        """
        async_session_factory = async_sessionmaker(
            **sessionmaker_params,
            class_=AsyncSession,
            bind=async_engine,
        )
        return async_session_factory
    

    def __precreate_async_session(self) -> AsyncSession:

        """
            Precreate an asynchronous session for database operations.

            This method creates a URL, an asynchronous engine, and an asynchronous session factory.
            It then returns the created session.

            Returns:
            AsyncSession: An asynchronous session object ready for database operations.
        """

        url = self.__create_url(self.url_params)

        async_engine = self.__create_async_engine(url, self.engine_params)

        session = self.__create_async_session_factory(async_engine, self.sessionmaker_params)

        return session
        
    def create_async_session(self) -> Iterator[AsyncSession]:
        """
        Create new database async session.

        Yields:
            Database session.
        """
        # This pattern ensures that database transactions are handled safely:
        #   - Changes are committed only if everything succeeds
        #   - Changes are rolled back if an error occurs
        #   - The session is properly managed and cleaned up in all scenarios
        session = self.__precreate_async_session()

        yield session
        # try:
        #     yield session
        #     session.commit()
        # except Exception:
        #     session.rollback()
        #     raise
        # finally:
        #     session.close()
            
    @contextmanager
    def open_async_session(self) -> Iterator[AsyncEngine]:
        """
        Open database async session with context manager.

        Yields:
            Database session.
        """
        return self.create_async_session()
