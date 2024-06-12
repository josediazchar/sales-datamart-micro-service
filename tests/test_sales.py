from fastapi.security import OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
import pytest
from config import settings
from main import app
from routes.users import login

client = TestClient(app)


def test_sales_by_employee(access_token):
    headers = {
    "Accept": "*/*",
    "Authorization": f"Bearer {access_token}" 
    }

    response_1 = client.get(
        url=f"{settings.API_V1_STR}/sales/employees?start_date=2023-10-01&end_date=2023-11-30&skip=0&limit=100",
        headers=headers
    )
    assert response_1.status_code == 200

    response_2 = client.get(
        url=f"{settings.API_V1_STR}/sales/employees/1%7C10250",
        headers=headers
    )
    assert response_2.status_code == 200
    assert pytest.approx(response_2.json().get('TotalSales')) == next(filter(lambda x: x.get("KeyEmployee") == "1|10250", response_1.json().get('data'))).get('TotalSales')



def test_sales_by_product(access_token):
    headers = {
    "Accept": "*/*",
    "Authorization": f"Bearer {access_token}" 
    }

    response_1 = client.get(
        url=f"{settings.API_V1_STR}/sales/products?start_date=2023-10-01&end_date=2023-11-30&skip=0&limit=100",
        headers=headers
    )
    assert response_1.status_code == 200

    response_2 = client.get(
        url=f"{settings.API_V1_STR}/sales/products/1%7C42605",
        headers=headers
    )
    assert response_2.status_code == 200
    assert pytest.approx(response_2.json().get('TotalSales')) == next(filter(lambda x: x.get("KeyProduct") == "1|42605", response_1.json().get('data'))).get('TotalSales')



def test_sales_by_store(access_token):
    headers = {
    "Accept": "*/*",
    "Authorization": f"Bearer {access_token}" 
    }

    response_1 = client.get(
        url=f"{settings.API_V1_STR}/sales/stores?start_date=2023-10-01&end_date=2023-11-30&skip=0&limit=100",
        headers=headers
    )
    assert response_1.status_code == 200

    response_2 = client.get(
        url=f"{settings.API_V1_STR}/sales/stores/1%7C005",
        headers=headers
    )
    assert response_2.status_code == 200
    assert pytest.approx(response_2.json().get('TotalSales')) == next(filter(lambda x: x.get("KeyStore") == "1|005", response_1.json().get('data'))).get('TotalSales')



@pytest.fixture
def access_token():
    data = login(form_data=OAuth2PasswordRequestForm(
        username="jose@gmail.com",
        password="12345678"
    ))
    return data.get("access_token")
    