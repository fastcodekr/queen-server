from app.customers.worker.web.factory import WorkerFactory


class WorkerController(object):
    def __init__(self):
        self.factory = WorkerFactory()

    def customers_worker_by_all(self, **kwargs):
        return self.factory.create(strategy="customers_worker_by_all", **kwargs)
