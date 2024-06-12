from fastapi import APIRouter
from .sales_by_employee import sales_by_employee
from .sales_by_product import sales_by_product
from .sales_by_store import sales_by_store
from .total_and_avegare_sales_by_employee import total_and_avegare_sales_by_employee
from .total_and_avegare_sales_by_store import total_and_avegare_sales_by_store
from .total_and_avegare_sales_by_product import total_and_avegare_sales_by_product

sales_router = APIRouter()

sales_router.add_api_route('/employees', methods=['GET'], endpoint=sales_by_employee)
sales_router.add_api_route('/employees/{key_employee}', methods=['GET'], endpoint=total_and_avegare_sales_by_employee)
sales_router.add_api_route('/products', methods=['GET'], endpoint=sales_by_product)
sales_router.add_api_route('/products/{key_product}', methods=['GET'], endpoint=total_and_avegare_sales_by_product)
sales_router.add_api_route('/stores', methods=['GET'], endpoint=sales_by_store)
sales_router.add_api_route('/stores/{key_store}', methods=['GET'], endpoint=total_and_avegare_sales_by_store)

