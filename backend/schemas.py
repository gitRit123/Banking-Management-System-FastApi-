from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str
    email: str
    balance: float

class AccountUpdate(BaseModel):
    name: str
    email: str

class AccountResponse(BaseModel):
    id: int
    name: str
    email: str
    balance: float

    class Config:
        from_attributes = True
