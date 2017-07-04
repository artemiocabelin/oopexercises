class Product(object):
    def __init__(self,price,item_name,weight,brand,cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self,tax):
        self.price = (self.price * tax) + self.price
        return self

    def return_product(self,reason):
        if reason == "Defective":
            self.status = "Defective"
            self.price = 0
        elif reason == "Box,New":
            self.status = "For Sale"
        elif reason == "Box,Open":
            self.status = "Used"
            self.price = (self.price * .2) + self.price
        return self

    def displayInfo(self):
        print "Price: "+str(self.price)
        print "Name: "+self.item_name
        print "Weight: "+self.weight
        print "Brand: "+self.brand
        print "Cost: "+str(self.cost)
        print "Status: "+self.status

a = Product(1000,"Thing","1kg","Jordan",20)


a.displayInfo()