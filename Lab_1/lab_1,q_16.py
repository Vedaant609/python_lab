def interest(p,r,n):
    return(p*r*n/100)
a = int(input("enter the principle"))
b = int(input("enter the rate"))
c = int(input("enter the time in years"))
v = interest(a,b,c)
print(v)
