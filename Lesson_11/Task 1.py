# Створіть клас Rectangle для представлення прямокутника. Додайте методи для обчислення площі та периметра прямокутника.
# Створіть об'єкт Rectangle і викличте ці методи.

class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        print(f'Area of this rectangle is {self.side_a * self.side_b}')

    def perimeter(self):
        print(f'Perimeter of this rectangle is {(self.side_a + self.side_b) * 2}')


rectangle = Rectangle(4, 5)
rectangle.area()
rectangle.perimeter()
