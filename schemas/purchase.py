from pydantic import BaseModel


class PurchaseCreate(BaseModel):
    product_id: int
    quantity: float
    purchase_price: float