def adder(a,b,c):
    d = {}
    d.update(a)
    d.update(b)
    d.update(c)
    return(d)
a = eval(input("enter dict 1"))
b = eval(input("enter dict 2"))
c = eval(input("enter dict 3"))
w = adder(a,b,c)
print(w)

