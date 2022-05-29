from typing import Dict

from article import Article
from order_item import OrderItem


class Order:

    provencial_tax_rate: float = 0.09975
    federal_tax_rate: float = 0.05
    
    def __init__(self, article_list: Dict[Article, int]):
        self._order_item_list: Dict[OrderItem, int] = {}
        self._build_order(article_list)

    def _build_order(self, article_list: Dict[Article, int]):
        for article in article_list:
            self._order_item_list[OrderItem(article)] = article_list[article]

    def print_receipt(self) -> None:
        for order_item in self._order_item_list:
            item_total: float = order_item.unit_price * self._order_item_list[order_item] 
            print('{0: <30}'.format(str(self._order_item_list[order_item]) + "x " + order_item.name) + "{:.2f}".format(item_total))
        print("-"*35)
        print('{0: <30}'.format("Subtotal: ") + "{:.2f}".format(self.subtotal))
        print('{0: <30}'.format("Provencial Tax: ") + "{:.2f}".format(self.proviencial_tax_total))
        print('{0: <30}'.format("Federal Tax: ") + "{:.2f}".format(self.federal_tax_total))
        print('{0: <30}'.format("Total: ") + "{:.2f}".format(self.total))

    @property
    def subtotal(self) -> float:
        subtotal: float = 0.0
        for order_item in self._order_item_list:
            subtotal += order_item.unit_price * self._order_item_list[order_item]
        return subtotal

    @property
    def proviencial_tax_total(self) -> float:
        provencial_tax_total: float = 0.0
        for order_item in self._order_item_list:
            if order_item.is_taxable:
                provencial_tax_total += order_item.unit_price * self._order_item_list[order_item] * Order.provencial_tax_rate
        return provencial_tax_total

    @property
    def federal_tax_total(self) -> float:
        federal_tax_total: float = 0.0
        for order_item in self._order_item_list:
            if order_item.is_taxable:
                federal_tax_total += order_item.unit_price * self._order_item_list[order_item] * Order.federal_tax_rate
        return federal_tax_total

    @property
    def total(self) -> float:
        return self.subtotal + self.proviencial_tax_total + self.federal_tax_total
