class Table:

    def __init__(self,no_of_people):
        self.no_of_people = no_of_people
        self.bill = []

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

    def remove(self,item,price,quantity=1):
        self.item = item
        self.price = price
        self.quantity = quantity
        for dic in self.bill:
            if self.item in dic.values() and dic["quantity"] >= self.quantity:
                dic["quantity"] = (dic["quantity"] - self.quantity)
        for dic in self.bill:
            if self.item in dic.values() and dic["quantity"] == 0:
                self.bill.remove(dic)
    def get_subtotal(self):
        self.sub_total = 0
        for dict in self.bill:
            self.sub_total += dict["price"] * dict["quantity"]
        return self.sub_total
    def get_total(self,service_charge):
        self.sub_total = self.get_subtotal()
        self.total = self.sub_total + (self.sub_total * service_charge)
        serv_charge = self.sub_total * service_charge
        return {"Sub Total":"£"+str("{:.2f}".format(self.sub_total)),"Service Charge": "£"+str(serv_charge),"Total":"£"+str(self.total)}
    def split_bill(self):
        return round((self.get_subtotal() / self.no_of_people),2)






# table1 = Table(4)
# #  table1.bill.append(20)
# #  table1.bill.append(30)
# #  print(table1)
# table1.order("item",23,2)
# table1.order("item",23,2)
# table1.order("item",23,)
# table1.order("item1",23,3)
# table1.order("item2",23,3)
#
#
# print(table1.item)
# print(table1.price)
# print(table1.quantity)
# print(table1.bill)
# table1.remove("item",23,)
# print(table1.bill)


