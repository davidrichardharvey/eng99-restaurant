class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

    # order list created with item, price and quantity

    def order(self, item, price, quantity=1):
        self.item = item
        self.price = price
        for menu_item in self.bill:
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] += quantity
                return

        self.bill.append({"item": item, "price": price, "quantity": quantity})

        print("Item has been added.")

    # order list updated if item removed

    def remove(self, item, price, quantity=1):
        for menu_item in self.bill:
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] -= quantity
                if menu_item["quantity"] <= 0:
                    self.bill.remove(menu_item)

        print("Item has been removed.")

    # works out the total price of the table

    def get_subtotal(self):
        menu_total = 0
        for menu_item in self.bill:
            menu_total += menu_item["price"] * menu_item["quantity"]

        return round(menu_total, 2)

    # total bill after the surcharge included

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        total_service_charge = round((subtotal * service_charge), 2)
        total = subtotal + total_service_charge
        total_bill = {
            "Sub Total": f"£{subtotal:.2f}",
            "Service Charge": f"£{total_service_charge}",
            "Total": f"£{total}"
        }
        return total_bill

    # total bill split in equal amount for diners

    def split_bill(self):
        subtotal = self.get_subtotal()
        each_diner = subtotal / self.number_of_diners
        return each_diner
