from sqlalchemy import URL

from backend.app.config import settings


# Database URL: dialect+driver://username:password@host:port/database
url_object = URL.create(
    f"{settings.DB_DIALECT}+{settings.DB_DRIVERNAME}",
    username=settings.DB_USERNAME,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)