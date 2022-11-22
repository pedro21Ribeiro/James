#this is just a program not for realy coding but just for chilling. Enjoy (=
import time as t
import requests as req
import random as r


def james():
    print("Hi.")
    print(".")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print("Welcome to James. A chill program.")
    t.sleep(2)
    menu()
def menu():
    ui = input("What do you want to do today?\n1- Daily motivation 2- Harsh but true 3- exit"+ "\n")
    if ui == "1":
        Dm()
    elif ui == "2":
        Hbt()
    elif ui == "3":
        print("Good bye")
    else:
        print("This is not a vallid option")
        menu()
def Dm():
    t.sleep(2)
    result = req.get("https://zenquotes.io/api/random")
    clean_result = result.json()
    print(clean_result[0].get("q")+ "\n")
    t.sleep(2)
    menu()
def Hbt():
    hbtFile = open("hbt.txt")
    readed = hbtFile.read()
    splited = readed.split("\n")
    num = r.randrange(0, len(splited) - 1)
    print(splited[num]+"\n")
    menu()


james()
