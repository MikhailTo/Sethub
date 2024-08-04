import sqlalchemy
from sqlalchemy import Table, Column, Text, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.types import ARRAY
from .users import users_table

metadata = MetaData()

posts_table = Table(
    "lists",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey(users_table.c.id)),
    Column("created_at", DateTime()),
    Column("updated_at", DateTime()),
    Column("title", String(100)),
    Column("description", Text()),
    Column("entries", ARRAY(Text))
)