def factorial(a):
    u = 1
    for i in range(1,a+1):
        u = u*i
    print(u)
v = int(input("enter the factorial"))
factorial(v)
