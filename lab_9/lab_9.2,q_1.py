def prime(l,x):
    e = 1
    while x!= 1:
        e+=1
        if x%e == 0:
            l.append(e)
            x = x/e
            return (prime(l,x))
    else:
        return(l)
r = []
y = int(input("enter the num"))
print(prime(r,y))
        
