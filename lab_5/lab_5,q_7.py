def printer(l):
    for i in l:
        print(i,",",end="")
        
def popper(l):
    if len(l) == 0:
        print("underflow")
    else:
        l.pop()
    
def push(l):
    u = 0
    while True:
        r = input("enter the data in stack")
        if r == "":
            break
        l.append(r)
    for i in l:
        i = int(i)
        l[u]=i
        u+=1
def peek(l):
    if len(l) == 0:
        print("empty")
    else:
        print("peek is",l[-1])
l = []
while True:
    f= input('''
    1. pop
    2. print
    3. push
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
    

    
