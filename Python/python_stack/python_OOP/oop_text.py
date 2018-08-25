class users(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = True
    def login (self):
        print self.name + "welcome you are login in now."
        self.logged = True
        return self
    def logout (self):
        print self.name + "sorry to see you go, be back next time"
        self.logged =True
        return self
    def show (self):
        print "it is your name :"+ self.name + "and your email: " + self.email
        return self


dan = users("dan","dan@gmail.com")
print dan.login().logout().show()