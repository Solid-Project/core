from abc import ABCMeta

from core.operation.interface import IOperation


class ISell(IOperation, metaclass=ABCMeta):
    ...
