# Автосалон

from abc import ABC, abstractmethod


class Car:
    @abstractmethod
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def display_info(self):
        pass


class Sedan(Car):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_info(self):
        print(f'Car: {self.brand} {self.model}\n'
              f'Doors: {self.doors}')


class SUV(Car):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        print(f'Car: {self.brand} {self.model}\n'
              f'Seats: {self.seats}')


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display_info(self):
        print(f'Car: {self.brand} {self.model}\n'
              f'Max Speed: {self.speed} km/h')


# Створюємо об'єкти різних класів
sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

# Виводимо інформацію про кожен автомобіль
sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()