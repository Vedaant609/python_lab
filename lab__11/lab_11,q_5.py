class date:
    def __init__(self,d):
        self.day= d[0]
        self.mon=d[1]
        self.year=d[2]
    def __eq__(self,other):
        if all([self.day==other.day,self.mon==other.mon,self.year==other.year]):
            return "same"
        else:
            return "diff"
    def __repr__(self):
        return f"the dates are {__eq__()}"
d1= date([6,10,56])
d2 = date([6,10,56])
print(d1==d2)
