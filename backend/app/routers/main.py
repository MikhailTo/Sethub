from fastapi import FastAPI, APIRouter, Request, Depends, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import DatabaseSession
from app.services.posts import PostService
from app.data.posts import Posts as local_posts
from app.core.config import settings


staticfiles = StaticFiles(directory=settings.paths.STATIC_PATH)
templates = Jinja2Templates(directory=str(settings.paths.TEMPLATES_PATH))

router = APIRouter()
app = FastAPI()

app.mount("/static", staticfiles, name="static")

@router.get("/", response_class=HTMLResponse)
async def homepage(
    request: Request,
    # session: AsyncSession = Depends(next(DatabaseSession().create_async_session()))
    # session: AsyncSession = Depends(DatabaseSession().open_async_session)
    ):
    # with session_maker() as session:
    # posts = await PostService(session).get_posts()
    posts = local_posts.posts
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