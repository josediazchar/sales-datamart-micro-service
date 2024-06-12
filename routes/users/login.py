from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from firebase_admin import auth
from utils import create_jwt_token, auth_pyrebase
import datetime


def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    This function handles user login.
    If the authentication is successful, it retrieves the user's information and generates a JWT token.
    If the authentication fails, it raises an HTTPException with a 401 status code and an appropriate error message.

    Parameters:
    form_data (OAuth2PasswordRequestForm): The form data containing the email and password provided by the user.

    Returns:
    dict: A dictionary containing the access token and token type.

    Raises:
    HTTPException: If the authentication fails, it raises an HTTPException with a 401 status code and an appropriate error message.
    """
    try:
        user = auth_pyrebase.sign_in_with_email_and_password(form_data.username, form_data.password)
        user_info = auth.get_user_by_email(form_data.username)
        access_token_expires = datetime.timedelta(minutes=30)
        access_token = create_jwt_token(
            data={"sub": user_info.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )