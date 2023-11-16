from abc import ABCMeta, abstractmethod


class BoardService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
