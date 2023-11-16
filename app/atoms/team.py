from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="팀id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")
    name = Column(String(20), nullable=False, doc="이름")

    staff_id = Column(Integer, ForeignKey(column="staffs.id", ondelete="CASCADE"), doc="관리자id")
    staff = relationship(argument="Staff", back_populates="team")

    company_id = Column(Integer, ForeignKey(column="companies.id", ondelete="CASCADE"), doc="회사id")
    company = relationship(argument="Company", back_populates="team")

    worker = relationship(argument="Worker", back_populates="team")
