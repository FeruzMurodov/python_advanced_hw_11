from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        print('Hello from abstract class!')


class Circle(Shape):
    def area(self):
        super().area()
        return "Here is area of Circle"


class Rectangle(Shape):
    def area(self):
        super().area()
        return "Here is area of Rectangle"


class Triangle(Shape):
    def area(self):
        super().area()
        return "Here is area of Triangle"

if __name__ == '__main__':
    circle = Circle()
    rectangle = Rectangle()
    triangle = Triangle()
    print(circle.area())
    print()
    print(rectangle.area())
    print()
    print(triangle.area())
