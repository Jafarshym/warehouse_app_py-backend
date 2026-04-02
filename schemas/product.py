from pydantic import BaseModel
from typing import List

class ProductCreate(BaseModel):
    name: str
    unit: str
    min_stock: float = 0

class ProductsBulkCreate(BaseModel):
    products: List[ProductCreate]


class ProductUpdate(BaseModel):
    name: str
    unit: str
    min_stock: float