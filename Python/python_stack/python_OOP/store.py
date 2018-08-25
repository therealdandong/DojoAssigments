class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        for staff in self.products:
            if staff == product:
                self.products.remove(staff)

    def inventory(self):
        for staff in self.products:
            print "product: {}".format(staff)
        print "\n"


apple_store = Store("NYC","jason")

apple_store.add_product("green_apple")
apple_store.add_product("blue_apple")

apple_store.inventory()

apple_store.remove_product("green_apple")


apple_store.inventory()