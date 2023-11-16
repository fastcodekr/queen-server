from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="회사id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")
    name = Column(String(20), nullable=False, unique=True, doc="이름")
    address = Column(String(256), doc="주소")

    staff_id = Column(Integer, ForeignKey(column="staffs.id", ondelete="CASCADE"), doc="관리자id")
    staff = relationship(argument="Staff", back_populates="company")

    board = relationship(argument="Board", back_populates="company")
    farm = relationship(argument="Farm", back_populates="company")
    team = relationship(argument="Team", back_populates="company")
