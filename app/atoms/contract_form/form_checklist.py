from sqlalchemy import Integer, Column, Text

from app.utils.dev.database import Base


class FormChecklist(Base):
    __tablename__ = "form_checklists"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="건강체크리스트id")
    number = Column(Integer, index=True, doc="번호")
    content = Column(Text, doc="내용")
