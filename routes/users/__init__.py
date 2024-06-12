from fastapi import APIRouter
from .login import login
from .register import register
from .read_user_me import read_user_me


user_router = APIRouter()

user_router.add_api_route('/login', methods=['POST'], endpoint=login)
user_router.add_api_route('/register', methods=['POST'], endpoint=register)
user_router.add_api_route('/me', methods=['GET'], endpoint=read_user_me)

