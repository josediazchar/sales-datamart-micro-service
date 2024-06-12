from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from collections.abc import Generator
from sqlmodel import Session
from typing import Annotated
from database import engine
from models import User
from config import settings

from utils import verify_jwt_token



def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        

SessionDep = Annotated[Session, Depends(get_db)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/users/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    email = verify_jwt_token(token)
    return User(email=email)