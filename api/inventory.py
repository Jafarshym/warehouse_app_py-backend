from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.inventory import InventoryCheckCreate
from app.services.inventory_service import inventory_check

router = APIRouter(prefix="/inventory", tags=["Inventory"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/check")
def check(data: InventoryCheckCreate, db: Session = Depends(get_db)):
    return inventory_check(db, data.product_id, data.real_quantity)