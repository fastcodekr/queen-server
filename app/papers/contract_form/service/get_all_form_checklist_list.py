from app.papers.contract_form.db.dao import select_all_form_checklists, \
    select_all_form_checklist_details
from app.papers.contract_form.model.form_checklist import FormChecklistVO
from app.papers.contract_form.model.form_checklist_detail import FormChecklistDetailVO
from app.papers.contract_form.service.abstract import ContractFormService
from app.utils.dev.response import success_message


class PapersContractFormByChecklist(ContractFormService):
    def handle(self, **kwargs):
        form_checklists = select_all_form_checklists()
        form_checklist_numbers = [form_checklist.number for form_checklist in form_checklists]
        form_checklist_details = select_all_form_checklist_details(form_checklist_numbers=form_checklist_numbers)
        grouped_form_checklist_details = {}
        for form_checklist_detail in form_checklist_details:
            if form_checklist_detail.form_checklist_number not in grouped_form_checklist_details:
                grouped_form_checklist_details[form_checklist_detail.form_checklist_number] = []
            grouped_form_checklist_details[form_checklist_detail.form_checklist_number].append(form_checklist_detail)
        array = []
        for form_checklist in form_checklists:
            form_checklist_vo = FormChecklistVO()
            form_checklist_vo.id = form_checklist.id
            form_checklist_vo.number = form_checklist.number
            form_checklist_vo.content = form_checklist.content
            form_checklist_vo.formChecklistDetailArray = []
            for form_checklist_detail in grouped_form_checklist_details.get(form_checklist.number, []):
                form_checklist_detail_vo = FormChecklistDetailVO()
                form_checklist_detail_vo.id = form_checklist_detail.id
                form_checklist_detail_vo.number = form_checklist_detail.number
                form_checklist_detail_vo.shortName = form_checklist_detail.short_name
                form_checklist_detail_vo.content = form_checklist_detail.content
                form_checklist_detail_vo.formChecklistNumber = form_checklist_detail.form_checklist_number
                form_checklist_vo.formChecklistDetailArray.append(form_checklist_detail_vo)
            array.append(form_checklist_vo)
        return success_message(array=array)
