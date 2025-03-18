def binary(l,a):
    while a!=0:
        if a%2 == 0:
            l.append(0)
            a=a/2
            return (binary(l,a))
        else:
            l.append(1)
            a = (a-1)/2
            return (binary(l,a))
    l = l[::-1]
    return l
t = []
a = int(input("enter the num"))
print(binary(t,a))
