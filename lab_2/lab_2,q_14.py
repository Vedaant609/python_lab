def fail(a,b,c):
    if (a<39 or b<39 or c<39):
        print("fail")
    else:
        print("pass")
def avg(a,b,c):
    return ((a+b+c)/3)
def grade(a,b,c):
    l = [a,b,c]
    for i in l:
        if 0<=i<=39:
            print("F grade ",i)
        elif 40<i<=44:
            print("P grade ",i)
        elif 45<=i<=49:
            print("C grade ",i)
        elif 50<=i<=59:
            print("B grade ",i)
        elif 60<=i<=69:
            print("B+ grade ",i)
        elif 70<=i<=79:
            print("A grade ",i)
        else:
            print("A+ grade ",i)
x = int(input("enter the marks of maths"))
y = int(input("enter the marks of physics"))
z = int(input("enter the marks of CP"))
grade(x,y,z)
t = avg(x,y,z)
fail(x,y,z)
print("the avg is ",t)





            
