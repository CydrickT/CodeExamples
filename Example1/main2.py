from address import Address
from article import Article, NonTaxableArticle, TaxableArticle
from basket import Basket
from client import Client
from order import Order
from warehouse_manager import WarehouseManager

# class variable vs instance variable

address1: Address = Address("123", "4e boulevard", "Montreal", "QC", "Canada", "J7V 1A1")
client1: Client = Client("John", "Doe", "111-222-3333", address1)

address2: Address = Address("567", "8e boulevard", "Montreal", "QC", "Canada", "J7V 2A2")
client2: Client = Client("Jane", "Doe", "444-555-6666", address2)

lollipop : Article = TaxableArticle(523, "One lollipop", "It's a nice one, with the swirls and all, but is heavily taxed!", 1.00)

warehouse_manager: WarehouseManager = WarehouseManager()
warehouse_manager.increaseStock(lollipop, 2)

basket_client1 : Basket = Basket(client1)
basket_client1.addArticle(lollipop, 1)

basket_client2: Basket = Basket(client2)
basket_client2.addArticle(lollipop, 1)

print("========== Ordering " + client1.first_name + "'s Basket ==========")
order_client1 : Order = basket_client1.order(warehouse_manager)
print("========== Printing " + client1.first_name + "'s Receipt ==========")
order_client1.print_receipt()

print("========== Ordering " + client2.first_name + "'s Basket ==========")
order_client2 : Order = basket_client2.order(warehouse_manager)
print("========== Printing " + client2.first_name + "'s Receipt ==========")
order_client2.print_receipt()

print("========== Setting provencial tax to 100% ==========")
Order.provencial_tax_rate = 1
print("========== Printing " + client1.first_name + "'s Receipt ==========")
order_client1.print_receipt()
print("========== Printing " + client2.first_name + "'s Receipt ==========")
order_client2.print_receipt()


print("========== Setting federal tax to 100% on order of client 1 ==========")
order_client1.federal_tax_rate = 1
print("========== Printing " + client1.first_name + "'s Receipt ==========")
order_client1.print_receipt()
print("========== Printing " + client2.first_name + "'s Receipt ==========")
order_client2.print_receipt()
