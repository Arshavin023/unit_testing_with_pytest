import pytest
import source.shapes as shapes
import math

# Parametized test for Square
@pytest.mark.parametrize("side_length, expected_area",
                         [(1,1),(2,4),(3,9),(4,16),(5,25)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter",
                         [(1,4),(2,8),(3,12),(4,16),(5,20)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter

# Parametized test for Rectangle
@pytest.mark.parametrize("length, width, expected_area",
                         [(2,3,6),(2,4,8),(3,4,12),(4,4,16),(5,4,20)])
def test_multiple_rectangle_area(length, width, expected_area):
    assert shapes.Rectangle(length,width).area() == expected_area

@pytest.mark.parametrize("length, width, expected_perimeter",
                         [(2,3,10),(2,4,12),(3,4,14),(4,4,16),(5,4,18)])
def test_multiple_rectangle_perimeter(length, width, expected_perimeter):
    assert shapes.Rectangle(length,width).perimeter() == expected_perimeter

# Parametized test for Circle
@pytest.mark.parametrize("radius, expected_area",
                         [(3,math.pi*3**2),(4,math.pi*4**2),(5,math.pi*5**2),
                          (6,math.pi*6**2),(7,math.pi*7**2)])
def test_multiple_circle_area(radius, expected_area):
    assert shapes.Circle(radius).area() == expected_area

@pytest.mark.parametrize("radius, expected_circumference",
                         [(3,2*math.pi*3),(4,2*math.pi*4),(5,2*math.pi*5),
                          (6,2*math.pi*6),(7,2*math.pi*7)])
def test_multiple_circle_circumference(radius, expected_circumference):
    assert shapes.Circle(radius).circumference() == expected_circumference


# Parametized test for Cylinder
@pytest.mark.parametrize("radius, height, expected_surface_area",
                         [(2,3,2*math.pi*2*(2+3)),(3,4,2*math.pi*3*(3+4)),(4,5,2*math.pi*4*(4+5)),
                          (5,6,2*math.pi*5*(5+6)),(6,7,2*math.pi*6*(6+7))])
def test_multiple_cylinder_surface_area(radius, height, expected_surface_area):
    assert shapes.Cylinder(radius, height).surface_area() == expected_surface_area

@pytest.mark.parametrize("radius, height, expected_circumference",
                         [(3,1,2*math.pi*3),(4,1,2*math.pi*4),(5,1,2*math.pi*5),
                          (6,1,2*math.pi*6),(7,1,2*math.pi*7)])
def test_multiple_cylinder_circumference(radius, height, expected_circumference):
    assert shapes.Cylinder(radius, height).circumference() == expected_circumference
