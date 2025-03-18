def counter(a):
    u= 0
    l=0
    for i in a:
        if i.isupper() == True:
            u+=1
        elif i.islower() == True:
            l+=1
    d = {}
    d["upper"] = u
    d["lower"] = l
    return(d)
x = input("enter")
w = counter(x)
print(w)
