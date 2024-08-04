import sqlalchemy
from sqlalchemy import Table, Column, Text, Array, Integer, String, DateTime, MetaData, ForeignKey

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
    Column("entries", Array(Text))
)