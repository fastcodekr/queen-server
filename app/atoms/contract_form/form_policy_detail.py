from sqlalchemy import Integer, Column, Text

from app.utils.dev.database import Base


class FormPolicyDetail(Base):
    __tablename__ = "form_policy_details"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="세부정책id")
    number = Column(Integer, doc="번호")
    content = Column(Text, doc="내용")

    form_policy_number = Column(Integer, index=True, doc="정책번호")
