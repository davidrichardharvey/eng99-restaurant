class Table:

    def __init__(self, number_of_diners):
        self.bill = []
        self.people = number_of_diners


    def order(self, item: str, price: float, quantity=1):
        return self.bill.append({"item" : item, "price": price, "quantity": quantity})



    def remove(self, item, price, quantity=1):
        for i in self.bill:
            if i["item"] == item and i["price"] == price:
                i["quantity"] = i.get("quantity") - quantity
                return i["quantity"]
                if i["qauntity"] == False:
                    dict.clear(i)

    def get_subtotal(self):
        subtotal = 0

        for i in self.bill:
            subtotal += i["price"] * i["quantity"]
        return round(subtotal, 2)

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        service_charge1 = subtotal * service_charge
        total = service_charge1 + subtotal
        return {
            "Sub Total": f"£{subtotal:.2f}",
            "Service Charge": f"£{service_charge1}",
            "Total": f"£{total}"
        }

    def split_bill(self):
        subtotal = self.get_subtotal()
        return round(subtotal / self.people, 2)


