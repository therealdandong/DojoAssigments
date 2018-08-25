class Car (object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
    def display_all(self):
        if self.price > 10000:
            self.tax =0.15
        print "your car price is {}, the speed is {}, fuel condition: {}, mileage:{}, tax:{} ".format(self.price,self.speed,self.fuel,self.mileage,self.tax)
car2 = Car(100,150,"empty", 250)
car2.display_all()

