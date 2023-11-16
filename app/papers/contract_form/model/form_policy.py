from typing import Optional

from pydantic import BaseModel

from app.papers.contract_form.model.form_policy_detail import FormPolicyDetailVO


class FormPolicyVO(BaseModel):
    id: Optional[str] = None
    number: Optional[str] = None
    title: Optional[str] = None
    contentHead: Optional[str] = None
    contentTail: Optional[str] = None
    formPolicyDetailArray: Optional[list[FormPolicyDetailVO]] = None
