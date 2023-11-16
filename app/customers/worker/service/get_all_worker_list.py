from app.customers.worker.db.dao import select_all_workers
from app.customers.worker.model.worker import WorkerViewTableVO
from app.customers.worker.service.abstract import WorkerService
from app.utils.dev.response import success_message
from app.utils.dev.time import convert_time_to_au_format
from app.utils.dev.tool import mask_string


class CustomersWorkerByAll(WorkerService):
    def handle(self, **kwargs):
        workers = select_all_workers()
        if not workers:
            return success_message()
        array = []
        for worker in workers:
            # FIXME: 인증 적용 후 marking 해제
            worker_vo = WorkerViewTableVO()
            worker_vo.id = worker.id
            worker_vo.createdAt = convert_time_to_au_format(worker.created_at)
            worker_vo.updatedAt = convert_time_to_au_format(worker.updated_at)
            worker_vo.locationId = worker.location_id
            worker_vo.locationName = worker.location_name
            worker_vo.farmId = worker.farm_id
            worker_vo.farmName = worker.farm_name
            worker_vo.teamId = worker.team_id
            worker_vo.teamName = worker.team_name
            worker_vo.firstName = worker.first_name
            worker_vo.lastName = worker.last_name
            worker_vo.englishName = worker.english_name
            worker_vo.bsb = mask_string(worker.bsb)
            worker_vo.accountNumber = mask_string(worker.account_number)
            worker_vo.email = mask_string(worker.email)
            worker_vo.cellPhone = mask_string(worker.cell_phone)
            worker_vo.taxFileNumber = mask_string(worker.tax_file_number)
            worker_vo.birthDate = worker.birth_date
            worker_vo.gender = worker.gender
            worker_vo.nationality = worker.nationality
            worker_vo.passportNumber = mask_string(worker.passport_number)
            worker_vo.visaGrantNumber = mask_string(worker.visa_grant_number)
            worker_vo.fundName = worker.fund_name
            worker_vo.memberNumber = mask_string(worker.member_number)
            worker_vo.address = mask_string(worker.address)
            worker_vo.startDate = worker.start_date
            worker_vo.endDate = worker.end_date
            worker_vo.tax = worker.tax
            worker_vo.farmNumber = worker.farm_number
            worker_vo.memo = worker.memo
            array.append(worker_vo)
        return success_message(array=array, )
