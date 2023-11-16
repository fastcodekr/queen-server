from sqlalchemy import Column, Integer, Text, ForeignKey, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class MedicalCondition(Base):
    __tablename__ = "medical_conditions"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="의료상태id")
    bee_sting = Column(String(1), doc="벌쏘임여부")
    epilepsy = Column(String(1), doc="간질여부")
    diabetes = Column(String(1), doc="당뇨여부")
    pregnant = Column(String(1), doc="임신여부")
    high_blood_pressure = Column(String(1), doc="고혈압여부")
    other = Column(Text, doc="기타")

    health_checklist_id = Column(Integer, ForeignKey(column="health_checklists.id", ondelete="CASCADE"),
                                 doc="건강조사체크리스트id")
    health_checklist = relationship(argument="HealthChecklist", back_populates="medical_condition")
