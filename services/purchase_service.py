from sqlalchemy.orm import Session
from app.models.purchase import PurchaseBatch


def create_purchase(db: Session, product_id: int, quantity: float, purchase_price: float):

    batch = PurchaseBatch(
        product_id=product_id,
        quantity=quantity,
        remaining=quantity,
        purchase_price=purchase_price
    )

    db.add(batch)
    db.commit()
    db.refresh(batch)

    return {
        "message": "Партия добавлена",
        "batch_id": batch.id,
        "quantity": quantity,
        "price": purchase_price
    }