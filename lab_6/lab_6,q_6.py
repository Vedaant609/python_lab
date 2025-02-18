def modder(l):
    r = int(input("enter the index of element"))
    u  = int(input("enter the element"))
    t = []
    for i in l:
        if not i == l[r]:
            t.append(i)
        else:
            t.append(u)
    print(tuple(t))
l = (1,2,3,4,5,6)
modder(l)
