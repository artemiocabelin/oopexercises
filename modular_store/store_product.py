class Product(object):
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = []

    def add_prod(self,product):
        self.products.append(product)
        return self

    def remove_prod(self, product):
        for i,item in enumerate(self.products):
            if item == product:
                self.products.pop(i)
        return self

    def product_inventory(self):
        print ""
        print "Location: "+self.location
        print "Owned by: "+self.owner
        print "Our products include:"
        for item in self.products:
            print item


if __name__ =="__main__":
    a = Product('Los Angeles','Art')
    a.add_prod('Lock').add_prod('key').add_prod('door').product_inventory()
    a.remove_prod('Lock').product_inventory()