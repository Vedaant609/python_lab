def converter():
    t =[]
    u = 0
    for i in range(5):
        r = input("enter the string")
        t.append(r)
    for i in t:
        i = i.upper()
        t[u]=i
        u+=1
    print(t)
converter()
