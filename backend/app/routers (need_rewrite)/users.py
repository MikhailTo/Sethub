from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from backend.app.schemas import users
from backend.app.utils import users as users_utils

router = APIRouter()

@router.post("/sign-up", response_model=users.User)
async def create_user(user: users.UserCreate):
    db_user = await users_utils.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return await users_utils.create_user(user=user)

@router.post("/auth", response_model=users.TokenBase)
async def auth(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_utils.get_user_by_email(email=form_data.username)

    if not user:
        raise HTTPException(
            status_code=400, 
            detail="Incorrect username or password")
    
    if not users_utils.validate_password(
        form_data.password, 
        hashed_password=user["hashed_password"]):
        raise HTTPException(
            status_code=400, 
            detail="Incorrect username or password")
    
    return await users_utils.create_user_token(user_id=user["id"])