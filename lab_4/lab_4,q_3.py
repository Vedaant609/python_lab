def counter(a):
    q=0
    w=0
    for i in a:
        if i.isdigit() == True:
            q +=1
        elif i.isalpha() == True:
            w+=1
    print(q,"alphabets")
    print(w,"nums")
c = input("enter str")
counter(c)
