class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

        self.display_all()

    def display_all(self):
        print "Price: "+str(self.price)
        print "Speed: "+self.speed
        print "Fuel: "+self.fuel
        print "Mileage: "+self.mileage
        print "Tax: "+str(self.tax)
        return self


car1 = Car(2000,"35mph","Full","105mpg")
car2 = Car(3000,"5mph","Full","105mpg")
car3 = Car(4000,"15mph","Sort of Full","105mpg")
car4 = Car(5000,"25mph","Kind of Full","105mpg")
car5 = Car(6000,"45mph","Not Full","105mpg")
car6 = Car(7000,"35mph","Full","105mpg")

