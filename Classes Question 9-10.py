# Muhammad Wasif Zawar         FA24-BBD-053
import math

# Base class for Shape
class Shape:
    def area(self):
        pass  # This will be overridden by the subclasses

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 5)

# Print areas
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())
print("Triangle area:", triangle.area())


# Qestion Number 2:
# Define the Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # This method will be overridden in the subclasses

# Define the Dog subclass
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Woof!"

# Define the Cat subclass
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Meow!"

# Define the Cow subclass
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Moo!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

print(f"{dog.name} says: {dog.sound()}")
print(f"{cat.name} says: {cat.sound()}")
print(f"{cow.name} says: {cow.sound()}")



