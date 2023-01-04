#this is just a program not for realy coding but just for chilling. Enjoy (=
#importing repositories

import time as t
import requests as req
import random as r

#initialization of the program
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

#main menu function can scale
def menu():
    ui = input("What do you want to do today?\n1- Daily motivation 2- exit"+ "\n")
    if ui == "1":
        Dm()
    elif ui == "2":
        print("Good bye")
    else:
        print("This is not a vallid option")
        menu()
#daily motivation functionc uses a api to get a quote then cleans the response gettin only the quote
def Dm():
    t.sleep(2)
    result = req.get("https://zenquotes.io/api/random")
    clean_result = result.json()
    print(clean_result[0].get("q")+ "\n")
    t.sleep(2)
    menu()


james()
