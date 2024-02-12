from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import schemas,models
from database.dependencies import db_dependency, get_db
from typing import Annotated

router = APIRouter()

@router.post("/transaction", response_model=schemas.TransactionModel)
async def create_transaction(transaction: schemas.TransactionBase, db: db_dependency):
    db_transaction = models.transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

