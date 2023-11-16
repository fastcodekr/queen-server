from app.papers.contract_form.db.dao import select_all_form_policies, select_all_form_policy_details
from app.papers.contract_form.model.form_policy import FormPolicyVO
from app.papers.contract_form.model.form_policy_detail import FormPolicyDetailVO
from app.papers.contract_form.service.abstract import ContractFormService
from app.utils.dev.response import success_message


class PapersContractFormByPolicy(ContractFormService):
    def handle(self, **kwargs):
        form_policies = select_all_form_policies()
        form_policy_numbers = [form_policy.number for form_policy in form_policies]
        form_policy_details = select_all_form_policy_details(form_policy_numbers=form_policy_numbers)
        grouped_form_policy_details = {}
        for form_policy_detail in form_policy_details:
            if form_policy_detail.form_policy_number not in grouped_form_policy_details:
                grouped_form_policy_details[form_policy_detail.form_policy_number] = []
            grouped_form_policy_details[form_policy_detail.form_policy_number].append(form_policy_detail)
        array = []
        for form_policy in form_policies:
            form_policy_vo = FormPolicyVO()
            form_policy_vo.id = form_policy.id
            form_policy_vo.number = form_policy.number
            form_policy_vo.title = form_policy.title
            form_policy_vo.contentHead = form_policy.content_head
            form_policy_vo.contentTail = form_policy.content_tail
            form_policy_vo.formPolicyDetailArray = []
            for form_policy_detail in grouped_form_policy_details.get(form_policy.number, []):
                form_policy_detail_vo = FormPolicyDetailVO()
                form_policy_detail_vo.id = form_policy_detail.id
                form_policy_detail_vo.number = form_policy_detail.number
                form_policy_detail_vo.content = form_policy_detail.content
                form_policy_detail_vo.formPolicyNumber = form_policy_detail.form_policy_number
                form_policy_vo.formPolicyDetailArray.append(form_policy_detail_vo)
            array.append(form_policy_vo)
        return success_message(array=array)


if __name__ == '__main__':
    FormPolicyVO()
