from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="워홀러id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")
    start_date = Column(String(20), doc="시작일")
    end_date = Column(String(20), doc="종료일")
    tax = Column(String(10), doc="세금")
    farm_number = Column(String(20), doc="농장번호")
    memo = Column(Text, doc="관리자메모")

    team_id = Column(Integer, ForeignKey(column="teams.id", ondelete="CASCADE"), doc="팀id")
    team = relationship(argument="Team", back_populates="worker")

    person_id = Column(Integer, ForeignKey(column="people.id", ondelete="CASCADE"), doc="개인id")
    person = relationship(argument="Person", back_populates="worker")

    order = relationship(argument="Order", back_populates="worker")

    contract = relationship(argument="Contract", back_populates="worker")
