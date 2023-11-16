from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class GeneralHealth(Base):
    __tablename__ = "general_healths"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="일반건강id")
    pre_existing_medical_condition = Column(String(1), doc="기존의료상태여부")
    taking_medication = Column(String(1), doc="약복용여부")
    recent_surgery = Column(String(1), doc="최근수술여부")
    recent_injury = Column(String(1), doc="최근부상여부")
    job_related_limitation = Column(String(1), doc="직무관련제한여부")

    health_checklist_id = Column(Integer, ForeignKey(column="health_checklists.id", ondelete="CASCADE"),
                                 doc="건강조사체크리스트id")
    health_checklist = relationship(argument="HealthChecklist", back_populates="general_health")
