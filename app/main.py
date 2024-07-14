from fastapi import FastAPI
from .routes import auth
import uvicorn

app = FastAPI()

app.include_router(auth.router)

