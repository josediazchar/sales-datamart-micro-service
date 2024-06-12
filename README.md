# CELES Sales Datamart API

## Overview
Welcome to the CELES Sales Datamart API. This API allows you to access and analyze sales data by employees, products, and stores. The API provides endpoints to retrieve sales data, calculate total and average sales, and manage user authentication.

## Version
**Current Version:** 0.1.0

## Running the API
### Prerequisites

Ensure you have Docker and Docker Compose installed on your machine. You can download and install them from the following links:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)



**Download data** from https://drive.google.com/file/d/1s0irIrngQVeRDXY8F5gizkttG9Rqshg0/view?usp=drive_link and save in the root folder into **'data/'** folder.



**Create .env file** in root folder set the environment variables:
```bash
SECRET_KEY=AIzaSyD58uj4h6YWxZW3K9oM6GZXLeruP_OXS78

# Postgres
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=hscKjq3dXgXofJzDz-W8q1DbU8MmF2vzAL9WiVdb2HE

# Firebase
FIREBASE_APIKEY=AIzaSyD58uj4h6YWxZW3K9oM6GZXLeruP_OXS78
FIREBASE_AUTHDOMAIN=celes-datamart.firebaseapp.com
FIREBASE_PROJECTID=celes-datamart
FIREBASE_STORAGEBUCKET=celes-datamart.appspot.com
FIREBASE_MESSAGINGSENDERID=509529236240
FIREBASE_APPID=1:509529236240:web:b79f14f7cecc3fd79b7b95
FIREBASE_CREDENTIALS_PATH=./celes-datamart-firebase-adminsdk-9o7vu-3bd6e0d0e0.json
```


**NOTE**: THIS IS ONLY FOR TEST ENVIRONMENTS, AND FOR FACILITATE TO RUN THE PROJECT, THIS CREDENTIAS WILL BE UNAVAILABLE IN THE NEXT DAYS.




**Build and start the services**: Run the following command to build the Docker images and start the containers defined in the `docker-compose.yml` file.

   ```bash
   docker-compose up --build
   ```

**NOTE**: Pleas await that api service load tada from files into /data folder to the Postgres database.


**Access the API**: Once the services are running, you can access your FastAPI API at `http://localhost:8000/docs`.

![alt text](image.png)


**Check the status of the containers**: You can verify that the containers are running correctly using the following command.

   ```bash
   docker-compose ps
   ```

**Stop the services**: To stop and remove the containers, run the following command.

   ```bash
   docker-compose down
   ```

## Endpoints

### Sales Endpoints

#### 1. Sales By Employee
- **Endpoint:** `/api/v1/sales/employees`
- **Method:** GET
- **Description:** Calculates the total sales for each employee within a given date range.
- **Parameters:**
  - `start_date` (string, required): The start date of the period.
  - `end_date` (string, required): The end date of the period.
  - `skip` (integer, optional): The number of records to skip for pagination. Default is 0.
  - `limit` (integer, optional): The maximum number of records to return for pagination. Default is 100.
- **Returns:** An object containing the total sales for each employee.
- **Responses:**
  - `200`: Successful Response (SalesByEmployees)
  - `422`: Validation Error (HTTPValidationError)

#### 2. Total And Average Sales By Employee
- **Endpoint:** `/api/v1/sales/employees/{key_employee}`
- **Method:** GET
- **Description:** Calculates the total and average sales by a specific employee.
- **Parameters:**
  - `key_employee` (string, required): The unique identifier of the employee.
- **Returns:** An object containing the total and average sales by the employee.
- **Responses:**
  - `200`: Successful Response (TotalAndAvegareSalesByEmployee)
  - `422`: Validation Error (HTTPValidationError)

#### 3. Sales By Product
- **Endpoint:** `/api/v1/sales/products`
- **Method:** GET
- **Description:** Calculates the total sales for each product within a given date range.
- **Parameters:**
  - `start_date` (string, required): The start date of the period.
  - `end_date` (string, required): The end date of the period.
  - `skip` (integer, optional): The number of records to skip for pagination. Default is 0.
  - `limit` (integer, optional): The maximum number of records to return for pagination. Default is 100.
- **Returns:** An object containing the total sales for each product.
- **Responses:**
  - `200`: Successful Response (SalesByProducts)
  - `422`: Validation Error (HTTPValidationError)

#### 4. Total And Average Sales By Product
- **Endpoint:** `/api/v1/sales/products/{key_product}`
- **Method:** GET
- **Description:** Calculates the total and average sales by a specific product.
- **Parameters:**
  - `key_product` (string, required): The unique identifier of the product.
- **Returns:** An object containing the total and average sales by the product.
- **Responses:**
  - `200`: Successful Response (TotalAndAvegareSalesByProduct)
  - `422`: Validation Error (HTTPValidationError)

#### 5. Sales By Store
- **Endpoint:** `/api/v1/sales/stores`
- **Method:** GET
- **Description:** Calculates the total sales for each store within a given date range.
- **Parameters:**
  - `start_date` (string, required): The start date of the period.
  - `end_date` (string, required): The end date of the period.
  - `skip` (integer, optional): The number of records to skip for pagination. Default is 0.
  - `limit` (integer, optional): The maximum number of records to return for pagination. Default is 100.
- **Returns:** An object containing the total sales for each store.
- **Responses:**
  - `200`: Successful Response (SalesByStores)
  - `422`: Validation Error (HTTPValidationError)

#### 6. Total And Average Sales By Store
- **Endpoint:** `/api/v1/sales/stores/{key_store}`
- **Method:** GET
- **Description:** Calculates the total and average sales by a specific store.
- **Parameters:**
  - `key_store` (string, required): The unique identifier of the store.
- **Returns:** An object containing the total and average sales by the store.
- **Responses:**
  - `200`: Successful Response (TotalAndAvegareSalesByStore)
  - `422`: Validation Error (HTTPValidationError)

### User Endpoints

#### 1. User Login
- **Endpoint:** `/api/v1/users/login`
- **Method:** POST
- **Description:** Handles user login and generates a JWT token upon successful authentication.
- **Parameters:**
  - `form_data` (OAuth2PasswordRequestForm, required): The form data containing the email and password provided by the user.
- **Returns:** A dictionary containing the access token and token type.
- **Responses:**
  - `200`: Successful Response
  - `422`: Validation Error (HTTPValidationError)

#### 2. User Registration
- **Endpoint:** `/api/v1/users/register`
- **Method:** POST
- **Description:** Handles new user registration.
- **Parameters:**
  - Request body (UserCreate, required): The user data to create a new user.
- **Returns:** The created user object.
- **Responses:**
  - `200`: Successful Response (User)
  - `422`: Validation Error (HTTPValidationError)

#### 3. Read Current User
- **Endpoint:** `/api/v1/users/me`
- **Method:** GET
- **Description:** Retrieves the current user's information.
- **Responses:**
  - `200`: Successful Response (User)

## Security
This API uses OAuth2 with Password (Bearer) flow for securing the endpoints. The token URL for obtaining the JWT token is `/api/v1/users/login`.

## Schemas
### SalesByEmployee
- `KeyEmployee` (string): The unique identifier of the employee.
- `TotalSales` (number): The total sales made by the employee.

### SalesByEmployees
- `data` (array of SalesByEmployee): The list of total sales by each employee.

### SalesByProduct
- `KeyProduct` (string): The unique identifier of the product.
- `TotalSales` (number): The total sales made for the product.

### SalesByProducts
- `data` (array of SalesByProduct): The list of total sales by each product.

### SalesByStore
- `KeyStore` (string): The unique identifier of the store.
- `TotalSales` (number): The total sales made by the store.

### SalesByStores
- `data` (array of SalesByStore): The list of total sales by each store.

### TotalAndAvegareSalesByEmployee
- `KeyEmployee` (string): The unique identifier of the employee.
- `TotalSales` (number): The total sales made by the employee.
- `AverageSales` (number): The average sales made by the employee.

### TotalAndAvegareSalesByProduct
- `KeyProduct` (string): The unique identifier of the product.
- `TotalSales` (number): The total sales made for the product.
- `AverageSales` (number): The average sales made for the product.

### TotalAndAvegareSalesByStore
- `KeyStore` (string): The unique identifier of the store.
- `TotalSales` (number): The total sales made by the store.
- `AverageSales` (number): The average sales made by the store.

### User
- `email` (string): The email of the user.

### UserCreate
- `email` (string): The email of the user.
- `password` (string): The password of the user.

### HTTPValidationError
- `detail` (array of ValidationError): A list of validation errors.

### ValidationError
- `loc` (array of strings/integers): The location of the error.
- `msg` (string): The error message.
- `type` (string): The type of the error.



