import math
class shape:
    def __init__(self,name,size):
        self.name = name
        self.size = size
    def s_area(self):
        if self.name == "circle":
            return 2*math.pi*self.size[0]
        elif self.name == "triange":
            return self.size[0]+self.size[1]+self.size[2]
        elif self.name == "rectangle":
            return 2*self.size[0]+2*self.size[1]
    def __repr__(self):
        if self.name == "circle":
            return f"the circumference of {self.name} is {self.s_area()}"
        else:
            return f"the perimeter of {self.name} is {self.s_area()}"
a = shape("circle",[math.pi])
print(a)
