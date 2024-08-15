from fastapi import Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from jose import jwt
from sqlalchemy import select
from passlib.context import CryptContext

from backend.app.schemas.auth import UserSchema, CreateUserSchema, TokenSchema
from backend.app.services.base import BaseService, BaseDataManager
from backend.app.models.auth import UserModel
from backend.app.utils.exc import raise_with_log
from backend.app.const import (
    TOKEN_TYPE,
    TOKEN_ALGORITHM
)
from backend.app.core.config import settings

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

    def create_user(self, user: CreateUserSchema) -> None:
        
        user_model = UserModel(
            name=user.name,
            email=user.email,
            hashed_password=self.bcrypt(user.password)
        )
        AuthDataManager(self.session).add_user(user_model)
        
    def authenticate(
            self, login: OAuth2PasswordRequestForm = Depends()
    ):
        user = AuthDataManager(self.session).get_user(login.username)

        if user.hashed_password is None:
            raise_with_log(status.HTTP_401_UNAUTHORIZED, "Incorrect password")
        else:
            if not self.verify(user.hashed_password, login.password):
                raise_with_log(status.HTTP_401_UNAUTHORIZED, "Incorrect password")
            else:
                access_token = self._create_access_token(user.name, user.email)
                return TokenSchema(access_token=access_token, token_type=TOKEN_TYPE)
        return None
    
    def _create_access_token(self, name: str, email: str) -> str:
        
        payload = {
            "name": name,
            "sub": email,
            "expires_at": self._expiration_time()
        }
        
        return jwt.encode(payload, settings.token_key, algorithm=TOKEN_ALGORITHM)

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