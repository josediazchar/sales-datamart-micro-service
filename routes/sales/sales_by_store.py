from fastapi import HTTPException, status
from models import SalesData, SalesByStores
from dependecies import SessionDep
from sqlmodel import func, select
from datetime import date


def sales_by_store(
        session: SessionDep,
        start_date: date,
        end_date: date,
        skip: int = 0,
        limit: int = 100
        ) -> SalesByStores:
    
    """
    sales in a period per store
    """

    if start_date is None or end_date is None:
        raise HTTPException(status_code=400, detail="start_date and end_date must be specified")
    
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="start_date must be before end_date")

    try:
        sales_statement = select(
            SalesData.KeyStore,
            func.sum(SalesData.Amount * SalesData.Qty).label("TotalSales")
        ).where(
            SalesData.KeyDate >= start_date,
            SalesData.KeyDate <= end_date
        ).group_by(
            SalesData.KeyStore
        ).offset(
            skip
        ).limit(limit)

        results = session.exec(sales_statement).all()

        return SalesByStores(data=results)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

