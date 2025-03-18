def sum_avg():
    y = []
    for i in range(5):
        u = int(input("ENTER"))
        y.append(u)
    w = sum(y)
    e = w/5
    return(w,e)
a,b = sum_avg()
print(a,b)
