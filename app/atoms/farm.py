from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Farm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="농장id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")
    name = Column(String(20), nullable=False, doc="이름")

    location_id = Column(Integer, ForeignKey(column="locations.id", ondelete="CASCADE"), doc="지역id")
    location = relationship(argument="Location", back_populates="farm")

    company_id = Column(Integer, ForeignKey(column="companies.id", ondelete="CASCADE"), doc="회사id")
    company = relationship(argument="Company", back_populates="farm")

    order = relationship(argument="Order", back_populates="farm")
    contract = relationship(argument="Contract", back_populates="farm")
