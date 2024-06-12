from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from fastapi.testclient import TestClient
import pytest
from config import settings
from main import app
from routes.users import login

client = TestClient(app)



def test_login_success():
    response = client.post(
        url=f"{settings.API_V1_STR}/users/login",
        data={
            'username':'jose@gmail.com',
            'password':'12345678'
        }
    )
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert "access_token" in response.json()


12345678
def test_login_failure():
    with pytest.raises(HTTPException) as cm:
        login(form_data=OAuth2PasswordRequestForm(
        username="jose@gmail.com",
        password="abcdefg"
    ))
    assert cm.value.status_code == 401
    assert cm.value.detail == "Incorrect username or password"
