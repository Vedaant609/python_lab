def create_array(x,y,z,d):
    lis = []
    for i in range(x):
        temp = []
        for j in range(y):
            temp.append([d]*z)
        lis.append(temp)
    return lis
a = int(input("enter l1"))
b = int(input("enter l2"))
c = int(input("enter l3"))
d = int(input("enter element"))
q = create_array(a,b,c,d)
print(q)
                
