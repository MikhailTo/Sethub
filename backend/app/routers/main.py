from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# from app.data.posts import Posts as local_posts
from app.core.config import settings

templates = Jinja2Templates(directory=str(settings.paths.TEMPLATES_PATH))

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    context = {
        "title": "Sethub",
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