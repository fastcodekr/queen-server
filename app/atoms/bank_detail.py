from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class BankDetail(Base):
    __tablename__ = "bank_details"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="계좌정보id")
    bank_name = Column(String(20), doc="은행명")
    account_name = Column(String(20), doc="예금주")
    bsb = Column(String(20), doc="은행번호")
    account_number = Column(String(20), doc="계좌번호")

    personal_detail_id = Column(Integer, ForeignKey(column="personal_details.id", ondelete="CASCADE"), doc="인적사항id")
    personal_detail = relationship(argument="PersonalDetail", back_populates="bank_detail")
