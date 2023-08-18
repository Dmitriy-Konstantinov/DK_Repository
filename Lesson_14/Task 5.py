# Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод display_color().
# В методі display_color() виведіть повідомлення про колір прямокутника і додайте також виведення повідомлення про його
# розміри (ширину і висоту).

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

    def display_color(self):
        print(f'Color: {self.color}, Width: {self.width}, Height: {self.height}')


shape = Shape("Red")
shape.display_color()
rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()
print(rectangle.width)
print(rectangle.height)
