from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database  import SessionLocal
from app.services.oneproduct_service import get_oneproduct

router = APIRouter(prefix="/OneProduct", tags=["OneProdect"])

def get_db ():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_oneproduct(db, product_id)
