import random
def sorter():
    t = []
    positive=[]
    negative = []
    for i in range(30):
        r = random.randrange(-15,16)
        t.append(r)
    print(t)
    for i in t:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    print(positive)
    print(negative)
sorter()
