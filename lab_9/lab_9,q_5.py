def ispal(x):
    x = x.lower()
    l = []
    for i in range(97,123):
        l.append(i)
    s = set(x)
    for i in s:
        if ord(i) in l:
            l.remove(ord(i))
    if not l:
        print("True")
    else:
        print("not pal")
a = "abc    345defghijklmnopqrstuvwxyz"
ispal(a)  
