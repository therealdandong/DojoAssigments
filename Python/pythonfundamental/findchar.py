def findchar (char,list):
    newlist =[]
    for i in list:
        for chars in i:
            if chars == char:
                newlist.append(i)
    return set(newlist)


a = ["apple","banana","yourmom","canigetyourmoney","iscanigetyounaked"]
print(findchar("o", a))