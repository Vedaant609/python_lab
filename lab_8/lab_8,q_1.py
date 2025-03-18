def modder():
    x = set()
    print(x)
    for i in range(5):
        w = input("enter the name")
        x.add(w)
    print(x)
    r = input("enter the name to modify")
    d = input("enter new name")
    x.discard(r)
    x.add(d)
    print(x)
    for i in range(2):
        o =input("enter the element to delete")
        x.discard(o)
    print(x)
modder()
