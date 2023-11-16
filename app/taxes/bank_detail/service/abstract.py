from abc import ABCMeta, abstractmethod


class BankDetailService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, **kwargs): pass
