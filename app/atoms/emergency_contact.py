from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="비상연락처id")
    name = Column(String(20), doc="이름")
    cell_phone = Column(String(20), doc="휴대폰번호")

    personal_detail_id = Column(Integer, ForeignKey(column="personal_details.id", ondelete="CASCADE"), doc="인적사항id")
    personal_detail = relationship(argument="PersonalDetail", back_populates="emergency_contact")
