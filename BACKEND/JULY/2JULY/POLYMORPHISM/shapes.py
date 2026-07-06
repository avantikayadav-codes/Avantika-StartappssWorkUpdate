class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        print("Area of Circle")


class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")


class Triangle(Shape):
    def area(self):
        print("Area of Triangle")


def display_area(shape):
    shape.area()


c = Circle()
r = Rectangle()
t = Triangle()

display_area(c)
display_area(r)
display_area(t)