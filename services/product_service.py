from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.product import Product
from app.schemas.product import ProductUpdate

def create_products_bulk(db: Session, products_data: list):
    products_added = []
    for item in products_data:
        product = Product(
            name=item.name,
            unit=item.unit,
            min_stock=item.min_stock
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        products_added.append({
            "id": product.id,
            "name": product.name,
            "unit": product.unit,
            "min_stock": product.min_stock
        })
    return products_added



def delete_product(db: Session, product_id: int):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}


def update_product(db: Session, product_id: int, data: ProductUpdate):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = data.name
    product.unit = data.unit
    product.min_stock = data.min_stock

    db.commit()
    db.refresh(product)

    return product


def get_all_products(db: Session):
    products = db.query(Product).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "unit": p.unit,
            "min_stock": p.min_stock
        }
        for p in products
    ]