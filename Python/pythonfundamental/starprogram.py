"""
input is a list contain a series of number. and convert it into a cordinate number of star in the program.
"""


def star(list1):
    for i in range(len(list1)):
        if isinstance(list1[i], int) or isinstance(list1[i], float):
            result = ""
            for j in range(list1[i]):
                result += "*"
            print(result)
        elif isinstance(list1[i], str):
            result = ""
            for k in range(len(list1[i])):
                result += list1[i][0]
            print(result)


star([4, 6, 1, "apple", 3, "banana", 5, "orange", 7, 25])
