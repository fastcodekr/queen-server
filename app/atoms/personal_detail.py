from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class PersonalDetail(Base):
    __tablename__ = "personal_details"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="인적사항id")
    cell_phone = Column(String(20), doc="휴대폰번호")
    email = Column(String(50), doc="이메일")
    address = Column(String(256), doc="주소")
    tax_file_number = Column(String(20), doc="세금번호")

    contract_id = Column(Integer, ForeignKey(column="contracts.id", ondelete="CASCADE"), doc="계약서id")
    contract = relationship(argument="Contract", back_populates="personal_detail")

    emergency_contact = relationship(argument="EmergencyContact", back_populates="personal_detail")
    superannuation = relationship(argument="Superannuation", back_populates="personal_detail")
    bank_detail = relationship(argument="BankDetail", back_populates="personal_detail")
