class Table:
    def __init__(self, num_people):
        self.num_people = num_people
        self.bill =[]


    def order(self, item, price, qty = 1):
        for menu_item in self.bill:
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] = menu_item.get("quantity") + qty
                return None
        self.bill.append({"item": item, "price": price, "quantity": qty})

    def remove(self, item, price, qty = 1):
        for menu_item in self.bill:
            if menu_item["item"] == item and menu_item["price"] == price:
                menu_item["quantity"] = menu_item.get("quantity") - qty
                if menu_item["quantity"] <=0:
                    self.bill.remove(menu_item)


    def get_subtotal(self):
        total = 0.00
        for item in self.bill:
            total += item["price"] * item["quantity"]
        return round(total,2)

    def get_total(self, service_charge_percentage:float):
        subtotal = self.get_subtotal()
        ser_charge = round(subtotal * service_charge_percentage,2)
        total = subtotal + ser_charge
        total_bill ={"Sub Total": f"£{subtotal:.2f}","Service Charge": f"£{ser_charge:.2f}","Total":f"£{total:.2f}"} # :.2f puts the float to 2dp
        return total_bill

    def split_bill(self):
        subtotal = self.get_subtotal()
        per_person = round(subtotal/self.num_people,2)
        return per_person


