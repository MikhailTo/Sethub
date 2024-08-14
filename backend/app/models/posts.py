from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.types import ARRAY

from backend.app.database.base import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now(), onupdate=func.now()) # !!! Check it
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text())
    entries: Mapped[list[str]] = mapped_column(ARRAY(Text()))

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, description={self.description!r})"
