from app.customers.worker.service.get_all_worker_list import CustomersWorkerByAll

strategy_map = {
    "customers_worker_by_all": CustomersWorkerByAll(),
}


class WorkerFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)
