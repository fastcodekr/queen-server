from app.papers.contract_form.web.factory import ContractFormFactory


class ContractFormController(object):
    def __init__(self):
        self.factory = ContractFormFactory

    def papers_contract_form_by_policy(self, **kwargs):
        return self.factory.create(strategy="papers_contract_form_by_policy", **kwargs)

    def papers_contract_form_by_agree(self, **kwargs):
        return self.factory.create(strategy="papers_contract_form_by_agree", **kwargs)

    def papers_contract_form_by_schedule(self, **kwargs):
        return self.factory.create(strategy="papers_contract_form_by_schedule", **kwargs)

    def papers_contract_form_by_guideline(self, **kwargs):
        return self.factory.create(strategy="papers_contract_form_by_guideline", **kwargs)

    def papers_contract_form_by_checklist(self, **kwargs):
        return self.factory.create(strategy="papers_contract_form_by_checklist", **kwargs)
