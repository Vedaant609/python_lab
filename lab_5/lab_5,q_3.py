import random
def popper():
    t = []
    o = 0
    for i in range(50):
        u = random.randrange(1,31)
        t.append(u)
    print(sorted(t))
    for i in range(50):
        if t[i] != t[i-1]:
            print(t[i])

        
        
popper()
        
