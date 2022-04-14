from abc import ABCMeta, abstractmethod
from datetime import date
from typing import List, Set

from core.investment.interface import IInvestment
from core.product.interface import IProduct


class IPortfolio(metaclass=ABCMeta):
    name: str
    investment_list: List[IInvestment]

    @abstractmethod
    def get_product_list(self) -> Set[IProduct]:
        ...

    @abstractmethod
    def get_profit(
        self,
        portfolio_products: Set[IProduct],
        start_date: date,
        end_date: date,
    ):
        ...
