from app.papers.contract.web.factory import ContractFactory


class ContractController(object):
    def __init__(self):
        self.factory = ContractFactory

    def papers_contract_do_add(self, **kwargs):
        return self.factory.create(strategy="papers_contract_do_add", **kwargs)
