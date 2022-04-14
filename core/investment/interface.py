from abc import ABCMeta, abstractclassmethod
from datetime import date

from core.operation.purchase.interface import IPurchase


class IInvestment(metaclass=ABCMeta):
    purchase: IPurchase
    price_variation: float

    @abstractclassmethod
    def calculate_profit(self, start_date: date, end_date: date):
        ...
