import math
def circle(a,b,c):
    if math.sqrt(a**2+b**2) == c:
        print("the point is on the circle")
    elif math.sqrt(a**2+b**2)< c:
        print("the point is inside the circle")
    else:
        print("the point is outside the circle")
x = int(input("enter the x coordinate"))
y = int(input("enter the y coordinate"))
r = int(input("enter the radius"))
circle(x,y,r)
    
