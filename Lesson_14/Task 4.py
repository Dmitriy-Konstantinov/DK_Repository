# Створіть базовий клас "Shape" (фігура), який має властивість color (колір) і метод display_color() для виведення
# коліру фігури. Створіть похідний клас "Rectangle" (прямокутник), який наслідує властивість color і додає властивості
# width (ширина) і height (висота). Забезпечте можливість встановлення значень ширини і висоти прямокутника та виведення
# їх значень.

class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f'Color: {self.color}')


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height


shape = Shape("Red")
shape.display_color()
rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()
print(rectangle.width)
print(rectangle.height)
