from fastapi import APIRouter
from .sales import sales_router
from .users import user_router

#from app.api.routes import items, login, users, utils

api_router = APIRouter()

api_router.include_router(sales_router, prefix="/sales", tags=["sales"])
api_router.include_router(user_router, prefix="/users", tags=["users"])




