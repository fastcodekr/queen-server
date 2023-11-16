from app.systems.company.db.dao import select_all_companies
from app.systems.company.model.company import CompanyVO
from app.systems.company.service.abstract import CompanyService
from app.utils.dev.response import success_message
from app.utils.dev.time import convert_time_to_au_format


class SystemsCompanyByAll(CompanyService):
    def handle(self, **kwargs):
        companies = select_all_companies()
        array = []
        for company in companies:
            company_vo = CompanyVO()
            company_vo.id = company.id
            company_vo.createdAt = convert_time_to_au_format(company.created_at)
            company_vo.updatedAt = convert_time_to_au_format(company.updated_at)
            company_vo.name = company.name
            company_vo.address = company.address
            company_vo.staffId = None
            company_vo.boardArray = None
            company_vo.farmArray = None
            company_vo.teamArray = None
            array.append(company_vo)
        return success_message(array=array)
