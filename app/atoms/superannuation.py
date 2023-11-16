from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class Superannuation(Base):
    __tablename__ = "superannuations"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="연금id")
    fund_name = Column(String(20), doc="연금이름")
    member_number = Column(String(20), doc="회원번호")

    personal_detail_id = Column(Integer, ForeignKey(column="personal_details.id", ondelete="CASCADE"), doc="인적사항id")
    personal_detail = relationship(argument="PersonalDetail", back_populates="superannuation")
