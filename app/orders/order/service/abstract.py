from abc import ABCMeta, abstractmethod


class OrderService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
