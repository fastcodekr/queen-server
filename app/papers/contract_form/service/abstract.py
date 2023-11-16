from abc import ABCMeta, abstractmethod


class ContractFormService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
