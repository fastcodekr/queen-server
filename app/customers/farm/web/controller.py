from app.customers.farm.web.factory import FarmFactory


class FarmController(object):
    def __init__(self):
        self.factory = FarmFactory

    def customers_farm_by_location(self, **kwargs):
        return self.factory.create(strategy="customers_farm_by_location", **kwargs)
