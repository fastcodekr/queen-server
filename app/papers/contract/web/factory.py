from app.papers.contract.service.insert_contract import PapersContractDoAdd

strategy_map = {
    "papers_contract_do_add": PapersContractDoAdd(),
}


class ContractFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)
