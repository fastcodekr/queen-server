from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Staff(Base):
    __tablename__ = "staffs"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="관리자id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")
    level = Column(String(10), nullable=False, doc="관리자등급")
    name = Column(String(20), nullable=False, doc="이름")
    password = Column(String(60), nullable=False, doc="비밀번호")

    company = relationship(argument="Company", back_populates="staff")
    team = relationship(argument="Team", back_populates="staff")
