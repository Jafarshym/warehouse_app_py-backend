from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from app.database import Base


class InventoryCheck(Base):
    __tablename__ = "inventory_checks"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))

    real_quantity = Column(Float)     # фактическое количество
    system_quantity = Column(Float)   # количество в системе
    difference = Column(Float)        # разница

    created_at = Column(DateTime, default=datetime.utcnow)