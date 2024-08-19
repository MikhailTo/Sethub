import uvicorn
from fastapi import FastAPI

from app.const import app_params, uvicorn_params
from app.routers import main, auth, posts


app = FastAPI(**app_params)


app.include_router(main.router)
app.include_router(posts.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app, **uvicorn_params)