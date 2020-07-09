from sqlalchemy import String, DateTime, Column, Integer, Float
from API.Models.base import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    cod = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    brand = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())


