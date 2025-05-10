from app.db.session import SessionLocal
from sqlalchemy.orm import Session

# Generator de sesiune DB pentru FastAPI
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
