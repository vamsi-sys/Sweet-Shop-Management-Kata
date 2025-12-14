from pydantic import BaseModel
from typing import Optional


class SweetCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int


class SweetUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


class SweetOut(BaseModel):
    id: int
    name: str
    category: str
    price: float
    quantity: int

    class Config:
        from_attributes = True
