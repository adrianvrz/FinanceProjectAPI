from sqlalchemy.orm import Session
from database.database import SessionLocal  # Asegúrate de que este import es correcto
from fastapi import Depends
from typing import Annotated

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]