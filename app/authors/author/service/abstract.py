from abc import ABCMeta, abstractmethod


class AuthorService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
