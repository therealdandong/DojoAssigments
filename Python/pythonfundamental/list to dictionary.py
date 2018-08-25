name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "apple", "banana"]


def make_dict(list1, list2):

    new_dict = {}
    for i in range(len(name)):
        new_dict[list1[i]] = list2[i]
    return new_dict





"""
hacker challenge if one list is longer, the longer list should be used as key.
"""


def make_dict2(list1, list2):

    new_dict = {}
    if len(list1) >= len(list2):
        for i in range(len(name)):
            new_dict[list1[i]] = list2[i]
        return new_dict
    else:
        for i in range(len(name)):
            new_dict[list2[i]] = list1[i]
        return new_dict


print(make_dict2(name, favorite_animal))