from contextlib import asynccontextmanager
from fastapi import FastAPI
from firebase_admin import credentials, initialize_app
from config import settings
from routes import api_router
from load_data import load_data

cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
initialize_app(cred)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    """
    print("Loading data to database")
    load_data()

    yield

    print("shutting down application")


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)


app.include_router(api_router, prefix=settings.API_V1_STR)
