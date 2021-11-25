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
        sub = 0
        for i in self.bill:
            price = i["price"]
            amount = i["quantity"]
            sub += price * amount
        return round(sub, 2)

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        service_charge = subtotal * service_charge
        total = subtotal + service_charge
        summary = {"Sub Total": f"£{subtotal:.2f}",
                   "Service Charge": f"£{service_charge:.2f}",
                   "Total": f"£{total:.2f}"}
        return summary

    def split_bill(self):
        subtotal = self.get_subtotal()
        split = subtotal / self.num
        return split
