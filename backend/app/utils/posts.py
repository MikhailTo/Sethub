
from models.database import database
from sqlalchemy import select, desc, func
from models.posts import posts_table
from models.users import users_table


async def get_posts(post: id):
    query = (
        select(
            [
                posts_table.c.id,
                posts_table.c.user_id,
                posts_table.c.created_at,
                posts_table.c.updated_at,
                posts_table.c.title,
                posts_table.c.description,
                posts_table.c.entries,
                users_table.c.name.label("user_name")
            ]
        )
        .select_from(posts_table.join(users_table))
        .order_by(desc(posts_table.c.created_at))
    )
    return await database.fetch_all(query)

async def get_posts_count():
    query = select([func.count()]).select_from(posts_table)
    return await database.fetch_val(query)