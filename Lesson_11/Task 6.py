# Створіть клас Circle, який представляє коло. Реалізуйте методи для обчислення площі та довжини кола.
# Використовуйте аттрибут класу для зберігання значення π (pi).

class Circle:
    pi = 3.14159265359

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * Circle.pi

    def circle_length(self):
        return self.radius * 2 * Circle.pi


circle = Circle(7)

print(f'Circle area is {round(circle.area(), 2)} m')
print(f'Circle length is {round(circle.circle_length(), 2)} m')
