from sqlmodel import SQLModel

class User(SQLModel):
    email: str


class UserCreate(SQLModel):
    email: str
    password: str