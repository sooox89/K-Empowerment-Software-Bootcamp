# day07 class 

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        # self.x = x
        # self.y = y
        # self.radius = radius
        super().__init__(x, y, radius)
        self.height = height

    def __init__(self, x, y, width, length):
    def get_area(self):
        return self.width * self.length

    def __repr__(self):
        return f'사각형의 좌표는 x:{self.x}, y:{self.y}이고 넓이는 {self.get_area()}입니다'

    def __add__(self, other):
        # 두 사각형 넓이의 합
        return (self.width * self.length) + (other.width * other.length)
        # 각 사각형 width의 합과 length 합의 곱
        # return Rectangle(0, 0, (self.width+other.width), (self.length+other.length))

cy1 = Cylinder(20, 20, 10.0, 2)
c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r2 = Rectangle(70, 30, 10, 15)
r1 = Rectangle(100, 50, 5, 2)

print(r2)
print(cy1.get_area())
print(f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 {r1.get_area()}입니다')
print(r1)
print(r1 + r2)
print(c1.get_area())