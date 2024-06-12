from fastapi import HTTPException, status, Depends
from models import SalesData, SalesByStores, User
from dependecies import SessionDep, get_current_user
from sqlmodel import func, select
from datetime import date


def sales_by_store(
        session: SessionDep,
        start_date: date,
        end_date: date,
        skip: int = 0,
        limit: int = 100,
        current_user: User = Depends(get_current_user)
        ) -> SalesByStores:
    
    """
        Calculates the total sales for each store within a given date range.

        Parameters:
        session (SessionDep): The database session for executing the query.
        start_date (date): The start date of the period.
        end_date (date): The end date of the period.
        skip (int, optional): The number of records to skip for pagination. Default is 0.
        limit (int, optional): The maximum number of records to return for pagination. Default is 100.

        Returns:
        SalesByStores: An object containing the total sales for each store.

        Raises:
        HTTPException: If start_date or end_date is not provided, or if start_date is after end_date.
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

