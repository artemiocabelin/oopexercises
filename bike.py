class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        print self.miles
        return self

    def reverse(self):
        print "Reversing"
        if self.miles > 0:
            self.miles = self.miles - 5
        print self.miles
        return self

a = Bike(200, "25mph")
b = Bike(300, "15mph")
c = Bike(150, "50mph")

a.ride().ride().ride().reverse().displayInfo()
b.ride().ride().reverse().reverse().displayInfo()
c.reverse().reverse().reverse().displayInfo()