from sqlalchemy import Column, Integer, ForeignKey, Text, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="게시판id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")
    title = Column(Text, doc="제목")
    content = Column(Text, doc="내용")

    company_id = Column(Integer, ForeignKey(column="companies.id", ondelete="CASCADE"), doc="회사id")
    company = relationship(argument="Company", back_populates="board")
