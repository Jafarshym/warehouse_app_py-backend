from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.sale import Sale, SaleCost
from app.models.purchase import PurchaseBatch


def get_stock(db: Session, product_id: int):
    stock = (
        db.query(func.sum(PurchaseBatch.remaining))
        .filter(PurchaseBatch.product_id == product_id)
        .scalar()
    )
    return stock or 0


def create_sale(db: Session, product_id, quantity, sale_price, client):

    stock = get_stock(db, product_id)

    if stock < quantity:
        raise Exception("Недостаточно товара")

    sale = Sale(
        product_id=product_id,
        quantity=quantity,
        sale_price=sale_price,
        client=client
    )

    db.add(sale)
    db.commit()
    db.refresh(sale)

    qty_needed = quantity
    total_cost = 0

    batches = (
        db.query(PurchaseBatch)
        .filter(PurchaseBatch.product_id == product_id)
        .filter(PurchaseBatch.remaining > 0)
        .order_by(PurchaseBatch.created_at)
        .all()
    )

    for batch in batches:
        if qty_needed <= 0:
            break

        take = min(batch.remaining, qty_needed)

        batch.remaining -= take
        qty_needed -= take

        cost = SaleCost(
            sale_id=sale.id,
            batch_id=batch.id,
            quantity=take,
            purchase_price=batch.purchase_price
        )

        total_cost += take * batch.purchase_price
        db.add(cost)

    db.commit()

    revenue = quantity * sale_price

    return {
        "sale_id": sale.id,
        "revenue": revenue,
        "cost": total_cost,
        "profit": revenue - total_cost
    }