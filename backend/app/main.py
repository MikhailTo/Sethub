import uvicorn
from fastapi import FastAPI

from backend.app.const import app_params, uvicorn_params
from backend.app.routers import main, users, posts


app = FastAPI(**app_params)

app.include_router(main.router)
app.include_router(posts.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, **uvicorn_params)