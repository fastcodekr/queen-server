from sqlalchemy import Integer, Column, Text

from app.utils.dev.database import Base


class FormPolicy(Base):
    __tablename__ = "form_policies"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="정책id")
    number = Column(Integer, index=True, doc="번호")
    title = Column(Text, doc="제목")
    content_head = Column(Text, doc="내용-전")
    content_tail = Column(Text, doc="내용-후")
