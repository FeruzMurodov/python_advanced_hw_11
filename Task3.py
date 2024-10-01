class Rectangle:
    sum_of_sides = 0

    def __init__(self, height, widht=None):
        self.height = height
        if widht:
            self.widht = widht
        else:
            self.widht = height
        self.sum_of_sides = self.perimeter()

    def perimeter(self):
        return (self.height + self.widht) * 2

    def area(self):
        return self.height * self.widht

    def __add__(self, other):
        return Rectangle(self.height + other.height, self.widht + other.widht)

    def __str__(self):
        return f'Rectangle with sides of widht {self.widht} and height {self.height}. Perimeter: {self.sum_of_sides}'

    def __repr__(self):
        return f'Rectangle{self.widht, self.height}'

    def __gt__(self, other):
        return self.sum_of_sides > other.sum_of_sides

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.sum_of_sides != other.sum_of_sides

    def __ge__(self, other):
        return self.sum_of_sides >= other.sum_of_sides

    def __le__(self, other):
        return self.area() <= other.area()

    def __sub__(self, other):
        height = abs(self.height - other.height)
        widht = abs(self.widht - other.widht)
        if self > other:
            return Rectangle(height, widht)
        else:
            raise ValueError('It is impossible to subtract a large value from a small value')


if __name__ == '__main__':
    rec1 = Rectangle(2, 3)
    rec2 = Rectangle(10, 5)
    print(rec1)
    print(rec2)
    rec3 = rec1 + rec2
    print(rec3)
    rec4 = rec2 - rec1
    print(rec4)
    rec5 = rec2
    print(rec5)
    print(repr(rec5))
    print(rec2 == rec5)
    print(rec1 != rec2)
    print(rec1 > rec2)
    print(rec1 < rec2)
