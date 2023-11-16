from app.systems.company.db.dao import select_company_by_company_name
from app.systems.company.model.company import CompanyVO
from app.systems.company.service.abstract import CompanyService
from app.utils.dev.response import success_message, not_found_message
from app.utils.dev.time import convert_time_to_au_format


class SystemsCompanyByName(CompanyService):
    def handle(self, **kwargs):
        company_name = kwargs.get("by")
        company = select_company_by_company_name(company_name=company_name)
        if not company:
            return not_found_message()
        company_vo = CompanyVO()
        company_vo.id = company.id
        company_vo.createdAt = convert_time_to_au_format(company.created_at)
        company_vo.updatedAt = convert_time_to_au_format(company.updated_at)
        company_vo.name = company.name
        company_vo.address = company.address
        company_vo.staffId = company.staff_id
        company_vo.boardArray = None
        company_vo.farmArray = None
        company_vo.teamArray = None
        json = company_vo
        return success_message(json=json)
