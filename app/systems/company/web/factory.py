from app.systems.company.service.get_all_company_list import SystemsCompanyByAll
from app.systems.company.service.get_company_by_name import SystemsCompanyByName

strategy_map = {
    "systems_company_by_all": SystemsCompanyByAll(),
    "systems_company_by_name": SystemsCompanyByName(),
}


class CompanyFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)
