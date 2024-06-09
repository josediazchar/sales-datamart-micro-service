from fastapi import APIRouter
from .sales_by_employee import sales_by_employee
from .sales_by_product import sales_by_product
from .sales_by_store import sales_by_store

sales_router = APIRouter()

sales_router.add_api_route('/employees', methods=['GET'], endpoint=sales_by_employee)
sales_router.add_api_route('/products', methods=['GET'], endpoint=sales_by_product)
sales_router.add_api_route('/stores', methods=['GET'], endpoint=sales_by_store)

