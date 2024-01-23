import pytest
import source.shapes as shapes
import math

class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
    
    def test_area(self):
        assert self.circle.area() == math.pi * (self.circle.radius**2)
    
    def test_circumference(self):
        assert self.circle.circumference() == 2*math.pi * self.circle.radius*2

class TestRectangle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.rectangle = shapes.Rectangle(10,5)
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
    
    def test_area(self):
        assert self.rectangle.area() == self.rectangle.length * self.rectangle.width

    def test_perimeter(self):
        assert self.rectangle.perimeter() == 2 * (self.rectangle.length+self.rectangle.width)

class TestSquare:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.rectangle = shapes.Square(5)
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
    
    def test_area(self):
        assert self.rectangle.area() == self.rectangle.length * self.rectangle.width

    def test_perimeter(self):
        assert self.rectangle.perimeter() == 2 * (self.rectangle.length+self.rectangle.width)


class TestCynlinder:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.cylinder = shapes.Cylinder(3,7)
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
    
    def test_area(self):
        assert self.cylinder.surface_area() ==(2*math.pi*self.cylinder.radius)*(self.cylinder.radius + self.cylinder.height)
    def test_circumference(self):
        assert self.cylinder.circumference() == 2*math.pi*self.cylinder.radius