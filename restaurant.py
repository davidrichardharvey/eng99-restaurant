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







