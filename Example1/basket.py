from typing import Dict
from article import Article
from order import Order
from client import Client
from warehouse_manager import WarehouseManager


class Basket:

    def __init__(self, client: Client):
        self._article_list: Dict[Article, int] = {}
        self.client: Client = client

    def addArticle(self, article: Article, quantity: int) -> None:
        if article in self._article_list:
            self._article_list[article] += quantity
        else:
            self._article_list[article] = quantity

    def removeArticle(self, article: Article) -> None:
        self._article_list.pop(article)

    def order(self, warehouse_manager: WarehouseManager) -> Order:
        if self._hasStockForAllArticles(warehouse_manager):
            self._reduceStockForAllArticles(warehouse_manager)
            return Order(self._article_list)
        else:
            print("Order did not go through because of lack of items")
            return None

    def _hasStockForAllArticles(self, warehouse_manager: WarehouseManager) -> bool:
        for article in self._article_list:
            if warehouse_manager.hasStock(article, self._article_list[article]) == False:
                return False
        return True

    def _reduceStockForAllArticles(self, warehouse_manager: WarehouseManager) -> None:
        for article in self._article_list:
            warehouse_manager.reduceStock(article, self._article_list[article])
            
