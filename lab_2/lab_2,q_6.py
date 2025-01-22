def counter(a):
    t = 0
    while a%10 != 0:
        u = a%10
        a = (a-u)/10
        t+=1
    return t
y = int(input("enter the number"))
d = counter(y)
print(d)
        
