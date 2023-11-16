from abc import ABCMeta, abstractmethod


class WorkerService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
