#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the lists of words you want to choose from.
entrees = ["calzone","tortilla espanyola","ham and cheese sandwich", "lasagna"]
sides = ["chicken noodle soup","macaroni and cheese", 'croquetas', 'banana', 'mashed potatos']
desserts = ["gelato","cheesecake", 'candy', 'brownies', 'licorice']
print("Welcome to Katie's cafe!")

for a in range(3):
    if a = 1:
        item = "entrees"
    elif a = 2:
        item = "sides"
    elif a = 3:
        item = "deserts"
    print("""
Here are your options for""", item)
    for i in range(3):
        aRandomIndex = randint(0, len(item)-1)
        print(item[aRandomIndex])
