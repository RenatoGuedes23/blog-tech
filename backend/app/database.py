import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da URL do banco de dados a partir de uma variável de ambiente
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Criação do motor do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criação de uma sessão local do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para seus modelos SQLAlchemy
Base = declarative_base()

# Função de dependência para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()