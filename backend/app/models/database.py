from os import environ
import databases
from backend.app.core.config import settings


DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_PORT = environ.get("DB_PORT", 5432)
DB_NAME = "sethub-db"

database_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

SQLALCHEMY_DATEBASE_URL = (
    database_url
)

database = databases.Database(SQLALCHEMY_DATEBASE_URL)
