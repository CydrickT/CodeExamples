from address import Address
from article import Article, NonTaxableArticle, TaxableArticle
from basket import Basket
from client import Client
from order import Order
from warehouse_manager import WarehouseManager


address1: Address = Address("123", "4e boulevard", "Montreal", "QC", "Canada", "J7V 1A1")
client1: Client = Client("John", "Doe", "111-222-3333", address1)

address2: Address = Address("567", "8e boulevard", "Montreal", "QC", "Canada", "J7V 2A2")
client2: Client = Client("Jane", "Doe", "444-555-6666", address2)

computer : Article = TaxableArticle(42, "IBM Thinkpad", "Fantastic and fast computer", 1499.99)
mouse : Article = TaxableArticle(6152, "Logitech MX Master", "A nice and ergonomic mouse", 59.99)
bread: Article = NonTaxableArticle(2416, "POM bread loaf", "Something nice to eat, also not taxable!", 4.99)

print("========== Printing all articles before adding anything ==========")
warehouse_manager: WarehouseManager = WarehouseManager()
warehouse_manager.increaseStock(computer, 1)
warehouse_manager.increaseStock(mouse, 3)
warehouse_manager.increaseStock(bread, 10)
warehouse_manager.printAllArticles()

basket_client1 : Basket = Basket(client1)
basket_client2 : Basket = Basket(client2)

basket_client1.addArticle(computer, 1)
basket_client1.addArticle(mouse, 1)
basket_client1.addArticle(bread, 4)

#basket_client2.addArticle(computer, 1)
basket_client2.addArticle(mouse, 2)
basket_client2.addArticle(bread, 2)

print("========== Ordering Client 1's Basket ==========")
order_client1 : Order = basket_client1.order(warehouse_manager)
print("========== Printing Client 1's Receipt ==========")
if order_client1 is not None:
    order_client1.print_receipt()

print("========== Ordering Client 2's Basket ==========")
order_client2 : Order = basket_client2.order(warehouse_manager)
print("========== Printing Client 2's Receipt ==========")
if order_client2 is not None:
    order_client2.print_receipt()

print("========== Reprinting all articles ==========")

warehouse_manager.printAllArticles()
