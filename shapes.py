import math
from msilib.schema import Class
# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area_Circle(self):
        A=math.pi*self.radius*self.radius
        return f"The area is of the circle is: {A}"
    def circumference_Circle(self):
        C=2*math.pi*self.radius
        return f"The circumference of the circle is: {C}"

# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a
class Square():
    def __init__(self,a):
        self.a=a
    def area_Square(self):
        A=self.a*self.a
        return f"The area of the square is: {A}"
    def perimeter_Square(self):
        P=4*self.a
        return f"The perimeter of the square is: {P}"
# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)
class Rectangle():
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area_Rectangle(self):
        A=self.w*self.l
        return f"The area of the rectangle is: {A}"
    def perimeter_Rectangle(self):
        P=2(self.l+self.w)
        return f"The perimeter of the rectangle is: {P}"
# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
class Sphere():
    def __init__(self,r):
        self.r=r
    def surface_Area(self):
        A=4*math.pi*self.r*self.r
        return f"The surface area of the Sphere is: {A}"
    def volume_Sphere(self):
        V=4/3(math.pi*self.r**3)
        return f"The volume of the sphere is: {V}"