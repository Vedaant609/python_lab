def frequency(x):
    d = x.split()
    g = {}
    for i in d:
        g[i] = d.count(i)
    print(g)

a = input("enter")
frequency(a)
        
