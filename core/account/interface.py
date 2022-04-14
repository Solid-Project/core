from abc import ABCMeta, abstractmethod

from core.transaction.historic import Historic


class IAccount(metaclass=ABCMeta):
    is_freezed: bool
    historic: Historic

    @abstractmethod
    def register_transaction(self):
        ...

    @abstractmethod
    def freeze(self):
        ...
