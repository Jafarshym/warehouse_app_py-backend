from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Float)
    sale_price = Column(Float)
    client = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")


class SaleCost(Base):
    __tablename__ = "sale_costs"

    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    batch_id = Column(Integer, ForeignKey("purchase_batches.id"))
    quantity = Column(Float)
    purchase_price = Column(Float)