from app.atoms.farm import Farm
from app.atoms.location import Location
from app.utils.dev.database import execute_query


def select_all_locations() -> list[Location | None]:
    query = """
    select
        id,
        created_at,
        updated_at,
        name
    from locations
    order by created_at;
    """
    locations = execute_query(query=query)
    array = [
        Location(
            id=location[0],
            created_at=location[1],
            updated_at=location[2],
            name=location[3],
        ) for location in locations
    ] if locations else []
    return array


def select_all_farms(location_ids: list[int | None]) -> list[Farm | None]:
    if not location_ids:
        return []
    tpl = tuple(location_ids) if len(location_ids) > 1 else f"({location_ids[0]})"
    query = f"""
    select
        id,
        created_at,
        updated_at,
        name,
        location_id,
        company_id
    from farms
    where location_id in {tpl}
    order by created_at
    """
    farms = execute_query(query=query)
    array = [
        Farm(
            id=farm[0],
            created_at=farm[1],
            updated_at=farm[2],
            name=farm[3],
            location_id=farm[4],
            company_id=farm[5],
        ) for farm in farms
    ] if farms else []
    return array
