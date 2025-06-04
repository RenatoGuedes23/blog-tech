from pydantic import BaseModel, EmailStr
from typing import List, Optional

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    post_id: int

class Comment(CommentBase):
    id: int
    owner_id: int
    post_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    cpf: str # Adicionado CPF para criação

class User(UserBase):
    id: int
    is_active: bool
    cpf: str # Adicionado CPF no modelo de resposta
    posts: List[Post] = []
    comments: List[Comment] = []

    class Config:
        from_attributes = True