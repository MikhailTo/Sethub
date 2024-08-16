from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.const import auth_params
from backend.app.database.session import DatabaseSession

from backend.app.schemas.auth import TokenSchema
from backend.app.services.auth import AuthService

router = APIRouter(**auth_params)

@router.post("")
async def authenticate(
    login: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(DatabaseSession().create_async_session)
    ) -> TokenSchema | None:
    """User authentication.

    Raises:
        HTTPException: 401 Unauthorized
        HTTPException: 404 Not Found

    Returns:
        Access token.
    """
    return AuthService(session).authenticate(login)