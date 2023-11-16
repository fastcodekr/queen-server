from abc import ABCMeta, abstractmethod


class TeamService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
