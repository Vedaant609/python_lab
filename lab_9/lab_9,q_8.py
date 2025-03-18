def convert(x):
    l = x.split()
    l = set(l)
    l = list(l)
    l.sort()
    q = " ".join(l)

    return q
a = input("enter")
print(convert(a))
