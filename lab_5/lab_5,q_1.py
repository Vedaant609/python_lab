import random
def odd():
    o = []
    e = []
    t = []
    u = 0
    for i in range(5):
        y = random.randrange(1,100,2)
        o.append(y)
    print("got the random odd",o)
    for i in range(4):
        y = random.randrange(0,100,2)
        e.append(y)
    print("got the even nos",e)
    o[2]=e
    print(o)
    i = 0
    while i !=2:
        t.append(o[i])
        i+=1
    for i in o[2]:
        t.append(i)
    for i in range(3,5):
        t.append(o[i])
    print(t)
    print("the sorted list,",sorted(t))
    
odd()    
        
    

