from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        print("Area of Circle")


class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")


obj1 = Circle()
obj2 = Rectangle()

obj1.area()
obj2.area()