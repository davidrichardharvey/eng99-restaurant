from math import ceil


class Table:
    def __init__(self, customers):
        self.bill = []
        self.customers = customers
        pass

    def order(self, item, price, quantity=1):
        '''
        Adds the menu order to the bill
        :param item: menu item
        :param price: Price, float gbp
        :param quantity: quantity order of the specified menu item
        :return: n/a
        '''
        new_item = False
        # Checks if item already exists on bill, if so increase the quanitiy of it on bill
        for dictionary in self.bill:
            if dictionary["item"] == item:
                dictionary["quantity"] += quantity
                new_item = True
        # If item isn't on the bill, adds it to the bill
        if new_item == False:
            bill_listing = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(bill_listing)

    def remove(self, item, price, quantity=1):
        '''
        Removes a currently existing menu order
        by reducing the quantity, if quantity becomes 0, removes menu item
        :param item: menu order
        :param price: Price, float gbp
        :param quantity: quantity order of the specified menu item
        :return: Returns true, if order is removed/ quantity reduced, otherwise returns false
        '''
        for dictionary in self.bill:
            # if menu item exists, attempt to reduce quantity
            # if that results in 0 for the quantity, remove order completely
            if dictionary["item"] == item and dictionary["price"] == price and dictionary["quantity"] >= quantity:
                if dictionary["quantity"] - quantity == 0:
                    self.bill.remove(dictionary)
                else:
                    dictionary["quantity"] -= quantity
                return True
            return False

    def get_subtotal(self):
        '''
        Gets the subtotal for the order, i.e. cost before service charge
        :return:
        '''
        subtotal = 0
        for dictionary in self.bill:
            quantity = dictionary["quantity"]
            cost_item = dictionary["price"]
            subtotal += quantity * cost_item
        return subtotal

    def get_total(self, service_charge_fraction=0.1):
        '''
        :param service_charge_fraction: fraction for the service charge, defaults to 10% if not defined
        :return: dictionary of the subtotal, total and service charge
        '''
        subtotal = self.get_subtotal()
        service_charge = service_charge_fraction * subtotal
        total = subtotal + service_charge
        # example return {"Sub Total": "£120.00", "Service Charge": "£12.00", "Total": "£132.00"}
        return {"Sub Total": f"£{subtotal:.2f}", "Service Charge": f"£{service_charge:.2f}", "Total": f"£{total:.2f}"}

    def split_bill(self):
        '''
        :return: returns the subtotal per person on the table, rounded to the nearest penny
        '''
        subtotal = self.get_subtotal()
        subtotal_per_customer = subtotal / self.customers
        return ceil(subtotal_per_customer * 100) / 100
