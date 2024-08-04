import uvicorn
from fastapi import FastAPI

from app.models.database import database
from app.routers import main, posts, users

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="../../frontend/static"), name="static")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(main.router)
app.include_router(users.router)
app.include_router(posts.router)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)