from fastapi import FastAPI
from database.database import engine
from schema import models
from fastapi.middleware.cors import CORSMiddleware
from features.transaction import router

app = FastAPI()

origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

models.Base.metadata.create_all(bind=engine)

app.include_router(router)
