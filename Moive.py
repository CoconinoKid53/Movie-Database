import firebase_admin
import datetime
import re
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate("Database.json")

app = firebase_admin.initialize_app(cred)

db = firestore.client()


class MovieTitles:
    x = datetime.datetime(1999, 5, 30)
    print(x)
    print(x.strftime("%B"))
    print(x.strftime("%H"))
    print(x.strftime("%I"))
    print(x.strftime("%p"))

    movieList = ["Armageddon","BattleShip","Distrubia","Its a Wonderful Life"]

    
    movieList.remove("Armageddon")
    
    print(movieList)


    thisdict1 = {
    "rating" :"pg-13", 
    "year" : 1999, 
    "User" : 5
    }
    thisdict1.clear()
    print(thisdict1)

    thisdict2 = {"rating" : "pg-13",
     "year" : 2012, 
     "user" : 5,
     "critictsComments" :"One Stellar movie worth watching",
     "runtime" : "2hr 11min"
    }
    thisdict2["MemorableSong"] = "Thunderstruck"
    print(thisdict2)



    thisdict3 = {"rating" : "pg-13",
    "year" : 2007,
    "user" : 3,
    "memorablesong" : "One man wrekcing Machine"
    }
    print(thisdict3)

    thisdict4 = {
        "rating" : "pg-13",
        "year" : "1946",
        "memorable song" : "Buffalo Gal wont you come out Tonight",
        "runtime" : "2hr 9min"
    }
    thisdict4.update({"rating" : "pg"})
    print(thisdict4)

a = "Armageddon is in the dictonary"
b = "Armageddon is not in the dictonary"

if a < b :
    print("Armageddon is  not in the dictonary")
else:
    print("Armageddon is is in the dictonary")


txt = "One man Wrecking Machine"
x = re.search("Distrubia", txt)
print(x)


CandyList = ["Cookie dough bites", "M&Ms", "Starbursts", "Red Vines"]
BestCandyList = [True, False, True, False]

list3 = CandyList + BestCandyList
print(list3)

txt = "I Love to code"[::-1]
print(txt)

mytuple = ("Pepsi","Cherry Coke", "Dr Pepper")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

a = "pepsi"
b = "CherryCoke"

if a > b:
    print("a is greater than b pepsi tastes better than cherry coke")
else:
    print("b is not greater than a than Cherry coke tastes better than pepsi")

thisset = {"best actor: Bruce Willis", "Best Soundtrack 1999: Armageddon", "Best Visual Effects: John Fraizer"}
print(thisset)

thisset2 = {"Teen choice award best thriller movie 07: Distrubia", "Globe award best Director 1947, Frank Capra"}
print(thisset2)

thistuple = {"Action", "Thriller", "Drama"}
print(thistuple)

thistuple2 = { "No Sequles:" "BattleShip", "Armageddon", "Its a Wonderful Life" }
print(thistuple2)


