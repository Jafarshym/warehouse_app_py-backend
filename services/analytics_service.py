from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.sale import Sale, SaleCost


def total_profit(db: Session):
    revenue = db.query(func.sum(Sale.quantity * Sale.sale_price)).scalar() or 0

    cost = db.query(
        func.sum(SaleCost.quantity * SaleCost.purchase_price)
    ).scalar() or 0

    return {
        "revenue": revenue,
        "cost": cost,
        "profit": revenue - cost
    }