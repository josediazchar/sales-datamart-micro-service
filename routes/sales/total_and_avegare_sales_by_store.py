from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from models import TotalAndAvegareSalesByStore, SalesData
from dependecies import SessionDep
from sqlmodel import func, select
from datetime import date


def total_and_avegare_sales_by_store(
        session: SessionDep,
        key_store: str
        ) -> TotalAndAvegareSalesByStore:
    
    """
    total and avegare sales by store
    """

    try:
        sales_statement = select(
            func.sum(SalesData.Amount * SalesData.Qty).label("TotalSales"),
            func.avg(SalesData.Amount * SalesData.Qty).label("AverageSales")
        ).where(
            SalesData.KeyStore == key_store
        )

        result = session.exec(sales_statement).one()

        return TotalAndAvegareSalesByStore(
            KeyStore=key_store,
            TotalSales=result.TotalSales,
            AverageSales=result.AverageSales
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

