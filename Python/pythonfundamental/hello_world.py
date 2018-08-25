

mylist = [1, 3, 5, 7, 9]
apple = mylist[1:3]


def listfunc (list):
    for i in range(len(list)):
        if i:
            list[i] = list[i] + i
    return list


print(listfunc(mylist))
