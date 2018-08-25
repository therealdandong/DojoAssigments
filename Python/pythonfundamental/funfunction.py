"""
even/odd
"""


def evenodd():
    i = 0
    while i < 1001:
        if i % 2 == 0:
            print("is even")
        elif i % 2 == 1:
            print("is odd")
        i += 1
evenodd()


"""
multiply
"""


def multiply(list,num):

    newlist = []
    i = 0
    while i < len(list)-1:
        newlist.append(num * list[i])
        i += 1
    return newlist


apple = [1, 3, 5, 7, 15, 16, 8]
print(multiply(apple, 7))

"""
hacker challenge
"""


def hacker(list1):

    for i in range(len(list1)):
        newlist = []
        for nums in range(list1[i]):
            newlist.append(1)
        list1[i] = newlist
    return list1


print(hacker(multiply(apple, 2)))