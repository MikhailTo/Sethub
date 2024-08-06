from typing import Optional
from pydantic import BaseModel, EmailStr, Field, UUID4, datetime

class UserCreate(BaseModel):
    ''' Проверка sign-up запрос '''
    email: EmailStr
    name: str
    password: str

class UserBase(BaseModel):
    ''' Формирует тело ответа с деталями пользователя '''
    id: int
    email: EmailStr
    name: str

class TokenBase(BaseModel):
    ''' Формирует тело ответа с деталями токена '''

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
        allow_population_by_field_name = True

class User(UserBase):
    ''' Формирует тело ответа с деталями пользователя и токеном'''
    token: TokenBase = {}