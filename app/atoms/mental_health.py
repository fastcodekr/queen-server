from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class MentalHealth(Base):
    __tablename__ = "mental_healths"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="정신건강id")
    job_stress = Column(String(1), doc="직무스트레스여부")
    mental_counseling = Column(String(1), doc="정신상담여부")
    aware_of_eap = Column(String(1), doc="EAP인지여부")

    health_checklist_id = Column(Integer, ForeignKey(column="health_checklists.id", ondelete="CASCADE"),
                                 doc="건강조사체크리스트id")
    health_checklist = relationship(argument="HealthChecklist", back_populates="mental_health")
