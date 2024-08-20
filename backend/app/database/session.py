'''
This module provides functionality for initializing and setting up database connections
and ORM components using SQLAlchemy with asynchronous support.

Note:
 - dsn_params
https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.dsn.create

 - create_async_engine_params:
https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#sqlalchemy.ext.asyncio.create_async_engine

 - session_maker_params: 
https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.__init__

'''
from contextlib import contextmanager
from typing import Dict, Any, Iterator
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, async_sessionmaker, create_async_engine
from app.core.config import settings


class DatabaseSession():
    """
    A class to initialize and set up the database connection and ORM components.
    """
    def __init__(self, settings: Any = settings) -> None:
        """
        Initialize the InitialDatabase instance.
        """
        self.dsn_params = settings.db.params

        self.engine_params = settings.engine.params

        self.sessionmaker_params = settings.session.params


    def __create_dsn(self, dsn_params: Dict[str, str]) -> URL:
        """
        Create a SQLAlchemy dsn (data source name) object for database connection.
        """
        dsn = URL.create(**dsn_params)
        
        return dsn


    def __create_async_engine(self, dsn: str,
                        engine_params: Dict[str, bool]) -> AsyncEngine:
        """
        Create an asynchronous SQLAlchemy engine.
        """
        async_engine = create_async_engine(dsn, **engine_params)
        
        return async_engine
    
    def __precreate_async_session_factory(self, async_engine: AsyncEngine, sessionmaker_params: Dict[str, Any]) -> AsyncSession:
        """
        Precreate an asynchronous session for database operations.
        """
        async_session_factory = async_sessionmaker(
            **sessionmaker_params,
            class_=AsyncSession,
            bind=async_engine,
        )
        return async_session_factory
    
    
    def create_async_session_factory(self) -> AsyncSession:
        """
        Create a configured session factory.
        """

        dsn = self.__create_dsn(self.dsn_params)

        async_engine = self.__create_async_engine(dsn, self.engine_params)

        session_factory = self.__precreate_async_session_factory(async_engine, self.sessionmaker_params)

        return session_factory
        
    # def create_async_session(self) -> Iterator[AsyncSession]:
    #     """
    #     Create new database async session.

    #     Yields:
    #         Database session.
    #     """
    #     # This pattern ensures that database transactions are handled safely:
    #     #   - Changes are committed only if everything succeeds
    #     #   - Changes are rolled back if an error occurs
    #     #   - The session is properly managed and cleaned up in all scenarios
    #     session = self.__precreate_async_session()

    #     yield session
    #     # try:
    #     #     yield session
    #     #     session.commit()
    #     # except Exception:
    #     #     session.rollback()
    #     #     raise
    #     # finally:
    #     #     session.close()
            
    # @contextmanager
    # def open_async_session(self) -> Iterator[AsyncEngine]:
    #     """
    #     Open database async session with context manager.

    #     Yields:
    #         Database session.
    #     """
    #     return self.create_async_session()

class SessionContextManager():
    
    def __init__(self) -> None:
        self.db_session = DatabaseSession(settings)
        self.session_factory = self.db_session.create_async_session_factory()
        self.session = None

    async def __aenter__(self) -> 'SessionContextManager':
        self.session = self.session_factory()
        return self
        
    async def __aexit__(self, *args: object) -> None:
        await self.rollback()

    async def commit(self) -> None:
        await self.session.commit()
        await self.session.close()
        self.session = None

    async def rollback(self) -> None:
        await self.session.rollback()
        await self.session.close()
        self.session = None


async def get_db_session():
    async with SessionContextManager() as session_manager:
        yield session_manager.session