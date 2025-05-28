from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime
import uuid

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        id=str(uuid.uuid4()),
        nome=user.nome,
        email=user.email,
        senha_hash=user.senha,
        data_criacao=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_post(db: Session, post_id: str):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(
        id=str(uuid.uuid4()),
        titulo=post.titulo,
        conteudo=post.conteudo,
        autor_id=post.autor_id,
        categoria_id=post.categoria_id,
        data_publicacao=datetime.utcnow(),
        tags=",".join(post.tags)
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_comment(db: Session, comment_id: str):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(
        id=str(uuid.uuid4()),
        post_id=comment.post_id,
        autor_id=comment.autor_id,
        conteudo=comment.conteudo,
        data_comentario=datetime.utcnow()
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
