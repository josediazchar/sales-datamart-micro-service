from fastapi import HTTPException, status, Depends
from models import TotalAndAvegareSalesByProduct, SalesData, User
from dependecies import SessionDep, get_current_user
from sqlmodel import func, select
from datetime import date


def total_and_avegare_sales_by_product(
        session: SessionDep,
        key_product: str,
        current_user: User = Depends(get_current_user)
        ) -> TotalAndAvegareSalesByProduct:
    
    """
       Calculates the total and average sales by a specific product.

        Parameters:
        session (SessionDep): The database session dependency.
        key_product (str): The unique identifier of the product.
        current_user (User, optional): The current user making the request. Defaults to Depends(get_current_user).

        Returns:
        TotalAndAvegareSalesByproduct: An object containing the total and average sales by the product.

        Raises:
        HTTPException: If an error occurs during the database query.
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

