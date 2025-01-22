a = eval(input("enter the coordinates"))
b = eval(input("enter the coordinates"))
c = eval(input("enter the coordinates"))
if ((b[1]-a[1])/(b[0]-a[0])) == ((a[1]-c[1])/(a[0]-c[0])):
    print("they are on same line")
else:
    print("they are not on same line")
    
