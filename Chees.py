
'''

for i in range(1,1001):
    x=i
    L=0
    M=0
    while x > 0 :
        L = L + 1
        if x % 2 == 1 :
            M=M + x % 10
        x=x // 10
   if L=3 and M=8:
       print(i)
       break


a = [0,5,7]

def math(a):
    print(max(a))

math(a)


while True:
    u = int(input())
    if u % 4 == 0:
        print("This is year leap")
    else:
        print("no")
'''
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
