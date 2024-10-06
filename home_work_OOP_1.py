## home_work_OOP_1.py
""" Создайте программу на Python, моделирующую иерархию геометрических фигур с помощью концепций ООП"""
class Shape:
    PI = 3.14
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError

class TwoViewShape(Shape):
    def __init__(self, a):
        super().__init__()
        self.a = a
    def area(self):
        self.a *= self.a
    def perimeter(self):
        p = (self.a + self.a) * 2

class ThreeViewShape(Shape):
    def __init__(self, a):
        super().__init__()
        self.a = a
    def area(self):
        self.a *= self.a
    def perimeter(self):
        self.a *= 2

class Rectangle(TwoViewShape, Shape):
    def __init__(self, a, b):
        super().__init__(a)
        self.width = a
        self. height = b
    def area(self):
        s = self.width * self.height
        return f'Площадь прямоугольника: {s}'
    def perimeter(self):
        p = (self.width + self.height) * 2
        return f'Периметр прямоугольника: {p}'

class Circle(TwoViewShape, Shape):
    def __init__(self, a):
        super().__init__(a)
        self.radius = a
    def area(self):
        s =  self.PI * (self.radius ** 2)
        return f'Площадь круга: {s}'
    def perimeter(self):
        c = 2 * self.PI + self.radius
        return f'Периметр круга: {c}'

class Cube(ThreeViewShape, Shape):
    def __init__(self, a):
        super().__init__(a)
        self.side = a
    def area(self):
        s = 6 * (self.side ** 2)
        return f'Площадь куба: {s}'
    def perimeter(self):
        c = 12 * self.side
        return f'Периметр куба: {c}'

class Sphere(ThreeViewShape, Shape):
    def __init__(self, a):
        super().__init__(a)
        self.radius = a
    def area(self):
        s = 4 * self.PI * (self.radius ** 2)
        return f'Площадь сферы: {s}'
    def perimeter(self):
        v = 4 / 3 * self.PI * (self.radius ** 3)
        return f'Нет формулы для расчета периметра сферы, но можно высчитать обЪем шара с радиусом  {self.radius}, который равен: {v}'

rectangle = Rectangle(4, 6)
print(rectangle.area())
print(rectangle.perimeter())

circle = Circle(5)
print(circle.area())
print(circle.perimeter())

cube = Cube(5)
print(cube.area())
print(cube.perimeter())

sphere = Sphere(3)
print(sphere.area())
print(sphere.perimeter())
