from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC): # here ABC denotes that it is a abstract class and object cannot be created directly, use child class to create object 
    
    @abstractmethod # decorator 
    def area(self):
        pass


    def description(self):
        print("This is a shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Test
r = Rectangle(5, 3)
c = Circle(4)


print("Rectangle Area:", r.area())
print("Circle Area:", c.area())

r.description()

