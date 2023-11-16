from abc import ABCMeta, abstractmethod


class CalculatorService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
