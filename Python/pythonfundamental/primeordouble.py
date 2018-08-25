def deter():
    for numb in range(100,100001):
        if primedeter(numb):
            print("Foo")
        elif perfectdeter(numb):
            print("bar")
        else:
            print("FooBar")


def primedeter(numb):
    for i in range(2, numb):
        if numb % i == 0:
            return False

    return True


def perfectdeter(numb):
    for i in range(2, numb):
        if numb % i == i:
            return True
    return False

deter()