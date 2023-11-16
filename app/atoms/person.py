from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base
from app.utils.dev.time import current_time


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="개인id")
    created_at = Column(String(20), nullable=False, server_default=current_time(), doc="생성일시")
    updated_at = Column(String(20), nullable=False, server_default=current_time(), doc="수정일시")
    title = Column(String(10), doc="칭호")
    first_name = Column(String(20), nullable=False, doc="이름")
    last_name = Column(String(20), nullable=False, doc="성")
    english_name = Column(String(20), doc="영문이름")
    gender = Column(String(10), doc="성별")
    birth_date = Column(String(20), doc="생년월일")

    passport = relationship(argument="Passport", back_populates="person")
    worker = relationship(argument="Worker", back_populates="person")
