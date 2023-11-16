from abc import ABCMeta, abstractmethod


class Draft53Service(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
