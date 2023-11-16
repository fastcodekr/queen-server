from sqlalchemy import Integer, Column, Text

from app.utils.dev.database import Base


class FormSchedule(Base):
    __tablename__ = "form_schedules"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="일정id")
    number = Column(Integer, doc="번호")
    title = Column(Text, doc="제목")
    content1 = Column(Text, doc="내용1")
    content2 = Column(Text, doc="내용2")
    content21 = Column(Text, doc="내용2-1")
    content22 = Column(Text, doc="내용2-2")
