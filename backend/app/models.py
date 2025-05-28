from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="autor")
    comments = relationship("Comment", back_populates="autor")

class Post(Base):
    __tablename__ = "posts"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    titulo = Column(String, index=True)
    conteudo = Column(Text)
    autor_id = Column(String, ForeignKey("users.id"))
    categoria_id = Column(String, ForeignKey("categories.id"))
    data_publicacao = Column(DateTime, default=datetime.utcnow)
    tags = Column(String)
    likes = Column(Integer, default=0)

    autor = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    post_id = Column(String, ForeignKey("posts.id"))
    autor_id = Column(String, ForeignKey("users.id"))
    conteudo = Column(Text)
    data_comentario = Column(DateTime, default=datetime.utcnow)

    post = relationship("Post", back_populates="comments")
    autor = relationship("User", back_populates="comments")

class Category(Base):
    __tablename__ = "categories"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, index=True)
    descricao = Column(String)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, index=True)

class PostTag(Base):
    __tablename__ = "post_tags"
    post_id = Column(String, ForeignKey("posts.id"), primary_key=True)
    tag_id = Column(String, ForeignKey("tags.id"), primary_key=True)
