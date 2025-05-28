from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    nome: str
    email: str

class UserCreate(UserBase):
    senha: str

class User(UserBase):
    id: str
    data_criacao: datetime
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    titulo: str
    conteudo: str
    tags: Optional[List[str]] = []

class PostCreate(PostBase):
    autor_id: str
    categoria_id: str

class Post(PostBase):
    id: str
    data_publicacao: datetime
    likes: int
    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    conteudo: str

class CommentCreate(CommentBase):
    post_id: str
    autor_id: str

class Comment(CommentBase):
    id: str
    data_comentario: datetime
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    nome: str
    descricao: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: str
    class Config:
        orm_mode = True

class TagBase(BaseModel):
    nome: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: str
    class Config:
        orm_mode = True
