from pydantic import BaseModel

class PostCreateSchema(BaseModel):
    title: str
    content: str

class PostResponseSchema(BaseModel):
    title: str
    content: str