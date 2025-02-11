def converter():
    t = []
    r = 0
    u = 0
    while True:
        r = input("enter the temp in Fahrenheit ")
        if r == "":
            break
        t.append(r)
    for i in t:
        i = int(i)
        i = (5/9)*(i-32)
        t[u]=i
        u+=1
    print(t)
converter()
    
