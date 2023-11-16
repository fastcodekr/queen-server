from abc import ABCMeta, abstractmethod


class ContractService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
