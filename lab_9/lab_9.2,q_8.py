def length(x,c=0):
    if len(x) == c:
        return 0
    return(1 +length(x,c+1))
print(length("123"))
