from pydantic import BaseModel


class InventoryCheckCreate(BaseModel):
    product_id: int
    real_quantity: float