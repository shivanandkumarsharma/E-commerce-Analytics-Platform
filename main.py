from fastapi import FastAPI
from app.routes import data_routes

app = FastAPI()

app.include_router(data_routes.router)