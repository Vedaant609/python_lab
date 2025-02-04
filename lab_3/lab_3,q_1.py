def vowels(a):
    t = 0
    for i in a:
        if i.lower() in "aeiou":
            t+=1
    return(t)
st = input("enter the string")
d = vowels(st)
print(d)
