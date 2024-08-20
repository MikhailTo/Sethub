import pytest
from sqlalchemy import text
from app.database.session import DatabaseSession, SessionContextManager
from app.core.config import settings

# For tests copy to config
    # DIALECT: str = get("DB_DIALECT", "sqlite")
    # DRIVERNAME: str = get("DB_DRIVERNAME", "aiosqlite")
    # NAME: str = get("DB_NAME", ":memory:")  # Использование in-memory SQLite

    # @property
    # def params(self) -> Dict[str, str]:
    #     return {
    #         "drivername": f"{self.DIALECT}+{self.DRIVERNAME}",
    #         "database": self.NAME
    #     }

db_params = settings.db

#Override the database configuration for tests
db_params.DIALECT = "sqlite"
db_params.DRIVERNAME = "aiosqlite"
db_params.NAME = ":memory:"

@pytest.mark.asyncio
async def test_database_session():
    db_session = DatabaseSession()
    session_factory = db_session.create_async_session_factory()
    
    async with session_factory() as session:
        result = await session.execute(text("SELECT 1"))
        assert result.scalar() == 1

@pytest.mark.asyncio
async def test_session_context_manager():
    async with SessionContextManager() as session_manager:
        result = await session_manager.session.execute(text("SELECT 1"))
        assert result.scalar() == 1
