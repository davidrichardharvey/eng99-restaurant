
class Table:
    def __init__(self, num):
        self.bill = []
        self.num = num

    def order(self, item, price, amount=1):
        self.item = item
        self.price = price
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                item["quantity"] += amount
        self.bill.append({"item": item, "price": price, "quantity": amount})

    def remove(self, item, price, amount=1):
        for items in self.bill:
            if items["item"] == item:
                items["quantity"] -= amount
                if items["quantity"] == 0:
                    self.bill.remove(items)
        print("The item has been removed.")


    def get_subtotal(self):
        pass

    def get_total(self, param):
        pass

    def split_bill(self):
        pass
