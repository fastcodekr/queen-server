from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class HealthChecklist(Base):
    __tablename__ = "health_checklists"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="건강조사체크리스트id")
    extra_disclosure = Column(Text, doc="추가 건강 관련 사항")

    contract_id = Column(Integer, ForeignKey(column="contracts.id", ondelete="CASCADE"), doc="계약서id")
    contract = relationship(argument="Contract", back_populates="health_checklist")

    general_health = relationship(argument="GeneralHealth", back_populates="health_checklist")
    mental_health = relationship(argument="MentalHealth", back_populates="health_checklist")
    safety_aware = relationship(argument="SafetyAware", back_populates="health_checklist")
    medical_condition = relationship(argument="MedicalCondition", back_populates="health_checklist")
