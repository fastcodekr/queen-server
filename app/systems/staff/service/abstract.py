from abc import ABCMeta, abstractmethod


class StaffService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
