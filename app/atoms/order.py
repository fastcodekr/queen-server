from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="파견id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")

    farm_id = Column(Integer, ForeignKey(column="farms.id", ondelete="CASCADE"), doc="농장id")
    farm = relationship(argument="Farm", back_populates="order")

    worker_id = Column(Integer, ForeignKey(column="workers.id", ondelete="CASCADE"), doc="워홀러id")
    worker = relationship(argument="Worker", back_populates="order")
