def counter(x):
    a = 0
    n = 0
    for i in x:
        if i.isalpha()== True:
            a+=1
        elif i.isdigit() == True:
            n+=1
    d = {}
    d["alpha"]=a
    d["num"] = n
    return d
a = input("enter")
print(counter(a))
