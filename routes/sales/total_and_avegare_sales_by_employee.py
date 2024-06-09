from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from models import TotalAndAvegareSalesByEmployee, SalesData
from dependecies import SessionDep
from sqlmodel import func, select
from datetime import date


def total_and_avegare_sales_by_employee(
        session: SessionDep,
        key_employee: str
        ) -> TotalAndAvegareSalesByEmployee:
    
    """
    total and avegare sales by employee
    """

    try:
        sales_statement = select(
            func.sum(SalesData.Amount * SalesData.Qty).label("TotalSales"),
            func.avg(SalesData.Amount * SalesData.Qty).label("AverageSales")
        ).where(
            SalesData.KeyEmployee == key_employee
        )

        result = session.exec(sales_statement).one()

        return TotalAndAvegareSalesByEmployee(
            KeyEmployee=key_employee,
            TotalSales=result.TotalSales,
            AverageSales=result.AverageSales
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

