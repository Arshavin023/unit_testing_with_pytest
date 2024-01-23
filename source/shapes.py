import math 

class Shape:
    def area(self):
        pass 
    def perimeter(self):
        pass
    def surface_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
    def circumference(self):
        return 2*math.pi*self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length+self.width)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def surface_area(self):
        return 2*math.pi*self.radius*(self.radius+self.height)
    def circumference(self):
        return 2*math.pi*self.radius
    
test = Cylinder(3,7)
print(test.surface_area())
print(test.circumference())