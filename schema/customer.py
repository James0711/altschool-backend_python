from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    username: str
    address: str

class CustomerCreate(BaseModel):
    username: str
    address: str


customers: list[Customer] = [
    Customer(id=1, username="Timothy", address="30B State housing str"),
    Customer(id=2, username="Paul", address="14 IBB way")
]