def compute(x):
    z = x*10+x
    c = x*100+z
    v = x*1000+c
    return (z+x+c+v)
a = int(input("enter the digit"))
q = compute(a)
print(q)
