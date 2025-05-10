# backend/app/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Importă toate modelele aici
from app.models.test import TestModel
