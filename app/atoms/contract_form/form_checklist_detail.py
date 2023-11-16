from sqlalchemy import Integer, Column, Text, String

from app.utils.dev.database import Base


class FormChecklistDetail(Base):
    __tablename__ = "form_checklist_details"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="세부건강체크리스트id")
    number = Column(Integer, doc="번호")
    short_name = Column(String(50), doc="줄임말")
    content = Column(Text, doc="내용")

    form_checklist_number = Column(Integer, index=True, doc="건강체크리스트번호")
