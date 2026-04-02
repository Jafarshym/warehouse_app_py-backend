from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.product import ProductsBulkCreate
from app.services.product_service import create_products_bulk
from app.services.product_service import delete_product
from app.services.product_service import get_all_products
from app.schemas.product import ProductUpdate
from app.services.product_service import update_product

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/bulk")
def products_bulk_create(data: ProductsBulkCreate, db: Session = Depends(get_db)):
    return create_products_bulk(db, data.products)

@router.delete("/{product_id}")
def delete_product_api(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)

@router.put("/{product_id}")
def update_product_api(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db)
):
    return update_product(db, product_id, data)

@router.get("/")
def products_list(db: Session = Depends(get_db)):
    """
    Получить список всех товаров
    """
    return get_all_products(db)