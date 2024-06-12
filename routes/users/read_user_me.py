from fastapi import Depends
from models import User
from dependecies import get_current_user


def read_user_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user
