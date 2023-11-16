from app.atoms.view_tables.worker_view_table import WorkerViewTable
from app.utils.dev.database import execute_query


def select_all_workers() -> list[WorkerViewTable | None]:
    query = """
    select 
        id,
        created_at,
        updated_at,
        location_id,
        location_name,
        farm_id,
        farm_name,
        team_id,
        team_name,
        first_name,
        last_name,
        english_name,
        bsb,
        account_number,
        email,
        cell_phone,
        tax_file_number,
        birth_date,
        gender,
        nationality,
        passport_number,
        visa_grant_number,
        fund_name,
        member_number,
        address,
        start_date,
        end_date,
        tax,
        farm_number,
        memo
    from worker_view
    order by created_at desc;
    """
    workers = execute_query(query)
    array = [
        WorkerViewTable(
            id=worker[0],
            created_at=worker[1],
            updated_at=worker[2],
            location_id=worker[3],
            location_name=worker[4],
            farm_id=worker[5],
            farm_name=worker[6],
            team_id=worker[7],
            team_name=worker[8],
            first_name=worker[9],
            last_name=worker[10],
            english_name=worker[11],
            bsb=worker[12],
            account_number=worker[13],
            email=worker[14],
            cell_phone=worker[15],
            tax_file_number=worker[16],
            birth_date=worker[17],
            gender=worker[18],
            nationality=worker[19],
            passport_number=worker[20],
            visa_grant_number=worker[21],
            fund_name=worker[22],
            member_number=worker[23],
            address=worker[24],
            start_date=worker[25],
            end_date=worker[26],
            tax=worker[27],
            farm_number=worker[28],
            memo=worker[29],
        ) for worker in workers
    ] if workers else []
    return array
