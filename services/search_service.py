from sqlalchemy.orm import Session
from app.models.product import Product

def search_product(db: Session, search: str = None):
    products = db.query(Product).filter(Product.name.ilike(f"%{search}%"))


    return [
        {
            "id": p.id,
            "name": p.name,
            "unit": p.unit,
            "min_stock": p.min_stock
        }
        for p in products
    ]