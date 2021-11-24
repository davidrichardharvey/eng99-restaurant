class Table:
    def __init__(self, num_people):
        self.num_people = num_people
        self.bill =[]

    def order(self, item, price, qty = 1):
        for x in self.bill:
            if x["item"] == item and x["price"] == price:
                print(x["item"])
                x["quantity"] = x.get("quantity")+qty
                print(x["quantity"])
                return None
        self.bill.append({"item": item, "price": price, "quantity": qty})

    def remove(self, item, price, qty = 1):
        for x in self.bill:
            if x["item"] == item and x["price"] == price:
                print(x["item"])
                x["quantity"] = x.get("quantity") - qty
                if x["quantity"] <=0:
                    self.bill.remove(x)


    def get_subtotal(self):
        '''
        - A `get_subtotal` method that returns the total cost for the table based on the prices and quantities in the bill.

        :return:
        '''
        pass

    def get_total(self):
        '''
        - A `get_total` method that accepts a service charge percentage in the form of a decimal.  If no service charge percentage is provided,
         it should default to 10% (i.e. `0.10`).  This method should return a dictionary with the following
         keys: `Sub Total`, `Service Charge`, `Total`.  The values should be string representations of the corresponding prices
          in British pounds and pence.  e.g. `{"Sub Total": "£120.00", "Service Charge": "£12.00", "Total": "£132.00"}`

        :return:
        '''
        pass

    def split_bill(self):
        '''
        - A `split_bill` method, which returns the the subtotal cost of the bill divided by the number of diners as a float rounded up
        to the nearest penny.

        :return:
        '''
        pass


