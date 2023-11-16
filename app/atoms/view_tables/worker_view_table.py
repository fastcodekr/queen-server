from sqlalchemy import Column, Integer, String, Text

from app.utils.dev.database import Base


class WorkerViewTable(Base):
    __tablename__ = "worker_view"
    id = Column(Integer, primary_key=True, autoincrement=True, doc="워홀러id")
    created_at = Column(String(20), doc="생성일시")
    updated_at = Column(String(20), doc="수정일시")

    location_id = Column(Integer, doc="지역id")
    location_name = Column(String(20), doc="지역이름")

    farm_id = Column(Integer, doc="농장id")
    farm_name = Column(String(20), doc="농장이름")

    team_id = Column(Integer, doc="팀id")
    team_name = Column(String(20), doc="팀이름")

    first_name = Column(String(20), doc="이름")
    last_name = Column(String(20), doc="성")
    english_name = Column(String(20), doc="영문이름")

    bsb = Column(String(20), doc="은행번호")
    account_number = Column(String(20), doc="계좌번호")

    email = Column(String(50), doc="이메일")
    cell_phone = Column(String(20), doc="휴대폰번호")
    tax_file_number = Column(String(20), doc="세금번호")
    birth_date = Column(String(20), doc="생년월일")
    gender = Column(String(10), doc="성별")
    nationality = Column(String(20), doc="국적")
    passport_number = Column(String(20), doc="여권번호")
    visa_grant_number = Column(String(20), doc="비자번호")
    fund_name = Column(String(20), doc="연금이름")
    member_number = Column(String(20), doc="회원번호")
    address = Column(String(256), doc="주소")

    start_date = Column(String(20), doc="시작일")
    end_date = Column(String(20), doc="종료일")
    tax = Column(String(10), doc="세금")
    farm_number = Column(String(20), doc="농장번호")
    memo = Column(Text, doc="관리자메모")
