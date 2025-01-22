def finder(a,b):
    if a>b:
        print("the larger number is",a)
        print("the smaller number is",b)
    elif a<b:
        print("the larger number is",b)
        print("the smaller number is",a)
    else:
        print("both numbers are same")
x = int(input("enter the fist number"))
z = int(input("enter the second number"))
finder(x,z)
