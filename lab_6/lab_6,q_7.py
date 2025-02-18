def del_(l):
    r = int(input("enter the index of element"))
    t = []
    for i in l:
        if not i == l[r]:
            t.append(i)
    print(tuple(t))
        


l = (1,2,3,4,5,6)
del_(l)
