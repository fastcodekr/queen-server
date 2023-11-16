from app.papers.contract_form.service.get_all_form_agree_list import PapersContractFormByAgree
from app.papers.contract_form.service.get_all_form_checklist_list import PapersContractFormByChecklist
from app.papers.contract_form.service.get_all_form_guideline_list import PapersContractFormByGuideline
from app.papers.contract_form.service.get_all_form_policy_list import PapersContractFormByPolicy
from app.papers.contract_form.service.get_all_form_schedule_list import PapersContractFormBySchedule

strategy_map = {
    "papers_contract_form_by_policy": PapersContractFormByPolicy(),
    "papers_contract_form_by_agree": PapersContractFormByAgree(),
    "papers_contract_form_by_schedule": PapersContractFormBySchedule(),
    "papers_contract_form_by_guideline": PapersContractFormByGuideline(),
    "papers_contract_form_by_checklist": PapersContractFormByChecklist(),
}


class ContractFormFactory:
    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)
