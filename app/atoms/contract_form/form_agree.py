from sqlalchemy import Integer, Column, Text

from app.utils.dev.database import Base


class FormAgree(Base):
    __tablename__ = "form_agrees"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="동의id")
    number = Column(Integer, doc="번호")
    content = Column(Text, doc="내용")
