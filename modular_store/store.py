class Store(object):

    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        for i,item in enumerate(self.products):
            if item == product:
                self.products.pop(i)
        return self

    def inventory(self):
        print ""
        print "Location: "+self.location
        print "Owned by: "+self.owner
        print "Our products include:"
        for item in self.products:
            print item
        
        print "Have a nice day!"

# test cases
if __name__ =="__main__":
    a = Store('Los Angeles','Art')
    a.add_product('Lotion').add_product('Soap').add_product('Chair').inventory()
    a.remove_product('Lotion').inventory()
