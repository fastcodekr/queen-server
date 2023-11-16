from app.papers.contract_form.db.dao import select_all_form_agrees
from app.papers.contract_form.model.form_agree import FormAgreeVO
from app.papers.contract_form.service.abstract import ContractFormService
from app.utils.dev.response import success_message


class PapersContractFormByAgree(ContractFormService):
    def handle(self, **kwargs):
        form_agrees = select_all_form_agrees()
        array = []
        for form_agree in form_agrees:
            form_agree_vo = FormAgreeVO()
            form_agree_vo.id = form_agree.id
            form_agree_vo.number = form_agree.number
            form_agree_vo.content = form_agree.content
            array.append(form_agree_vo)
        return success_message(array=array)
