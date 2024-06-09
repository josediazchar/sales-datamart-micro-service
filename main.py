from fastapi import FastAPI
from fastapi.routing import APIRoute
from config import settings

from routes import api_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router, prefix=settings.API_V1_STR)
