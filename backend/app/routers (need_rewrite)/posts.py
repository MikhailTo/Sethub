from backend.app.utils import posts as post_utils
from fastapi import APIRouter

router = APIRouter()


@router.get("/posts")
async def get_posts():
    total_cout = await post_utils.get_posts_count()
    posts = await post_utils.read_root()
    return {"total_count": total_cout, "results": posts}