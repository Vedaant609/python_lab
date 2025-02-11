import math
def sin(x,n):
    x = x*3.14159/180
    s = 0
    for i in range(n):
        temp = (-1)**i*(x**(2*i+1))/math.factorial(2*i+1)
        s+=temp
    return s
        
a = float(input("enter in degree"))
b = int(input("enter the terms"))
v = sin(a,b)
print(v)
