from typing import Optional

from pydantic import BaseModel

from app.papers.contract_form.model.form_checklist_detail import FormChecklistDetailVO


class FormChecklistVO(BaseModel):
    id: Optional[str] = None
    number: Optional[str] = None
    content: Optional[str] = None
    formChecklistDetailArray: Optional[list[FormChecklistDetailVO]] = None
