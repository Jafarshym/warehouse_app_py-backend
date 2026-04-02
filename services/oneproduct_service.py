from sqlalchemy.orm import Session
from app.models.product import Product

def get_oneproduct(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    data =  {
            "id": product.id,
            "name": product.name,
            "unit": product.unit,
            "min_stock": product.min_stock
        }
    print(data)
    return data
