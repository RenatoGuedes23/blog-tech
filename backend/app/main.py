from fastapi import FastAPI
from app.routers import users, posts, comments
from app.database import engine
from app.models import Base

# Cria as tabelas automaticamente ao iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Blog Tech"}