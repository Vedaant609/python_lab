def reverser(x,c =-1):
    if abs(c)>len(x):
        return ""
    return (x[c])+(reverser(x,c-1))
print(reverser("123"))

    
