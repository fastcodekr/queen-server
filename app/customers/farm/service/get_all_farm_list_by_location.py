from app.customers.farm.db.dao import select_all_locations, select_all_farms
from app.customers.farm.model.farm import FarmVO
from app.customers.farm.model.location import LocationVO
from app.customers.farm.service.abstract import FarmService
from app.utils.dev.response import success_message
from app.utils.dev.time import convert_time_to_au_format


class CustomersFarmByLocation(FarmService):
    def handle(self, **kwargs):
        locations = select_all_locations()
        location_ids = [location.id for location in locations]
        farms = select_all_farms(location_ids=location_ids)
        grouped_farms = {}
        for farm in farms:
            if farm.location_id not in grouped_farms:
                grouped_farms[farm.location_id] = []
            grouped_farms[farm.location_id].append(farm)
        array = []
        for location in locations:
            location_vo = LocationVO()
            location_vo.id = location.id
            location_vo.createdAt = convert_time_to_au_format(location.created_at)
            location_vo.updatedAt = convert_time_to_au_format(location.updated_at)
            location_vo.name = location.name
            location_vo.farmArray = []
            for farm in grouped_farms.get(location.id, []):
                farm_vo = FarmVO()
                farm_vo.id = farm.id
                farm_vo.createdAt = convert_time_to_au_format(farm.created_at)
                farm_vo.updatedAt = convert_time_to_au_format(farm.updated_at)
                farm_vo.name = farm.name
                farm_vo.locationId = farm.location_id
                farm_vo.companyId = farm.company_id
                farm_vo.orderArray = None
                location_vo.farmArray.append(farm_vo)
            array.append(location_vo)
        return success_message(array=array)
