def counter(x,c=0):
    x = x.lower()
    v = "aeiou"
    if c == len(x):
        return 0
    return(1 if x[c] in v else 0)+counter(x,c+1)
a = input("enter string")
print(counter(a))
    
    
