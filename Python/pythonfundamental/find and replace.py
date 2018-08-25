words = "It's thanksgiving day. It's my birthday,too!"

print(words.find("day"))
apple = words.replace("day","month",3)
print(apple)
print(words)

"""
min and max
"""

x = [2, 54, -2, 7, 12, 98]

mins = min(x)
maxs = max(x)
print(mins, maxs)

"""
first and last
"""
y = ["hello", 2, 54, -2, 7, 12, 98, "world"]
newlist = []
for i in y:
    if isinstance(i, str):
        newlist.append(i)
print(newlist)


"""
newlist
"""
z = [19, 2, 54,4, -2, 7, 12, 98, 32, 10, -3, 6]
z.sort()
print(z)
newlist3 = []
newlist2 = []
ul = []

newlist2 = z[:int(len(z)/2)]
newlist3 = z[int(len(z)/2):]

print(newlist2, newlist3)
newlist3.insert(0, newlist2)
print(newlist3)

















