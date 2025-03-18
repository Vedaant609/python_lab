def create_list(x,y):
    x = set(x)
    y = set(y)
    v = x&y
    v = list(v)
    return v
a = eval(input("enter"))
b = eval(input("enter"))
print(create_list(a,b))
