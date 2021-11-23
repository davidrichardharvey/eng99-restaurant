class Table:
    def __init__(self, people):
        self.people = people
        self.bill = {
            "item": "",
            "price": 0.00,
            "quantity": 1
        }

    def order(self, item: str, price: float, quantity=1):#Create a bill
        self.bill = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        return self.bill

    def remove(self, item, price, quantity): #modify bill to decrease quantity
        if self.bill.get("item") == item and self.bill.get("price") == price and self.bill.get("quantity") > 0:
            old_quantity = self.bill.get("quantity")
            new_quantity = old_quantity - quantity
            self.bill.update({"quantity": new_quantity})
            return self.bill
        else:
            return False

    def get_subtotal(self): # total the price of a table
        price_of_item = self.bill.get("price")
        quantity_of_item = self.bill.get("quantity")
        sub_total = price_of_item * quantity_of_item
        return sub_total
        #print(price_of_item)
        #print(quantity_of_item)


    #def get_total(self): #subtotal plus service charge

    #def split_bill(self): #divide the bill between all the people at the table

table02 = Table(2)
print(table02.order("Food", 10.00, 3))
print(table02.remove("Food", 10.00, 1))
print(table02.get_subtotal())

