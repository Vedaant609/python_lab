import random
def finder():
    t = []
    o = 0
    for i in range(20):
        u = random.randrange(1,100)
        t.append(u)
    print(t)
    b = int(input("enter the number"))
    for i in t:
        if b == i:
            print(t[o],o)
        o+=1
finder()    
