class Product(object):
    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self):
        self.price = self.price * 1.13
        return self
    def return_reason(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "return in box":
            self.status = "used"
            self.price *= 0.8
    def display_info(self):
        print "your item is {}, price is {}, weight is {}, brand is {}, is {}".format(self.price,self.item_name, self.weight, self.brand, self.status)

