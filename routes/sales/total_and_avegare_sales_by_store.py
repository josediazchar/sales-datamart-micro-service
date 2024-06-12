from fastapi import HTTPException, status, Depends
from models import TotalAndAvegareSalesByStore, SalesData, User
from dependecies import SessionDep, get_current_user
from sqlmodel import func, select
from datetime import date


def total_and_avegare_sales_by_store(
        session: SessionDep,
        key_store: str,
        current_user: User = Depends(get_current_user)
        ) -> TotalAndAvegareSalesByStore:
    
    """
        Calculates the total and average sales by a specific store.

        Parameters:
        session (SessionDep): The database session dependency.
        key_store (str): The unique identifier of the store.
        current_user (User, optional): The current user making the request. Defaults to Depends(get_current_user).

        Returns:
        TotalAndAvegareSalesBystore: An object containing the total and average sales by the store.

        Raises:
        HTTPException: If an error occurs during the database query.
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

