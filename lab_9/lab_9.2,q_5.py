def powr(x,y):
    if y == 0:
        return 1
    return(x*powr(x,y-1))
print(powr(2,1))
