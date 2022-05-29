from time import sleep
from typing import Dict
from article import Article


class WarehouseManager:
    def __init__(self):
        self._stock: Dict[Article, int] = {}
        
    def hasStock(self, article: Article, quantity: int) -> bool:
        sleep(1);
        if article in self._stock:
            return self._stock[article] >= quantity
        else:
            return False

    def increaseStock(self, article: Article, quantity_added: int) -> None:
        if article in self._stock:
            self._stock[article] += quantity_added
        else:
            self._stock[article] = quantity_added

    def reduceStock(self, article: Article, quantity_reduced: int) -> None:
        sleep(1);
        if article in self._stock:
            self._stock[article] -= quantity_reduced

    def getArticleById(self, id) -> Article:
        foundArticle: Article = None

        for article in self._stock:
            if(article.id == id):
                foundArticle = article

        return foundArticle

    def printAllArticles(self) -> None:
        for article in self._stock:
            print(article.getFormattedDescription())
            print("Number of articles: " + str(self._stock[article]))
            print("-"*20)