from fastapi import HTTPException, status
import jwt
import pyrebase
from datetime import datetime, timedelta
import pytz
from config import settings


# Pyrebase config
config = {
  "apiKey"           : settings.FIREBASE_APIKEY,
  "authDomain"       : settings.FIREBASE_AUTHDOMAIN,
  "projectId"        : settings.FIREBASE_PROJECTID,
  "storageBucket"    : settings.FIREBASE_STORAGEBUCKET,
  "messagingSenderId": settings.FIREBASE_MESSAGINGSENDERID,
  "appId"            : settings.FIREBASE_APPID,
  "databaseURL": None
}

firebase = pyrebase.initialize_app(config)
auth_pyrebase = firebase.auth()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"


def create_jwt_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(tz=pytz.utc).replace(tzinfo=None) + expires_delta
    else:
        expire = datetime.now(tz=pytz.utc).replace(tzinfo=None) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return email
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )