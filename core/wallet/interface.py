from abc import ABCMeta, abstractmethod
from datetime import date
from typing import Set

from core.portfolio.interface import IPortfolio


class IWallet(metaclass=ABCMeta):
    portfolio_list = Set[IPortfolio]

    @abstractmethod
    def get_portfolio_list(self) -> Set[IPortfolio]:
        ...

    @abstractmethod
    def get_profit(
        self,
        wallet_portfolios: Set[IPortfolio],
        start_date: date,
        end_date: date,
    ):
        ...
