import uvicorn
from fastapi import FastAPI
from models.database import database
from routers import main, posts
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="../../frontend/static"), name="static")

@app.on_event("startup")
async def startup():
    try:
        await database.connect()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        

@app.on_event("shutdown")
async def shutdown():
        await database.disconnect()

app.include_router(main.router)
app.include_router(posts.router)
# app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)