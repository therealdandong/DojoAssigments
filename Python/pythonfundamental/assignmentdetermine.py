"""
a program take one list contain the mixed type of element or, single type of element. and is up to me to determine what
 kind of element to choice from. and concatenate together.
"""


def detect(data):
    string = ""
    numb = 0
    newlist = []
    truthstr = 0
    truthnumb = 0
    truthlist = 0
    for i in range(len(data)):
        if isinstance(data[i], str):
            string += data[i]
            truthstr += 1
        elif isinstance(data[i], int) or isinstance(data[i], float):
            numb += data[i]
            truthnumb += 1
        elif isinstance(data[i], list):
            newlist += data[i]
            truthlist += 1

    if truthnumb != 0 and truthlist != 0 or truthnumb != 0 and truthstr != 0 or truthlist != 0 and truthstr != 0:
        print(" this is a mixed type \n string: {0} \n sum: {1} \n list: {2}".format(string, numb, newlist))
    elif truthstr == 0:
        print("this is a integer type \n sum: {}".format(numb))
    elif truthnumb == 0:
        print("this is a string type \n string:", string)


lj = ['magical unicorns', 19, 'hello', 98.98, 'world']
detect(lj)
detect([2, 3, 1, 7, 4, 12])
detect(["apple", "banana", "orange", "oj"])