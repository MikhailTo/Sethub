from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


SyncSessionLocal = sessionmaker(
    expire_on_commit=False,
    class_= AsyncSession,
    bind=sync_engine,
)
