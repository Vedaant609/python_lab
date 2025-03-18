import random
def deller():
    s = set()
    l = []
    for i in range(10):
        k = random.randrange(15,46)
        if k in s:
            k = random.randrange(15,46)
        s.add(k)
    print(s)
    for i in s:
        if i < 30:
            l.append(i)
    for i in l:
        if i in s:
            s.remove(i)
    print(s)
deller()
        
        
    
