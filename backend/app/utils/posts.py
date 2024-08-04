
from app.models.database import database
from app.models.posts import posts_table

async def get_posts(post: id):
    query = (
        select(
            []
        )
    )