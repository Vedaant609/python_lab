def finder(a,b,c):
    l = [a,b,c]
    l.sort()
    print("the smallest is ",l[0])
    print("the largest is ",l[2])
x = int(input("enter the fist number"))
y = int(input("enter the second number"))
z = int(input("enter the 3rd number"))
finder(x,y,z)

