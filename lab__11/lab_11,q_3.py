import math
class solid:
    def __init__(self,s,size):
        self.shape = s
        self.size = size
    def surface_area(self):
        if self.shape == "sphere":
            return 4*math.pi*self.size[0]**2
    def __repr__(self):
        return f"surface area = {self.surface_area()}"
e = solid("sphere",[12])
print(e)
