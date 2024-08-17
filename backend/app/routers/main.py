from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.session import DatabaseSession
from backend.app.services.posts import PostService
# from backend.app.data.posts import Posts as local_posts
from backend.app.core.config import settings

router = APIRouter()
app = FastAPI()

app.mount("/static", StaticFiles(directory=settings.STATIC_FOLDER), name="static")
templates = Jinja2Templates(directory=settings.TEMPLATES_FOLDER)


@router.get("/", response_class=HTMLResponse)
async def homepage(
    request: Request,
    session: AsyncSession = Depends(DatabaseSession().create_async_session)):
    posts = PostService(session).get_posts()
    # posts = local_posts.posts
    context = {
        "title": "Sethub",
        "posts": posts
        }
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context
    )


@router.get("/create", response_class=HTMLResponse)
async def create_list(request: Request):
    context = {
        "title": "Create New List - Sethub"
    }
    return templates.TemplateResponse(
        request=request,
        name="create_post.html",
        context=context
    )

@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str = ""):
    context = {
        "title": "Search - Sethub",
        "query": q
    }
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context=context
    )

@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    context = {
        "title": "About - Sethub",
    }
    return templates.TemplateResponse(
        request=request,
        name = "about.html",
        context=context)
    
@router.get("/auth", response_class=HTMLResponse)
async def auth(request: Request):
    context = {
        "title": "Auth",
    }
    return templates.TemplateResponse(
        request=request,
        name = "auth.html",
        context=context)