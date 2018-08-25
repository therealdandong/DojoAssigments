

def deterul (data):
    if isinstance(data,int):
        if data >= 100:
            print("Tha's a big number!")
        elif data < 100:
            print("That's a small number!")
    if isinstance(data,str):
        if len(data) >= 50:
            print("long sentences")
        if len(data) < 50:
            print("short sentences")
    if isinstance(data,list):
        if len(data) >= 10:
            print("long list")
        if len(data) < 10:
            print("short list")
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

deterul(sI)
deterul(mI)
deterul(bI)
deterul(eI)
deterul(spI)
deterul(sS)
deterul(mS)
deterul(bS)
deterul(eS)
deterul(aL)
deterul(mL)
deterul(lL)
deterul(eL)
deterul(spL)



