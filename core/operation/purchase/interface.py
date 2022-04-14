from abc import ABCMeta

from core.operation.interface import IOperation


class IPurchase(IOperation, metaclass=ABCMeta):
    ...
