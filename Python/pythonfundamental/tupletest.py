def test():
    my_tuple = (1, 3, 5, 7, 9)
    sum1 = 0
    for i in range(len(my_tuple)):
        if my_tuple[i] > 5:
            sum1 += my_tuple[i]
        if sum1 > 0:
            my_tuple[i] =i

    return sum1


print(test())