from app.atoms.company import Company
from app.utils.dev.database import execute_query


def select_all_companies() -> list[Company | None]:
    query = """
    select 
        id ,
        created_at ,
        updated_at,
        name,
        address,
        staff_id
    from companies
    order by created_at
    """
    companies = execute_query(query=query)
    array = [
        Company(
            id=company[0],
            created_at=company[1],
            updated_at=company[2],
            name=company[3],
            address=company[4],
            staff_id=company[5],
        ) for company in companies
    ] if companies else []
    return array


def select_company_by_company_name(company_name: str) -> Company | None:
    if not company_name:
        return None
    query = f"""
    select 
        id ,
        created_at ,
        updated_at,
        name,
        address,
        staff_id
    from companies
    where name = '{company_name}'
    limit 1
    """
    company = execute_query(query=query)[0]
    if not company:
        return None
    return Company(
        id=company[0],
        created_at=company[1],
        updated_at=company[2],
        name=company[3],
        address=company[4],
        staff_id=company[5],
    )
