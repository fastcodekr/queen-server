from app.papers.contract_form.db.dao import select_all_form_guidelines
from app.papers.contract_form.model.form_guideline import FormGuidelineVO
from app.papers.contract_form.service.abstract import ContractFormService
from app.utils.dev.response import success_message


class PapersContractFormByGuideline(ContractFormService):
    def handle(self, **kwargs):
        form_guidelines = select_all_form_guidelines()
        array = []
        for form_guideline in form_guidelines:
            form_guideline_vo = FormGuidelineVO()
            form_guideline_vo.id = form_guideline.id
            form_guideline_vo.number = form_guideline.number
            form_guideline_vo.title = form_guideline.title
            form_guideline_vo.content = form_guideline.content
            array.append(form_guideline_vo)
        return success_message(array=array)
