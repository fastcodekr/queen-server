from app.customers.farm.service.get_all_farm_list_by_location import CustomersFarmByLocation

strategy_map = {
    "customers_farm_by_location": CustomersFarmByLocation()
}


class FarmFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)
