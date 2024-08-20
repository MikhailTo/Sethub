import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.const import app_params, uvicorn_params
from app.routers import main, auth, posts
from app.core.config import settings

assets = StaticFiles(directory=settings.paths.ASSETS_PATH)

app = FastAPI(**app_params)
app.mount("/assets", assets, name="assets")

app.include_router(main.router)
app.include_router(posts.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app, **uvicorn_params)