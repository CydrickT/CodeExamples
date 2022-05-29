from abc import ABC


class Article(ABC):
    def __init__(self, id:int, name: str, description: str, unit_price: float, is_taxable: bool):
        self.id = id
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.is_taxable = is_taxable

    def getFormattedDescription(self) -> str:
        return "Article " + str(self.id) + ": \n" + self.name + "\n" + self.description

class NonTaxableArticle(Article):

    def __init__(self, id:int, name: str, description: str, unit_price: float):
        super().__init__(id, name, description, unit_price, False)

class TaxableArticle(Article):

    def __init__(self, id:int, name: str, description: str, unit_price: float):
        super().__init__(id, name, description, unit_price, True)

class ArticleInRebate(Article):

    def __init__(self, id:int, name: str, description: str, unit_price: float):
        super().__init__(id, name, description, unit_price, True)

    def getFormattedDescription(self) -> str:
        return super().getFormattedDescription() + "\n --> Get it today for the low low price of ${0:.3g}! <--".format(self.unit_price)
