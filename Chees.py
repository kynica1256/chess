king = {
    "value":"@",
    "motion":1,
    "left":True,
    "right":True,
    "top":True,
    "bottom":True,
    "obliquely-left":False,
    "obliquely-right":False,
    "obliquely-top":False,
    "obliquely-bottom":False
}
pawn = {
    "value":"I",
    "motion":1,
    "left":False,
    "right":False,
    "top":False,
    "bottom":False,
    "obliquely-left":True,
    "obliquely-right":True,
    "obliquely-top":True,
    "obliquely-bottom":True
}



a = []

users = {
    "pawns":8,
    "king":1,
}
def process(users):
    print("work")
for i in range(8):
    b = [str(i)+".",0,0,0,0,0,0,0,0]
    a.append(b)
for i in a:
    print(i)
