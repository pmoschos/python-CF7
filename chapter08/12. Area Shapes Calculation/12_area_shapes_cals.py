# A program that uses the 'match' keyword to work with different geometric shapes.

from math import pi

class Shape:
    """Base class for all geometric shapes."""
    def area(self):
        """Calculates the area of the shape."""
        raise NotImplementedError("Subclasses must implement the area method.")

class Circle(Shape):
    """Class representing a Circle."""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)

class Rectangle(Shape):
    """Class representing a Rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    """Class representing a Triangle."""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


def calculate_area(shape):
    """
    Calculates the area of the given shape using the 'match' keyword.

    Args:
        shape: An instance of a Shape or its subclasses.
    """
    match shape:
        # Case for matching a Circle instance
        case Circle(radius=radius):
            area = shape.area()
            print(f"The area of the circle with radius {radius} is {area:.2f}.")
        
        # Case for matching a Rectangle instance
        case Rectangle(width=width, height=height):
            area = shape.area()
            print(f"The area of the rectangle with width {width} and height {height} is {area}.")
        
        # Case for matching a Triangle instance
        case Triangle(base=base, height=height):
            area = shape.area()
            print(f"The area of the triangle with base {base} and height {height} is {area}.")
        
        # Default case for unknown shapes
        case _:
            print("Unknown shape.")


# Test cases to help students understand pattern matching with geometric shapes
if __name__ == "__main__":
    # Creating instances of different shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 7)
    unknown_shape = Shape()

    # Calculating and printing the area of each shape
    calculate_area(circle)          # Should calculate and print the area of the circle
    calculate_area(rectangle)       # Should calculate and print the area of the rectangle
    calculate_area(triangle)        # Should calculate and print the area of the triangle
    calculate_area(unknown_shape)   # Should indicate that the shape is unknown
