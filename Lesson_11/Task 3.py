# Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути, такі як назва, швидкість і вартість.
# Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
# Створіть список транспортних засобів і відсортуйте його за швидкістю.

class Vehicle:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price

    def __gt__(self, other):
        return self.speed > other.speed

    def __str__(self):
        return f'{self.name} - {self.speed} км/час'


Renault = Vehicle('Renault', 190, 30000)
Toyota = Vehicle('Toyota', 210, 40000)
Peugeot = Vehicle('Peugeot', 180, 25000)
Volkswagen = Vehicle('Volkswagen', 200, 35000)

cars = [Renault, Toyota, Peugeot, Volkswagen]
cars.sort(reverse=True)

for item in cars:
    print(item)
