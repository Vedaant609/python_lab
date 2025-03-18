def average(x,c=0,v=0):
    if c==len(x):
        return v/len(x)
    return(average(x,c+1,v+x[c]))
print(average([1,2,3,4,5]))
