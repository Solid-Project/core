from abc import ABCMeta, abstractmethod
from enum import Enum

from core.product.interface import IProduct


class __TransactionOperations(int, Enum):
    SELL = -1
    BUY = 1


class __TransactionExecution(str, Enum):
    EXECUTED = "EXECUTED"
    PARTIALLY_EXECUTED = "PARTIALLY_EXECUTED"
    NOT_EXECUTED = "NOT_EXECUTED"


class ITransaction(metaclass=ABCMeta):
    operation: __TransactionOperations
    product: IProduct
    quantity: int
    executed: __TransactionExecution

    @abstractmethod
    def make(self):
        ...

    @abstractmethod
    def calculate_value(self):
        ...
