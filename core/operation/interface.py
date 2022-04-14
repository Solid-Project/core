from abc import ABCMeta
from datetime import datetime

from core.product.interface import IProduct


class IOperation(metaclass=ABCMeta):
    product: IProduct
    datetime: datetime
    price: float
