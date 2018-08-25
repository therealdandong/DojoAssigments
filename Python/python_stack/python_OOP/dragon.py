class Animal(object):
    def __init__(self, name, bad_ass):
        self.name = name
        self.health = 100
        self.bad_ass = bad_ass

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display(self):
        print "i am {}, and my health is {}".format(self.name,self.health)
        return self


class Dog(Animal):
    def __init__(self, dog_name):
        super(Dog, self).__init__(dog_name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, dragon_name, extras):
        super(Dragon, self).__init__(dragon_name, extras)
        self.health = 170

    def fly(self):
        self.health -= 10

    def display(self):
        print "i am the dragon, my name is {}, also {}".format(self.name, self.bad_ass)

"""
dog2 = Dog("jimmy")
dog2.display()

dragon3 = Dragon("apple")
dragon3.display()

"""
dan = Animal("human","purebadass")
dan.display()

dan.display()
dragon3 = Dragon("apple","badassboy")
dragon3.display()