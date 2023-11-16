from app.atoms.bank_detail import BankDetail
from app.atoms.board import Board
from app.atoms.company import Company
from app.atoms.contract import Contract
from app.atoms.contract_form.form_agree import FormAgree
from app.atoms.contract_form.form_checklist import FormChecklist
from app.atoms.contract_form.form_checklist_detail import FormChecklistDetail
from app.atoms.contract_form.form_guideline import FormGuideline
from app.atoms.contract_form.form_policy import FormPolicy
from app.atoms.contract_form.form_policy_detail import FormPolicyDetail
from app.atoms.contract_form.form_schedule import FormSchedule
from app.atoms.emergency_contact import EmergencyContact
from app.atoms.farm import Farm
from app.atoms.general_health import GeneralHealth
from app.atoms.health_checklist import HealthChecklist
from app.atoms.location import Location
from app.atoms.medical_condition import MedicalCondition
from app.atoms.mental_health import MentalHealth
from app.atoms.order import Order
from app.atoms.passport import Passport
from app.atoms.person import Person
from app.atoms.personal_detail import PersonalDetail
from app.atoms.safety_aware import SafetyAware
from app.atoms.staff import Staff
from app.atoms.superannuation import Superannuation
from app.atoms.team import Team
from app.atoms.worker import Worker


def init_models():
    BankDetail()
    Board()
    Company()
    Contract()
    EmergencyContact()
    Farm()

    GeneralHealth()
    HealthChecklist()
    Location()
    MedicalCondition()
    MentalHealth()
    Order()
    Passport()
    Person()
    PersonalDetail()
    SafetyAware()
    Staff()
    Superannuation()
    Team()
    Worker()
    FormAgree()
    FormChecklist()
    FormChecklistDetail()
    FormGuideline()
    FormPolicy()
    FormPolicyDetail()
    FormSchedule()
