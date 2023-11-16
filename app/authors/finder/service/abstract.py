from abc import ABCMeta, abstractmethod


class FinderService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
