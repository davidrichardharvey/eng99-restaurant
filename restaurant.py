class Table:
    def __init__(self, person):
        self.person = person
        self.bill = []

    def order(self, item, price, quantity):
        return self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity):
        for n in self.bill:
            if n["item"] == item:
                n["quantity"] -= quantity
                if n["quantity"] == 0:
                    self.bill.remove(n)

    def get_subtotal(self):
        menu_total = 0
        for menu in self.bill:
            menu_total += menu["price"] * menu["quantity"]
            return menu_total

    def get_total(self):
        {"Sub Total": "£120.00", "Service Charge": "£12.00", "Total": "£132.00"}




table01 = Table(5)
table01.order("Risotto", 12.50, 2)
print(table01.bill)
table01.order("Burrito", 20.43, 3)
table01.remove("Burrito", 20.43, 2)
print(table01.bill)
print(table01.get_subtotal())
# print(table01.get_total(0.15))
# print(table01.split_bill())




    #
    # def setUp(self, table) -> None:
    #     self.table02.table = Table(2)
    #     self.table05.table = Table(5)
    #     self.table06.table = Table(6)
    #     return self.setUp()
    #
    # def order(self, table):
    #     self.table02.order('Food', 10.00, 3)
    #     self.table05.order('Food', 15.00, 2)
    #     self.table06.order('Food', 5, 1)
    #
    # def order_no_quantity(self):
    #     self.table02.order('Food', 10.00)
    #     self.table05.order('Food', 15)
    #     self.table06.order('Food', 5)
    #
    # def test_remove(self):
    #     self.table02.order('Food', 10.00, 5)
    #     self.table02.remove('Food', 10.00, 3)

# class Table():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def getPrice(self):
#         return self.price
#
#     def __str__(self):
#         return self.name + ' : ' + str(self.getprice())
#
#     # Defining a function for building a Menu
#     # which generates list of Food
#     def buildmenu(names, costs):
#         menu = []
#         for i in range(len(names)):
#             menu.append(Table(names[i], costs[i]))
#         return menu
#
#     # items
#     names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake']
#
#     # prices
#     costs = [250, 150, 180, 70, 65, 55, 120, 350]
#
#     # building food menu
#     Table = buildmenu(names, costs)
#
#     n = 1
#     for el in Table:
#         print(n, '. ', el)
#         n = n + 1
#
# def tax(bill):
#     """Adds 8% tax to a restaurant bill."""
#     bill *= 1.08
#     print
#     "With tax: %f" % bill
#     return bill
#
#
# def tip(bill):
#     """Adds 15% tip to a restaurant bill."""
#     bill *= 1.15
#     print
#     "With tip: %f" % bill
#     return bill

#
# meal_cost = 100
# meal_with_tax = tax(meal_cost)
# meal_with_tip = tip(meal_with_tax)


