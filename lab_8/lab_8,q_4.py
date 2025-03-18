def separater(x):
    y = set()
    z = set()
    for i in x:
        if i.startswith("A") == True:
            y.add(i)
        else:
            z.add(i)
    print(y)
    print(z)
x = {"Asasd","Bachan","Abhi"}
separater(x)
