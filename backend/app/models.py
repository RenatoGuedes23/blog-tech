from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base # Importar Base se não estiver em database.py

# Se Base já estiver importada de .database, você pode remover esta linha:
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Corrigido para referenciar o modelo Post e Comment
    posts = relationship("Post", back_populates="owner")
    comments = relationship("Comment", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    # Adicionando ForeignKey para owner_id
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Corrigido para referenciar o modelo User
    owner = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    # Adicionando ForeignKey para owner_id
    owner_id = Column(Integer, ForeignKey("users.id"))
    # Adicionando ForeignKey para post_id
    post_id = Column(Integer, ForeignKey("posts.id"))

    # Corrigido para referenciar o modelo User e Post
    owner = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")