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


    def get_subtotal(self):
        menu_total = 0
        for menu_item in self.bill:
            total += menu_item["price"] * menu_item["quantity"]
            return round(menu_total, 2)


    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        total_service_charge = round((subtotal * service_charge), 2)
        total = subtotal + total_service_charge
        total_bill = {
            "Sub Total": subtotal,
            "Service Charge": total_service_charge,
            "Total": total
        }
        return total_bill


    def split_bill(self, num_of_diners):
        subtotal = self.get_subtotal()
        each_diner = subtotal / num_of_diners
        return each_diner
