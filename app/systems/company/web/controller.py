from app.systems.company.web.factory import CompanyFactory


class CompanyController(object):
    def __init__(self):
        self.factory = CompanyFactory

    def systems_company_by_all(self, **kwargs):
        return self.factory.create(strategy="systems_company_by_all", **kwargs)

    def systems_company_by_name(self, **kwargs):
        return self.factory.create(strategy="systems_company_by_name", **kwargs)
