def reader(a):
    l = {}
    for i in a:
        l[i] = a.count(i)
    print(l)
x = input("enter")
reader(x)
