
from Example1.article import Article


class OrderItem:
    
    def __init__(self, article: Article, unit_price: float, is_taxable: bool):
        self.name = article.name
        self.unit_price = unit_price
        self.is_taxable = is_taxable
