from abc import ABC, abstractmethod

class Shape(ABC):  # Shape is an abstract base class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# This would cause a TypeError because Circle doesn't implement perimeter
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14159 * self.radius ** 2

# Correct Circle implementation
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# You cannot instantiate the abstract class directly
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

rect = Rectangle(5, 10)
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")

circ = Circle(7)
print(f"Circle Area: {circ.area()}")
print(f"Circle Perimeter: {circ.perimeter()}")