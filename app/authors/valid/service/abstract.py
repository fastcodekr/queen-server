from abc import ABCMeta, abstractmethod


class ValidService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
