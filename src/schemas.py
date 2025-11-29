from pydantic import BaseModel

class PostCreateSchema(BaseModel):
    title: str
    content: str