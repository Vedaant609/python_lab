def inserter(l):
    
    while True:
        r = input("enter the data")
        if r == "":
            break
        r = int(r)
        l.insert(0,r)
def peek(l):
    if len(l) ==0:
        print("empty")
    else:
        print("the peek is",l[0])
def printer(l):
    print(l)
def remover(l):
    l.popleft()
l = []
while True:
    f= input('''
    1. pop
    2. print
    3. inserter
    4. peek''')
    if f =="":
        print("terminated")
        break
    if int(f) == 1:
        popper(l)
    elif int(f) ==2:
        printer(l)
    elif int(f) == 3:
        push(l)
    elif int(f) == 4:
        peek(l)
    
