from fastapi import FastAPI
from app.api.api import api_router

# 🆕 Acestea sunt liniile esențiale pentru a crea tabelele
from app.db.session import engine
from app.db.base import Base

app = FastAPI()

# Creează tabelele în baza de date la pornirea aplicației
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api")

