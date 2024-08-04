import sqlalchemy
from sqlalchemy import Table, Column, Boolean, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("email", String(40), unique=True, index=True),
    Column("hashed_password", String()),
    Column("is_active",
            Boolean(),
            server_default=sqlalchemy.sql.expression.true(),
            nullable=False
        )
)

tokens_table = Table(
    "tokens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("expires", DateTime()),
    Column("token",
           UUID(as_uuid=False),
           server_default=sqlalchemy.text("uuid_generate_v4()"),
           unique=True,
           nullable=False,
           index=True
        )
)