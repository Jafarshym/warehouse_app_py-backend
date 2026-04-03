from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database  import SessionLocal
from app.services.search_service import search_product

router = APIRouter(prefix="/search", tags=["search"])

def get_db ():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@router.get("/{search}")
def get_product(search: str = None, db: Session = Depends(get_db)):
    return search_product(db, search)
