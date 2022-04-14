from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    name: str
    batch: int

    @abstractmethod
    def get_value(self):
        ...
