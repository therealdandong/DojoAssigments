

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def converttotup(dicts):
    keys = list(dicts.keys())
    values = list(dicts.values())
    newlist = []
    for i in range(len(dicts)):
        newlist.append((keys[i], values[i]))
    return newlist


print(converttotup(my_dict))
