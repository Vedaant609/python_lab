def bill(x,y):
    s = 0
    for i in x:
        if i in y:
            s+= (x[i]*y[i])
    print(s)
            


a = {"milk":100,"maggi":123,"ps5":50000}
b = {"milk":2,"ps5":2}
bill(a,b)
