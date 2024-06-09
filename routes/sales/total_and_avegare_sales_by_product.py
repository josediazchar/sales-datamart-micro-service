from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from models import TotalAndAvegareSalesByProduct, SalesData
from dependecies import SessionDep
from sqlmodel import func, select
from datetime import date


def total_and_avegare_sales_by_product(
        session: SessionDep,
        key_product: str
        ) -> TotalAndAvegareSalesByProduct:
    
    """
    total and avegare sales by product
    """

    try:
        sales_statement = select(
            func.sum(SalesData.Amount * SalesData.Qty).label("TotalSales"),
            func.avg(SalesData.Amount * SalesData.Qty).label("AverageSales")
        ).where(
            SalesData.KeyProduct == key_product
        )

        result = session.exec(sales_statement).one()

        return TotalAndAvegareSalesByProduct(
            KeyProduct=key_product,
            TotalSales=result.TotalSales,
            AverageSales=result.AverageSales
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

