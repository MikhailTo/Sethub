from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Text, DateTime
from sqlalchemy.types import ARRAY

from app.models.base import SQLModel

class PostModel(SQLModel):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # created_at: Mapped[DateTime] = mapped_column("created_at", default=datetime.now)
    # updated_at: Mapped[DateTime] = mapped_column("updated_at", default=datetime.now, onupdate=datetime.now)
    title: Mapped[str] = mapped_column("title", String(100))
    description: Mapped[str] = mapped_column("description", Text())
    entries: Mapped[list[str]] = mapped_column("entries", ARRAY(Text()))

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, description={self.description!r})"
