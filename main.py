from fastapi import FastAPI
from routes.motorcycles_routes import motorcycle_api_router

app = FastAPI()

app.include_router(motorcycle_api_router)