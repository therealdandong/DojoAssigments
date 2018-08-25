class bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo (self,):
        print "price are " + self.price + "max speed is " + self.max_speed + " your miles are " + str(self.miles)
    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    def reverse(self):
        if self.miles > 5:
            self.miles -= 5
        print "Reversing"
        return self
jay = bike("250 USD","100 MPH",15)
jay.ride().ride().ride().reverse().displayinfo()

john = bike("1500 USD","150 MPH",0)
john.ride().ride().reverse().reverse().displayinfo()

amy = bike("200 USD", "200 MPH", 10)
amy.reverse().reverse().reverse().displayinfo()