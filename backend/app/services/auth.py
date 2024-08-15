from fastapi import Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy import select
from passlib.context import CryptContext

from backend.app.schemas.auth import UserSchema
from backend.app.services.base import BaseService, BaseDataManager
from backend.app.database.models import UserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashingMixin:
    """Hashing and verifying passwords."""

    @staticmethod
    def bcrypt(password: str) -> str:
        """Generate a bcrypt hashed password."""

        return pwd_context.hash(password)

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        """Verify a password against a hash."""

        return pwd_context.verify(plain_password, hashed_password)
    
class AuthService(HashingMixin, BaseService):

    def authenticate(
            self, login: OAuth2PasswordRequestForm = Depends()
    ):
        user = AuthDataManager(self.session).get_user(login.username)

class AuthDataManager(BaseDataManager):
    def add_user(self, user: UserModel) -> None:
        """Add user to tadabase."""
        self.add_one(user)
    
    def get_user(self, email: str) -> UserSchema:

        model = self.get_one(select(UserModel).where(UserModel.email == email))

        if not isinstance(model, UserModel):
            raise_with_log(status.HTTP_404_NOT_FOUND, "User not found")

        return UserSchema(
            name=model.name,
            email=model.email,
            hashed_password=model.hashed_password
        )