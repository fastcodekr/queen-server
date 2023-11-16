from abc import ABCMeta, abstractmethod


class FarmService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
