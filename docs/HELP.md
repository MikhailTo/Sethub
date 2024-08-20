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