from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import AsyncSession

from backend.app.const import auth_params
from backend.app.database.session import create_async_session

from backend.app.schemas.auth import TokenSchema
from backend.app.services.auth import AuthService

'''
python
   from typing import Annotated
   from fastapi import Depends, FastAPI
   from fastapi.security import OAuth2PasswordRequestForm
   app = FastAPI()
   @app.post("/login")
   def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
       data = {}
       data["scopes"] = []
       for scope in form_data.scopes:
           data["scopes"].append(scope)
       if form_data.client_id:
           data["client_id"] = form_data.client_id
       if form_data.client_secret:
           data["client_secret"] = form_data.client_secret
       return data
'''
router = APIRouter(**auth_params)

@router.post("")
async def authenticate(
    login: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(create_async_session)
    ) -> TokenSchema | None:
    
    return AuthService(session).authenticate(login)