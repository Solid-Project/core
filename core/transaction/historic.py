from typing import List, Set

from core.transaction.interface import ITransaction


class Historic:
    transaction_list: List[ITransaction]

    def get_purchase_transactions(self) -> Set[ITransaction]:
        ...

    def get_sell_transactions(self) -> Set[ITransaction]:
        ...
