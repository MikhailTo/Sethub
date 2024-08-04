from os import environ
import databases

DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASSWORD", "password")
DB_HOST = environ.get("DB_HOST", "localhost")

#without database for tests
DB_NAME = "sethub-db"
SQLALCHEMY_DATEBASE_URL = (
    f"postgresql://%(DB_USER):%(DB_PASS)@%(DB_HOST):5432/%(DB_NAME)"
)
database = databases.Database(SQLALCHEMY_DATEBASE_URL)