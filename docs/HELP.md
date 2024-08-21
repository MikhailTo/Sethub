Для вывода главной страницы, когда frontend разрабатывается отдельно на Vite, можно использовать следующий подход:

В FastAPI бэкенде создайте эндпоинт для корневого URL:

```
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return FileResponse("path/to/index.html")
```

main.py
В Vite проекте настройте прокси для API запросов:
export default defineConfig({
  server: {
    proxy: {
      '/api': 'http://localhost:8000'
    }
  }
})
```

vite.config.js
Соберите frontend проект и скопируйте собранные файлы в директорию, доступную для FastAPI.

Настройте FastAPI для обслуживания статических файлов:
```
from fastapi.staticfiles import StaticFiles

app.mount("/assets", StaticFiles(directory="path/to/frontend/dist/assets"), name="static")
```

main.py
Этот подход позволит вам разрабатывать frontend отдельно, но при этом обслуживать его через FastAPI бэкенд.

Для запуска всего проекта вам нужно выполнить следующие шаги:

Запустите backend:
```cd backend
uvicorn app.main:app --reload```


Запустите frontend (предполагая, что вы используете Vite):
```cd frontend
npm run dev```


Если вы используете Docker, вы можете запустить всё одной командой:
```docker-compose up```

Убедитесь, что у вас настроен файл docker-compose.yml в корне проекта, который определяет сервисы для backend и frontend.

После запуска, ваше приложение будет доступно по адресу, указанному в конфигурации (обычно http://localhost:3000 для frontend и http://localhost:8000 для backend API).
Не забудьте также настроить переменные окружения и базу данных согласно вашей конфигурации в backend/app/core/config.py.



Создание базы:
```
CREATE SCHEMA IF NOT EXISTS sethub;

CREATE TABLE IF NOT EXISTS sethub.posts (
    post_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    released INTEGER NOT NULL,
    rating NUMERIC(2, 1) NOT NULL
);

CREATE TABLE IF NOT EXISTS sethub.users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    hashed_password TEXT NOT NULL,
    UNIQUE(email)
);

# app/cli.py

import click

from app.backend.session import create_session
from app.schemas.auth import CreateUserSchema
from app.services.auth import AuthService


@click.group()
def main() -> None:
    pass


@main.command()
@click.option("--name", type=str, help="User name")
@click.option("--email", type=str, help="Email")
@click.option("--password", type=str, help="Password")
def create_user(name: str, email: str, password: str) -> None:
    user = CreateUserSchema(name=name, email=email, password=password)
    session = next(create_session())
    AuthService(session).create_user(user)

#$ myapi --name 'test user' --email test_user@myapi.com --password password
```
