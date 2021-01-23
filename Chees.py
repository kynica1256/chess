jsondata = {
"king": {"value":"@","horse-run":False,"motion":1,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,4],"spawn-location-user2":[6,4],},
"pawn": {"value":"I","horse-run":False,"motion":1,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[1,True],"spawn-location-user2":[5,True],},
"officer":{"value":"Y","horse-run":False,"motion":True,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[0,3,6],"spawn-location-user2":[6,3,6],},
"queen":{"value":"!","horse-run":False,"motion":True,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":True,"obliquely-right":True,"obliquely-top":True,"obliquely-bottom":True,"spawn-location-user1":[0,5],"spawn-location-user2":[6,5],},
"horse":{"value":"$","horse-run":True,"motion":False,"left":False,"right":False,"top":False,"bottom":False,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,2,7],"spawn-location-user2":[6,2,7],},
"boat":{"value":"%","horse-run":False,"motion":True,"left":True,"right":True,"top":True,"bottom":True,"obliquely-left":False,"obliquely-right":False,"obliquely-top":False,"obliquely-bottom":False,"spawn-location-user1":[0,1,8],"spawn-location-user2":[6,1,8],},
}

print("https://github.com/kynica1256/cheess/blob/main/Chees.py")

figures = ["boat","king","queen","officer","horse","pawn"]
a = []

user1 = {}
user2 = {}
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


def spawn(a, jsondata, figures, user1, user2):
    n = 0
    for i in figures:
        n += 1
        data = jsondata[i]["value"]
        data1 = jsondata[i]["spawn-location-user1"]
        data2 = jsondata[i]["spawn-location-user2"]
        figurdata = {}
        figurdata["id"] = n
        figurdata["status"] = True
        user1[i] = figurdata
        n += 1
        figurdata["id"] = n
        figurdata["status"] = True
        user2[i] = figurdata
        analiz(data1, a, data, data2)
for i in range(1,8):
    b = [str(i),0,0,0,0,0,0,0,0]
    a.append(b)
massive = []
massive.append(0)
for i in range(1,9):
    massive.append(str(i))
a.append(massive)
spawn(a, jsondata, figures, user1, user2)
text = ""
for i in a:
    for k in i:
        h = str(k)
        text += h
        text += " "
    text += "\n"
print(text)
