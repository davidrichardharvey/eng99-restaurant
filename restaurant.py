class Table:

    def __init__(self, number_of_customers):
        self.bill = []
        self._customers = number_of_customers

    def order(self, item: str, price: float, quantity=1) -> None:
        for order in self.bill:
            if order["item"] == item:
                order["quantity"] += quantity
                return
        self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item: str, price: float, quantity=1) -> None:
        for order in self.bill:
            if order["item"] == item:
                order["quantity"] -= quantity
                if order["quantity"] <= 0:
                    self.bill.remove(order)
                return
        print("Item has not been ordered")

    def get_subtotal(self) -> float:
        subtotal = 0
        for item in self.bill:
            price = item["price"]
            quantity = item["quantity"]
            subtotal += price * quantity

        return round(subtotal, 2)

    def get_total(self, service_charge: float) -> float:
        subtotal = self.get_subtotal()
        service_charge_amount = subtotal * service_charge
        total = subtotal * (1 + service_charge)
        bill_summary = {
            "Service Charge": f"£{service_charge_amount:.2f}",
            "Sub Total": f"£{subtotal:.2f}",
            "Total": f"£{total:.2f}"
        }
        return bill_summary

    def split_bill(self) -> float:
        subtotal = self.get_subtotal()
        equal_split = subtotal / self._customers
        return round(equal_split, 2)
