from abc import ABCMeta, abstractmethod


class PersonService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
