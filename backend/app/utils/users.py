import random
import string
import hashlib
from datetime import datetime, timedelta
from sqlalchemy import and_

from backend.app.database.engine import database
from backend.app.models.users import tokens_table, users_table
from backend.app.schemas import users as user_schema

# Алгоритм в порядке выполнения для работы с пользователями в Sethub:
# Этот порядок отражает типичный жизненный цикл взаимодействия с пользователем в системе, 
# начиная с регистрации и заканчивая обновлением токена для поддержания сессии.

# Регистрация нового пользователя (create_user):
# - Генерация случайной соли (get_random_string)
# - Хеширование пароля с солью (hash_password)
# - Вставка данных пользователя в базу данных (insert_user)
# - Создание токена для нового пользователя (create_user_token)
# - Возврат информации о пользователе с токеном (user_schema.User)

# Аутентификация пользователя:
# - Получение пользователя по email (get_user_by_email)
# - Проверка пароля (validate_password)
# - При успешной проверке, создание нового токена (create_user_token)

# Проверка токена пользователя:
# - Получение пользователя по токену (get_user_by_token)
# - Проверка срока действия токена (is_token_expired)

# Обновление токена:
# - Создание нового токена для существующего пользователя (create_user_token)


def get_random_string(length: int = 12) -> str:
    ''' Генерирует случайную строку '''
    return "".join(random.choice(string.ascii_letters) for _ in range(length))

def hash_password(password: str, salt: str = None) -> str:
    ''' Хеширует пароль с солью '''
    if salt is None:
        salt = get_random_string()
    
    enc = hashlib.pbkdf2_hmac(              # Это функция из модуля hashlib, которая используется для хеширования паролей с помощью алгоритма PBKDF2.
        hash_name="sha256",                 # Это название алгоритма хеширования, который будет использоваться. В данном случае, используется алгоритм SHA-256.
        password=password.encode("utf-8"),  # Это пароль, который нужно хешировать.
        salt=salt.encode("utf-8"),          # Это соль, которая добавляется к паролю перед хешированием.
        iterations=100_000,                 # Это количество итераций, которые будут использованы для хеширования пароля.
    )
    return enc.hex()

def validate_password(password: str, hashed_password: str) -> bool:
    ''' Проверяет, что пароль совпадает с хешированным паролем '''
    salt, hashed = hashed_password.split("$")
    return hashed == hash_password(password, salt)

async def get_user_by_email(email: str) -> user_schema.User:
    ''' Возвращает пользователя по email '''
    query = users_table.select().where(users_table.c.email == email)
    return await database.fetch_one(query)

async def get_user_by_token(token: str) -> user_schema.User:
    ''' Возвращает пользователя по токену '''
    query = tokens_table.join(users_table).select().where(  # Это запрос, который объединяет таблицы tokens_table и users_table по условию, что поле token в таблице tokens_table соответствует значению token в запросе.
        and_(tokens_table.c.token == token,                 # Это условие, которое проверяет, что токен соответствует токену в базе данных.
             tokens_table.c.expires > datetime.now()        # Это условие, которое проверяет, что токен не истек.
            ) 
    )
    return await database.fetch_one(query)

async def create_user_token(user_id: int) -> user_schema.TokenBase:
    ''' Создает токен для пользователя '''
    query = (
        tokens_table.insert() #  
        .values(expires=datetime.now() + timedelta(weeks=2),  # новый токен для пользователя с истечением срока действия через 2 недели.
                user_id=user_id) # 
        .returning(tokens_table.c.token, tokens_table.c.expires) # Этот код возвращает только поля token и expires из таблицы tokens_table.
    )
    return await database.fetch_one(query)

async def create_user(user: user_schema.UserCreate) -> user_schema.User:
    ''' Создает нового пользователя в базе данных '''
    salt = get_random_string()
    hashed_password = hash_password(user.password, salt)
    query = users_table.insert().values(
        email=user.email,
        name=user.name,
        hashed_password=f"{salt}${hashed_password}",
    )
    user_id = await database.execute(query)
    token = await create_user_token(user_id)
    token_dict = {"token": token["token"],  "expires": token["expires"]}
    return {**user.model_dump(), "id": user_id, "token": token_dict}
    # Cоздает новый словарь, содержащий все поля пользователя из Pydantic модели, 
    # а также добавляет к нему ID пользователя и информацию о токене. 
    # Это удобный способ подготовить полные данные пользователя для возврата из функции.
