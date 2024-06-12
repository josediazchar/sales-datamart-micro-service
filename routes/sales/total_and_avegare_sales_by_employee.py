from fastapi import HTTPException, status, Depends
from models import TotalAndAvegareSalesByEmployee, SalesData, User
from dependecies import SessionDep, get_current_user
from sqlmodel import func, select
from datetime import date


def total_and_avegare_sales_by_employee(
        session: SessionDep,
        key_employee: str,
        current_user: User = Depends(get_current_user)
        ) -> TotalAndAvegareSalesByEmployee:
    
    """
       Calculates the total and average sales by a specific employee.

        Parameters:
        session (SessionDep): The database session dependency.
        key_employee (str): The unique identifier of the employee.
        current_user (User, optional): The current user making the request. Defaults to Depends(get_current_user).

        Returns:
        TotalAndAvegareSalesByEmployee: An object containing the total and average sales by the employee.

        Raises:
        HTTPException: If an error occurs during the database query.
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

