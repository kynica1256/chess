jsondata = {
"king": {"value":"@","horse-run":False,"motion":1,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,4],"spawn-location-user2":[6,5],},
"pawn": {"value":"I","horse-run":False,"motion":1,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[1,True],"spawn-location-user2":[5,True],},
"officer":{"value":"Y","horse-run":False,"motion":True,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[0,3,6],"spawn-location-user2":[6,3,6],},
"queen":{"value":"!","horse-run":False,"motion":True,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[0,5],"spawn-location-user2":[6,4],},
"horse":{"value":"$","horse-run":True,"motion":False,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,2,7],"spawn-location-user2":[6,2,7],},
"boat":{"value":"%","horse-run":False,"motion":True,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,1,8],"spawn-location-user2":[6,1,8],},
}
import json
import os

print("https://github.com/kynica1256/cheess/blob/main/Chees.py")

figures = ["boat","king","queen","officer","horse","pawn"]
figuresdataa = ["boat","boat","king","queen","officer","officer","horse","horse","pawn","pawn","pawn","pawn","pawn","pawn","pawn","pawn"]
a = []

user1 = {}
user2 = {}
def moving(a, jsondata, datamass, userdata, value, loc):
    print(value)
    if value == "@":
        for k, v in userdata.items():
            if value == userdata[k]["value"][0] and value == userdata[k]["location"][1]:
                if datamass[0] == userdata[k]["location"][0]+1 or datamass[0] == userdata[k]["location"][0]-1 or datamass[1] == userdata[k]["location"][1]+1 or datamass[1] == userdata[k]["location"][1]-1:
                    for i, b in userdata.items():
                        if datamass[0] == userdata[i]["location"][0] and datamass[1] == userdata[i]["location"][1]:
                            print("no")
                        else:
                            a[datamass[0]][datamass[1]] = 0
                            a[loc[0]][loc[1]] = value
    else:
        a[datamass[0]][datamass[1]] = 0
        for k, v in userdata.items():
            if datamass[0] == userdata[k]["location"][0] and datamass[1] == userdata[k]["location"][1]:
                userdata[k]["location"] = loc
        a[loc[0]][loc[1]] = value
def battle(a, userdata, enemydata, locuser, locenemy, who):
    for k, v in enemydata.items():
        if locenemy[0] == enemydata[k]["location"][0] and locenemy[1] == enemydata[k]["location"][1]:
            print(enemydata[k]["value"]+" - DEAD "+who)
            enemydata[k]["status"] = False
            enemydata[k]["location"] = False
    for k, v in userdata.items():
        if locuser[0] == userdata[k]["location"][0] and locuser[1] == userdata[k]["location"][1]:
            a[userdata[k]["location"][0]][userdata[k]["location"][1]] = 0
            userdata[k]["location"] = locenemy
            name = userdata[k]["value"]
            a[locenemy[0]][locenemy[1]] = name
def watchfig(spis, value):
    iu = []
    o = 1
    for k, v in spis.items():
        if value == spis[k]["value"]:
            if spis[k]["type"] == "pawn":
                checkdata = spis[k]["location"]
                checkdata[1] = o
                print(spis[k]["type"],spis[k]["value"],checkdata,end="\n")
                o += 1
            else:
                print(spis[k]["type"],spis[k]["value"],spis[k]["location"],end="\n")
        else:
            pass
def analiz(arg, a, val, data2):
    if arg[1] == True:
        for i in range(1, 9):
            a[arg[0]][i] = val
    else:
        if len(arg) > 2:
            a[arg[0]][arg[1]] = val
            a[arg[0]][arg[2]] = val
        else:
            a[arg[0]][arg[1]] = val
    if data2[1] == True:
        for i in range(1, 9):
            a[data2[0]][i] = val
    else:
        if len(data2) > 2:
            a[data2[0]][data2[1]] = val
            a[data2[0]][data2[2]] = val
        else:
            a[data2[0]][data2[1]] = val

def printfigur(a):
    text = ""
    for i in a:
        for k in i:
            h = str(k)
            text += h
            text += " "
        text += "\n"
    print(text)
def spawn(a, jsondata, figures, user1, user2):
    opo = 1
    n = 1
    res = {}
    res1 = {}
    for yu in figuresdataa:
        res[yu] = True
        res1[yu] = True
    for i in figures:
        data = jsondata[i]["value"]
        data1 = jsondata[i]["spawn-location-user1"]
        data2 = jsondata[i]["spawn-location-user2"]
        analiz(data1, a, data, data2)
    for u in figuresdataa:
        figurdata = {}
        figurdata["id"] = n
        figurdata["type"] = u
        figurdata["value"] = jsondata[u]["value"]
        figurdata["status"] = True
        if jsondata[u]["spawn-location-user1"][1] == True:
            figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], opo]
            opo += 1
        if len(jsondata[u]["spawn-location-user1"]) == 3:
            if res[u] == True:
                figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], jsondata[u]["spawn-location-user1"][2]]
                res[u] = False
            else:
                figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], jsondata[u]["spawn-location-user1"][1]]
        if len(jsondata[u]["spawn-location-user1"]) == 2:
            figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], jsondata[u]["spawn-location-user1"][1]]
        user1[n] = figurdata
        n += 1
        opo1 = 1
        figurdata1 = {}
        figurdata1["id"] = n
        figurdata1["type"] = u
        figurdata1["status"] = True
        figurdata1["value"] = jsondata[u]["value"]
        figurdata1["location"] = 1
        if jsondata[u]["spawn-location-user2"][1] == True:
            figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], opo]
            opo1 += 1
        if len(jsondata[u]["spawn-location-user2"]) == 3:
            if res1[u] == True:
                figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], jsondata[u]["spawn-location-user2"][2]]
                res1[u] = False
            else:
                figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], jsondata[u]["spawn-location-user2"][1]]
        if len(jsondata[u]["spawn-location-user2"]) == 2:
            figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], jsondata[u]["spawn-location-user2"][1]]
        user2[n] = figurdata1
        n += 1
for i in range(7):
    b = [str(i),0,0,0,0,0,0,0,0]
    a.append(b)
massive = []
massive.append(0)
for i in range(1,9):
    massive.append(str(i))
a.append(massive)
spawn(a, jsondata, figures, user1, user2)
printfigur(a)
while True:
    user1fig = input("User1: ")
    watchfig(user1, user1fig)
    user1fig1 = input("Enter the coordinates of the shape: ").split()
    user1figmove = input("Coordinat: ").split()
    usermove1 = [int(x) for x in user1figmove]
    user1list = [int(x) for x in user1fig1]
    moving(a, jsondata, user1list, user1, user1fig, usermove1)
    printfigur(a)
    user1battle = input("Figure Coordinat: ").split()
    user1batttledata = [int(x) for x in user1battle]
    battle(a, user1, user2, usermove1, user1batttledata, "User2")
    printfigur(a)
    user2fig = input("User2: ")
    watchfig(user2, user2fig)
    user2fig1 = input("Enter the coordinates of the shape: ").split()
    user2figmove = input("Coordinat: ").split()
    usermove2 = [int(x) for x in user2figmove]
    user2list = [int(x) for x in user2fig1]
    moving(a, jsondata, user2list, user2, user2fig, usermove2)
    printfigur(a)
    user2battle = input("Figure Coordinat: ").split()
    user2batttledata = [int(x) for x in user1battle]
    battle(a, user2, user1, usermove2, user2batttledata, "User1")
    printfigur(a)


























'''

jsondata = {
"king": {"value":"@","horse-run":False,"motion":1,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,4],"spawn-location-user2":[6,5],},
"pawn": {"value":"I","horse-run":False,"motion":1,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[1,True],"spawn-location-user2":[5,True],},
"officer":{"value":"Y","horse-run":False,"motion":True,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[0,3,6],"spawn-location-user2":[6,3,6],},
"queen":{"value":"!","horse-run":False,"motion":True,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[0,5],"spawn-location-user2":[6,4],},
"horse":{"value":"$","horse-run":True,"motion":False,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,2,7],"spawn-location-user2":[6,2,7],},
"boat":{"value":"%","horse-run":False,"motion":True,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,1,8],"spawn-location-user2":[6,1,8],},
}
import json
import os

print("https://github.com/kynica1256/cheess/blob/main/Chees.py")

figures = ["boat","king","queen","officer","horse","pawn"]
figuresdataa = ["boat","boat","king","queen","officer","officer","horse","horse","pawn","pawn","pawn","pawn","pawn","pawn","pawn","pawn"]
a = []

user1 = {}
user2 = {}
def moving(a, jsondata, datamass, userdata, value, loc):
    pol = a[datamass[0]][datamass[1]]
    a[datamass[0]][datamass[1]] = 0
    for k, v in userdata.items():
        if datamass[0] == userdata[k]["location"][0] and datamass[1] == userdata[k]["location"][1]:
            userdata[k]["location"] = loc
    a[loc[0]][loc[1]] = value
def battle(a, userdata, enemydata, locuser, locenemy, who):
    for k, v in enemydata.items():
        if locenemy[0] == enemydata[k]["location"][0] and locenemy[1] == enemydata[k]["location"][1]:
            print(enemydata[k]["value"]+" - DEAD "+who)
            enemydata[k]["status"] = False
            enemydata[k]["location"] = False
    for k, v in userdata.items():
        if locuser[0] == userdata[k]["location"][0] and locuser[1] == userdata[k]["location"][1]:
            a[userdata[k]["location"][0]][userdata[k]["location"][1]] = 0
            userdata[k]["location"] = locenemy
            name = userdata[k]["value"]
            a[locenemy[0]][locenemy[1]] = name
def watchfig(spis, value):
    iu = []
    o = 1
    for k, v in spis.items():
        if value == spis[k]["value"]:
            if spis[k]["type"] == "pawn":
                checkdata = spis[k]["location"]
                checkdata[1] = o
                print(spis[k]["type"],spis[k]["value"],checkdata,end="\n")
                o += 1
            else:
                print(spis[k]["type"],spis[k]["value"],spis[k]["location"],end="\n")
        else:
            pass
def analiz(arg, a, val, data2):
    if arg[1] == True:
        for i in range(1, 9):
            a[arg[0]][i] = val
    else:
        if len(arg) > 2:
            a[arg[0]][arg[1]] = val
            a[arg[0]][arg[2]] = val
        else:
            a[arg[0]][arg[1]] = val
    if data2[1] == True:
        for i in range(1, 9):
            a[data2[0]][i] = val
    else:
        if len(data2) > 2:
            a[data2[0]][data2[1]] = val
            a[data2[0]][data2[2]] = val
        else:
            a[data2[0]][data2[1]] = val

def printfigur(a):
    text = ""
    for i in a:
        for k in i:
            h = str(k)
            text += h
            text += " "
        text += "\n"
    print(text)
def spawn(a, jsondata, figures, user1, user2):
    opo = 1
    n = 1
    res = {}
    res1 = {}
    for yu in figuresdataa:
        res[yu] = True
        res1[yu] = True
    for i in figures:
        data = jsondata[i]["value"]
        data1 = jsondata[i]["spawn-location-user1"]
        data2 = jsondata[i]["spawn-location-user2"]
        analiz(data1, a, data, data2)
    for u in figuresdataa:
        figurdata = {}
        figurdata["id"] = n
        figurdata["type"] = u
        figurdata["value"] = jsondata[u]["value"]
        figurdata["status"] = True
        if jsondata[u]["spawn-location-user1"][1] == True:
            figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], opo]
            opo += 1
        if len(jsondata[u]["spawn-location-user1"]) == 3:
            if res[u] == True:
                figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], jsondata[u]["spawn-location-user1"][2]]
                res[u] = False
            else:
                figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], jsondata[u]["spawn-location-user1"][1]]
        if len(jsondata[u]["spawn-location-user1"]) == 2:
            figurdata["location"] = [jsondata[u]["spawn-location-user1"][0], jsondata[u]["spawn-location-user1"][1]]
        user1[n] = figurdata
        n += 1
        opo1 = 1
        figurdata1 = {}
        figurdata1["id"] = n
        figurdata1["type"] = u
        figurdata1["status"] = True
        figurdata1["value"] = jsondata[u]["value"]
        figurdata1["location"] = 1
        if jsondata[u]["spawn-location-user2"][1] == True:
            figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], opo]
            opo1 += 1
        if len(jsondata[u]["spawn-location-user2"]) == 3:
            if res1[u] == True:
                figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], jsondata[u]["spawn-location-user2"][2]]
                res1[u] = False
            else:
                figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], jsondata[u]["spawn-location-user2"][1]]
        if len(jsondata[u]["spawn-location-user2"]) == 2:
            figurdata1["location"] = [jsondata[u]["spawn-location-user2"][0], jsondata[u]["spawn-location-user2"][1]]
        user2[n] = figurdata1
        n += 1
for i in range(7):
    b = [str(i),0,0,0,0,0,0,0,0]
    a.append(b)
massive = []
massive.append(0)
for i in range(1,9):
    massive.append(str(i))
a.append(massive)
spawn(a, jsondata, figures, user1, user2)
printfigur(a)
while True:
    user1fig = input("User1: ")
    watchfig(user1, user1fig)
    user1fig1 = input("Enter the coordinates of the shape: ").split()
    user1figmove = input("Coordinat: ").split()
    usermove1 = [int(x) for x in user1figmove]
    user1list = [int(x) for x in user1fig1]
    moving(a, jsondata, user1list, user1, user1fig, usermove1)
    printfigur(a)
    user1battle = input("Figure Coordinat: ").split()
    user1batttledata = [int(x) for x in user1battle]
    battle(a, user1, user2, usermove1, user1batttledata, "User2")
    printfigur(a)
    user2fig = input("User2: ")
    watchfig(user2, user2fig)
    user2fig1 = input("Enter the coordinates of the shape: ").split()
    user2figmove = input("Coordinat: ").split()
    usermove2 = [int(x) for x in user2figmove]
    user2list = [int(x) for x in user2fig1]
    moving(a, jsondata, user2list, user2, user2fig, usermove2)
    printfigur(a)
    user2battle = input("Figure Coordinat: ").split()
    user2batttledata = [int(x) for x in user1battle]
    battle(a, user2, user1, usermove2, user2batttledata, "User1")
    printfigur(a)
'''
