from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, UUID4, field_validator, StringConstraints
from typing_extensions import Annotated

class UserBase(BaseModel):
    ''' This class forms the base structure for user details. 
    It includes basic user information like name and email. 
    '''
    name: str
    email: EmailStr

class TokenBase(BaseModel):
    ''' This class defines the structure for token details. 
    It includes fields for the token itself, expiration time, and token type. 
    It also has a method to convert the UUID token to a hexadecimal string. '''

    # UUID4 - это тип данных, который представляет собой уникальный идентификатор в формате UUID (Universally Unique Identifier). 
    # Он необходим для уникальной идентификации объектов в различных контекстах, таких как базы данных, системы хранения данных и других приложениях.
    # ... - это оператор распаковки, который позволяет распаковать словарь или список в отдельные переменные.
    # alias="access_token" - это псевдоним для поля token, который будет использоваться в ответе.
    token: UUID4 = Field(..., alias="access_token") 
    expires: datetime # это поле, которое представляет собой дату и время истечения срока действия токена.
    # bearer - тип токена, который будет использоваться в запросах, например, в заголовке Authorization, 
    # который будет содержать токен для доступа к защищенным ресурсам, таким как API. 
    # И этот тип токена обычно используется в сочетании с другими типами токенов, 
    # такими как токены обновления или токены доступа. 
    token_type: Optional[str] = "bearer"                    
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
    
    @field_validator("token")
    def hexlify_token(cls, value):
        """ Convert UUID to pure hex string """
        return value.hex

class UserCreate(UserBase):
    ''' This class extends UserBase and is used for sign-up requests. 
    It adds a password field with specific constraints. 
    '''
    password: Annotated[str, StringConstraints(strip_whitespace=True, min_length=8)]

class Login(BaseModel):
    ''' This class defines the structure for login requests, including email and password fields. '''
    email: EmailStr
    password: Annotated[str, StringConstraints(strip_whitespace=True, min_length=8)]

class UserInDBBase(UserBase):
    ''' This class extends UserBase and adds an optional id field. It's configured to work with ORM. '''
    id: Optional[int] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    '''  This class extends UserInDBBase and adds an optional token field. 
    It's used to form the response body with user details and token.
    '''
    token: TokenBase | None = None

class UserKey(BaseModel):
    ''' This class defines the structure for a user's public key. '''
    public_key: str

class UserKeyInDB(BaseModel):
    ''' This class extends UserKey and adds an id field. 
    It's configured to work with ORM and represents a user's key as stored in the database.
    '''
    id: int
    public_key: str

    class Config:
        orm_mode = True