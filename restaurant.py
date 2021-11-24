class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        self.item = item
        self.price = price
        for menu_item in self.bill:
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] += quantity
                return

        self.bill.append({"item": item, "price": price, "quantity": quantity})

        print("Item has been added.")


    def remove(self, item, price, quantity=1):
        for menu_item in self.bill:
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] -= quantity
                if menu_item["quantity"] <= 0:
                    self.bill.remove(menu_item)

        print("Item has been removed.")

