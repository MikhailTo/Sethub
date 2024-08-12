import uvicorn
from fastapi import FastAPI

from backend.app.routers import main, posts, users

app = FastAPI()

app.include_router(main.router)
app.include_router(posts.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)