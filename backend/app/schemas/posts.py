from typing import Optional
from pydantic import BaseModel

class PostBase(BaseModel):
    ''' This is the base class for post-related schemas. '''
    title: str
    content: str
    group_id: int

class PostInDBBase(PostBase):
    ''' This class extends PostBase and adds an optional 'id' field. '''
    id: Optional[int] = None

    class Config:
        orm_mode = True

class PaginatedPosts(BaseModel):
    ''' This class is used for paginated responses. '''
    total_count: int
    per_page: int
    posts: list[PostInDBBase]

class PostKeyInDB(BaseModel):
    ''' This class represents an encrypted key associated with a post as it exists in the database. '''
    encrypted_key: str

    class Config:
        orm_mode = True

class PostKey(BaseModel):
    ''' Similar to PostKeyInDB, but likely used for input/output operations that don't require ORM mode. '''
    encrypted_key: str

class PostDetails(PostInDBBase):
    ''' This class extends PostInDBBase and adds a 'keys' field, which is a list of PostKeyInDB objects or None.  '''
    keys: list[PostKeyInDB] | None
