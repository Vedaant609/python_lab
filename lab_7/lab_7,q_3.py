def max_finder(a):
    p = int(input("enter the department no to find its max"))
    l = []
    for j in a[p]:
        l.append(a[p][j])
    print(max(l))
def min_finder(a):
    p = int(input("enter the department no to find its min"))
    l = []
    for j in a[p]:
        l.append(a[p][j])
    print(min(l))    
            
            
    
x = eval(input("enter the nested dictionary"))

max_finder(x)
min_finder(x)
