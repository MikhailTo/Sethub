import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.models.database import database
from app.routers import main, posts, users
from app.core.config import settings

app = FastAPI()

app.mount("/static", StaticFiles(directory=settings.STATIC_FOLDER), name="static")

# @app.on_event("startup")
# async def startup():
#         await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#         await database.disconnect()

app.include_router(main.router)
app.include_router(posts.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)