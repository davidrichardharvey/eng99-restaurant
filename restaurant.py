class Table:
    bill = []
    def __init__(self,no_of_people):
        self.no_of_people = no_of_people

    def order(self,item,price,quantity=1):
        self.item = item
        self.price = price
        self.quantity = quantity
        promt_to_append = True
        temp_dic = {
            'item': self.item,
            'price': self.price,
            'quantity': self.quantity}
        for dic in self.bill:
            if self.item in dic.values():
                dic["quantity"]= dic["quantity"] + self.quantity
                promt_to_append = False
        if promt_to_append:
            self.bill.append(temp_dic)



# table1 = Table(4)
#  table1.bill.append(20)
#  table1.bill.append(30)
#  print(table1)
# table1.order("item",23,2)
# table1.order("item",23,2)
# table1.order("item",23,)
# print(table1.item)
# print(table1.price)
# print(table1.quantity)
# print(table1.bill)


