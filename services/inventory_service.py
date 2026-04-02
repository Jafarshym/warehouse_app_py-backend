from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.purchase import PurchaseBatch
from app.models.inventory import InventoryCheck


def inventory_check(db: Session, product_id: int, real_quantity: float):

    system_qty = (
        db.query(func.sum(PurchaseBatch.remaining))
        .filter(PurchaseBatch.product_id == product_id)
        .scalar()
    ) or 0

    diff = real_quantity - system_qty

    record = InventoryCheck(
        product_id=product_id,
        real_quantity=real_quantity,
        system_quantity=system_qty,
        difference=diff
    )

    db.add(record)

    if diff != 0:
        latest_batch = (
            db.query(PurchaseBatch)
            .filter(PurchaseBatch.product_id == product_id)
            .order_by(PurchaseBatch.created_at.desc())
            .first()
        )

        if latest_batch:
            latest_batch.remaining += diff

    db.commit()

    return {
        "system_quantity": system_qty,
        "real_quantity": real_quantity,
        "difference": diff
    }