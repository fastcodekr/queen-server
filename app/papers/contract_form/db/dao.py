from app.atoms.contract_form.form_agree import FormAgree
from app.atoms.contract_form.form_checklist import FormChecklist
from app.atoms.contract_form.form_checklist_detail import FormChecklistDetail
from app.atoms.contract_form.form_guideline import FormGuideline
from app.atoms.contract_form.form_policy import FormPolicy
from app.atoms.contract_form.form_policy_detail import FormPolicyDetail
from app.atoms.contract_form.form_schedule import FormSchedule
from app.utils.dev.database import execute_query


def select_all_form_policies() -> list[FormPolicy | None]:
    query = """
    select     
        id,
        number,
        title,
        content_head,
        content_tail
    from form_policies
    order by number;
    """
    form_policies = execute_query(query=query)
    array = [
        FormPolicy(
            id=form_policy[0],
            number=form_policy[1],
            title=form_policy[2],
            content_head=form_policy[3],
            content_tail=form_policy[4],
        )
        for form_policy in form_policies
    ] if form_policies else []
    return array


def select_all_form_policy_details(form_policy_numbers: list[int | None]) -> list[FormPolicyDetail | None]:
    if not form_policy_numbers:
        return []
    tpl = tuple(form_policy_numbers) if len(form_policy_numbers) > 1 else f"({form_policy_numbers[0]})"
    query = f"""
    select
        id,
        number,
        content,
        form_policy_number
    from form_policy_details
    where form_policy_number in {tpl}
    order by number;
    """
    form_policy_details = execute_query(query=query)
    array = [
        FormPolicyDetail(
            id=form_policy_detail[0],
            number=form_policy_detail[1],
            content=form_policy_detail[2],
            form_policy_number=form_policy_detail[3],
        )
        for form_policy_detail in form_policy_details
    ] if form_policy_details else []
    return array


def select_all_form_agrees() -> list[FormAgree | None]:
    query = """
    select 
        id,
        number,
        content
    from form_agrees
    order by number;
    """
    form_agrees = execute_query(query=query)
    array = [
        FormAgree(
            id=form_agree[0],
            number=form_agree[1],
            content=form_agree[2],
        )
        for form_agree in form_agrees
    ] if form_agrees else []
    return array


def select_all_form_schedules() -> list[FormSchedule | None]:
    query = """
    select
        id,
        number,
        title,
        content1,
        content2,
        content21,
        content22
    from form_schedules
    order by number;
    """
    form_schedules = execute_query(query=query)
    array = [
        FormSchedule(
            id=form_schedule[0],
            number=form_schedule[1],
            title=form_schedule[2],
            content1=form_schedule[3],
            content2=form_schedule[4],
            content21=form_schedule[5],
            content22=form_schedule[6],
        )
        for form_schedule in form_schedules
    ] if form_schedules else []
    return array


def select_all_form_guidelines() -> list[FormGuideline | None]:
    query = """
    select
        id,
        number,
        title,
        content
    from form_guidelines
    order by number;
    """
    form_guidelines = execute_query(query=query)
    array = [
        FormGuideline(
            id=form_guideline[0],
            number=form_guideline[1],
            title=form_guideline[2],
            content=form_guideline[3],
        )
        for form_guideline in form_guidelines
    ] if form_guidelines else []
    return array


def select_all_form_checklists() -> list[FormChecklist | None]:
    query = """
    select
        id,
        number,
        content
    from form_checklists
    order by number;
    """
    form_checklists = execute_query(query=query)
    array = [
        FormChecklist(
            id=form_checklist[0],
            number=form_checklist[1],
            content=form_checklist[2],
        )
        for form_checklist in form_checklists
    ] if form_checklists else []
    return array


def select_all_form_checklist_details(form_checklist_numbers: list[int | None]) -> list[FormChecklistDetail | None]:
    if not form_checklist_numbers:
        return []
    tpl = tuple(form_checklist_numbers) if len(form_checklist_numbers) > 1 else f"({form_checklist_numbers[0]})"
    query = f"""
    select
        id,
        number,
        short_name,
        content,
        form_checklist_number
    from form_checklist_details
    where form_checklist_number in {tpl}
    order by number;
    """
    form_checklist_details = execute_query(query=query)
    array = [
        FormChecklistDetail(
            id=form_checklist_detail[0],
            number=form_checklist_detail[1],
            short_name=form_checklist_detail[2],
            content=form_checklist_detail[3],
            form_checklist_number=form_checklist_detail[4],
        )
        for form_checklist_detail in form_checklist_details
    ] if form_checklist_details else []
    return array
