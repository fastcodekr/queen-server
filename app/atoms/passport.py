from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class Passport(Base):
    __tablename__ = "passports"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="여권정보id")
    visa_grant_number = Column(String(20), doc="비자번호")
    visa_expire_date = Column(String(20), doc="비자만료일")
    nationality = Column(String(20), doc="국적")
    passport_number = Column(String(20), nullable=False, unique=True, doc="여권번호")

    person_id = Column(Integer, ForeignKey(column="people.id", ondelete="CASCADE"), doc=" 개인id")
    person = relationship(argument="Person", back_populates="passport")
