from sqlalchemy.ext.asyncio import create_async_engine
from backend.app.database.url import url_object
from backend.app.config import settings


sync_engine = create_async_engine(url_object, 
                                  echo=settings.DB_ECHO)

