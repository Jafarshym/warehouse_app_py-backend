from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.sale_service import create_sale

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sale")
def sale(product_id: int, quantity: float, sale_price: float, client: str,
         db: Session = Depends(get_db)):
    return create_sale(db, product_id, quantity, sale_price, client)
