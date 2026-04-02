from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class PurchaseBatch(Base):
    __tablename__ = "purchase_batches"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Float)
    remaining = Column(Float)
    purchase_price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")