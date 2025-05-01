class mat:
    def __init__(self,c):
        self.c =c
        
    def __add__(self,other):
        x = mat(list(map(lambda x,y:[a+b for a,b in zip(x,y)],self.c,other.c)))
        return(x)
    def __repr__(self):
        return '\n'.join(str(i) for i in self.c)
    def __sub__(self,other):
        x = mat(list(map(lambda x,y:[a-b for a,b in zip(x,y)],self.c,other.c)))
        return x
    def __mul__(self,other):
        temp =[list(i) for i in zip(*self.c)]
        f = []
        for i in self.c:
            t = []
            for j in temp:
                t.append(sum(a*b for a,b in zip(i,j)))
            f.append(t)
        x=mat(f)        
        return x        
            
w = mat([[1,2,3],[4,5,6],[7,8,9]])
q = mat([[1,2,3],[4,5,6],[7,8,9]])
r = w+q
print(r)
y = w-q
print(y)
p = w*q
print(p)
