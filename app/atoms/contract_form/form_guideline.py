from sqlalchemy import Integer, Column, Text

from app.utils.dev.database import Base


class FormGuideline(Base):
    __tablename__ = "form_guidelines"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="안전수칙id")
    number = Column(Integer, doc="번호")
    title = Column(Text, doc="제목")
    content = Column(Text, doc="내용")
