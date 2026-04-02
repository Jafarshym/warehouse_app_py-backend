from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.stock_service import get_stock

router = APIRouter(prefix="/stock", tags=["Stock"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def stock(db: Session = Depends(get_db)):
    return get_stock(db)