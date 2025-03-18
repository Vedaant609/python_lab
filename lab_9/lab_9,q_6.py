def giver(x):
    t = []
    for i in range(1,x+1):
        r = (i,i**2,i**3)
        t.append(r)
    t = tuple(t)
    return t

a = int(input("enter the ending"))
b = giver(a)
print(b)
