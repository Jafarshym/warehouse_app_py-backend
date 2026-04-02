from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.purchase import PurchaseBatch
from app.models.product import Product


def get_stock(db: Session):
    rows = (
        db.query(
            Product.id,
            Product.name,
            Product.unit,
            func.sum(PurchaseBatch.remaining).label("stock")
        )
        .join(PurchaseBatch, PurchaseBatch.product_id == Product.id)
        .group_by(Product.id)
        .all()
    )

    return [
        {
            "product_id": r.id,
            "name": r.name,
            "unit": r.unit,
            "stock": r.stock or 0
        }
        for r in rows
    ]