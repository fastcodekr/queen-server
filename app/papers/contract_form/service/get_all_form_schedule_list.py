from app.papers.contract_form.db.dao import select_all_form_schedules
from app.papers.contract_form.model.form_schedule import FormScheduleVO
from app.papers.contract_form.service.abstract import ContractFormService
from app.utils.dev.response import success_message


class PapersContractFormBySchedule(ContractFormService):
    def handle(self, **kwargs):
        form_schedules = select_all_form_schedules()
        array = []
        for form_schedule in form_schedules:
            form_schedule_vo = FormScheduleVO()
            form_schedule_vo.id = form_schedule.id
            form_schedule_vo.number = form_schedule.number
            form_schedule_vo.title = form_schedule.title
            form_schedule_vo.content1 = form_schedule.content1
            form_schedule_vo.content2 = form_schedule.content2
            form_schedule_vo.content21 = form_schedule.content21
            form_schedule_vo.content22 = form_schedule.content22
            array.append(form_schedule_vo)
        return success_message(array=array)
