from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.utils.dev.database import Base


class SafetyAware(Base):
    __tablename__ = "safety_awares"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="안전인식id")
    aware_of_safety_policy = Column(String(1), doc="안전규정인지여부")
    first_aid_training = Column(String(1), doc="응급처치훈련여부")
    safety_reporting_comfort = Column(String(1), doc="안전신고편의여부")

    health_checklist_id = Column(Integer, ForeignKey(column="health_checklists.id", ondelete="CASCADE"),
                                 doc="건강조사체크리스트id")
    health_checklist = relationship(argument="HealthChecklist", back_populates="safety_aware")
