
from article import Article


class OrderItem:
    
    def __init__(self, article: Article):
        self.name = article.name
        self.unit_price = article.unit_price
        self.is_taxable = article.is_taxable
