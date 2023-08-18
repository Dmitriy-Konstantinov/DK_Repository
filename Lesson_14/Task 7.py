# Розробіть клас "Square", який успадковує властивості і методи з класу "Rectangle". Додайте властивість
# side_length (довжина сторони) і перевизначте методи, які використовують властивості width і height класу "Rectangle",
# щоб вони використовували властивість side_length класу "Square". Виведіть значення ширини, висоти і довжини сторони
# для об'єкта класу "Square".

class Rectangle:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def display_color(self):
        print(f'Color: {self.color}, Width: {self.width}, Height: {self.height}')


class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)
        self.side_length = side_length

    def display_color(self):
        print(f'Color: {self.color}')


square = Square("Green", 8)
square.display_color()
print(square.width)
print(square.height)
print(square.side_length)
