from math import ceil
class Table:
    def __init__(self, customers):
        self.bill = []
        self.customers = customers
        pass

    def order(self, item, price, quantity=1):
        x = False
        for dictionary in self.bill:
            if dictionary["item"] == item:
                dictionary["quantity"] += quantity
                x = True
        if x == False:
            bill_listing = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(bill_listing)
        #print(f"orders are {self.bill}")


    def remove(self, item, price, quantity=1):
        for dictionary in self.bill:
            if dictionary["item"] == item and dictionary["price"] == price and dictionary["quantity"] >= quantity:
                if dictionary["quantity"] - quantity == 0:
                    self.bill.remove(dictionary)
                else:
                    dictionary["quantity"] -= quantity
                return True
            return False

    def get_subtotal(self):
        subtotal = 0
        for dictionary in self.bill:
            quantity = dictionary["quantity"]
            cost_item = dictionary["price"]
            subtotal += quantity * cost_item
            #print(subtotal)
        return subtotal

    def get_total(self, service_charge_fraction = 0.1):
        subtotal = self.get_subtotal()
        service_charge = service_charge_fraction * subtotal
        total = subtotal + service_charge
        #subTotal_msg = f"Sub Total £{subtotal}, Service Charge {service_charge}, Total £{total}"
        return {"Sub Total": f"£{subtotal:.2f}", "Service Charge": f"£{service_charge:.2f}", "Total": f"£{total:.2f}"}

    def split_bill(self):
        #print(f"Total bill is {self.bill}")
        subtotal = self.get_subtotal()
        total_per_customer = subtotal/self.customers
        return ceil(total_per_customer*100)/100