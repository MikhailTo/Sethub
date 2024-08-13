import uuid
from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import EmailType, PasswordType, UUIDType

from backend.app.database.initial_database import Base
from backend.app.models.posts import Post


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[EmailType] = mapped_column(EmailType(50), unique=True, nullable=False) 
    password: Mapped[PasswordType] = mapped_column(PasswordType(schemes=["pbkdf2_sha512"]), nullable=False)
    
    posts: Mapped[List["Post"]] = relationship(
        default_factory=list,
        back_populates="author",
        lazy='joined',
        cascade="all, delete-orphan",
    )
    keys: Mapped["UserKeys"] = relationship(
        back_populates="user",
        lazy='dynamic',
        cascade="all, delete-orphan",
    )
    tokens: Mapped["UserToken"] = relationship(
        back_populates="user",
        lazy='dynamic',
        cascade="all, delete-orphan",
    )
    groups: Mapped["UserGroup"] = relationship(
        back_populates="users",
        secondary="user_group_association",
    )

class UserKeys(Base):
    __tablename__ = "user_keys"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    public_key: Mapped[str] = mapped_column(String(2000), nullable=False)
    is_revoked: Mapped[bool] = mapped_column(default=False)

    user: Mapped["User"] = relationship("User", back_populates="keys")

class UserToken(Base):
    __tablename__ = "user_tokens"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    token: Mapped[UUIDType] = mapped_column(UUIDType(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    expires: Mapped[datetime] = mapped_column()

    user: Mapped["User"] = relationship("User", back_populates="tokens", lazy='joined')

class UserGroup(Base):
    __tablename__ = "user_groups"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50))

    users: Mapped[List["User"]] = relationship(
        secondary="user_group_association",
        back_populates="groups",
    )
    posts: Mapped[List["Post"]] = relationship(
        back_populates="user_group",
        cascade="all, delete-orphan",
    )

class UserGroupAssociation(Base):
    __tablename__ = "user_group_association"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    group_id: Mapped[int] = mapped_column(ForeignKey("user_groups.id"))