from sqlmodel import Field, SQLModel, create_engine, Session
from datetime import datetime

class SalesData(SQLModel, table=True):
    
    KeySale: str = Field(default=None, primary_key=True)
    KeyDate: datetime
    KeyStore: str
    KeyWarehouse: str
    KeyCustomer: str
    KeyProduct: str
    KeyEmployee: str
    KeyCurrency: str
    KeyDivision: int
    KeyTicket: str
    KeyCedi: str
    TicketId: str
    Qty: float
    Amount: float
    CostAmount: float
    DiscAmount: float
    Tickets: str
    Products: str
    Customers: str
    Employees: str
    Stores: str
    Divisions: str
    Time: str
    Cedis: str


class SalesByEmployee(SQLModel):
    KeyEmployee: str
    TotalSales: float


class SalesByEmployees(SQLModel):
    data: list[SalesByEmployee]



class SalesByProduct(SQLModel):
    KeyProduct: str
    TotalSales: float


class SalesByProducts(SQLModel):
    data: list[SalesByProduct]


class SalesByStore(SQLModel):
    KeyStore: str
    TotalSales: float


class SalesByStores(SQLModel):
    data: list[SalesByStore]


class TotalAndAvegareSalesByEmployee(SQLModel):
    KeyEmployee: str
    TotalSales: float
    AverageSales: float


class TotalAndAvegareSalesByStore(SQLModel):
    KeyStore: str
    TotalSales: float
    AverageSales: float


class TotalAndAvegareSalesByProduct(SQLModel):
    KeyProduct: str
    TotalSales: float
    AverageSales: float