from fastapi import HTTPException, status
from firebase_admin import auth
from models import User, UserCreate


def register(user: UserCreate) -> User:
    try:
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
        )
        return User(email=user_record.email)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
