def popper(l):
    for i in l:
        if i == ():
            l.remove(i)
    print(l)
l = [(),(123),(342)]
print(l)
popper(l)

    
