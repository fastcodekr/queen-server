from abc import ABCMeta, abstractmethod


class CompanyService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
