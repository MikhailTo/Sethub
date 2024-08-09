from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from backend.app.utils import posts as post_utils
from backend.app.data.posts import Posts as local_posts
from backend.app.core.config import settings

router = APIRouter()

templates = Jinja2Templates(directory=settings.TEMPLATES_FOLDER)


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    # posts = await post_utils.get_posts()
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