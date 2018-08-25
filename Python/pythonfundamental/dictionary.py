

personal_info ={
    "name": "james alex john the second",
    "age": 25,
    "hobby": ["basketball", "pickup girl", "day dream about become a billionaire"],
    "location": "somewhere deep in the ocean"
}


def getuser_info():
    print("your name is: ", personal_info["name"])
    print("your age is:", personal_info["age"])
    print("your hobby is: ", personal_info["hobby"])
    print("your location is: ", personal_info["location"])


getuser_info()