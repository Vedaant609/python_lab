def ncr(a,b):
    n = 1
    r = 1
    v = 1
    for i in range(1,a+1):
        n = n*i
    for i in range(1,b+1):
        r = r*i
    for i in range(1,a-b+1):
        v = v*i
    print(n/(r*v))
def npr(a,b):
    n = 1
    r = 1
    for i in range(1,a+1):
        n = n*i
    for i in range(1,a-b+1):
        r = r*i
    print(n/(r))
x = int(input("enter the value of n"))
y = int(input("enter the value of r"))
ncr(x,y)
npr(x,y)
