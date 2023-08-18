# Розробіть клас "Car", який містить такі властивості: make (марка автомобіля), model (модель автомобіля),
# year (рік випуску автомобіля) і mileage (пробіг автомобіля). Забезпечте можливість доступу до цих властивостей через
# методи, а також зробіть властивості "make" і "model" приватними.
# Додайте метод "drive" до класу "Car", який збільшує пробіг автомобіля на задане значення.
# Перевірте, чи не перевищує пробіг заданий ліміт (наприклад, 300 000 км), і виведіть повідомлення про досягнення ліміту
# при спробі здійснити поїздку.

class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage
        self.__mileage_limit = 300000

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, distance):
        if self.mileage + distance < self.__mileage_limit:
            self.mileage += distance
            print(f'Текущий пробег: {self.mileage} км')
        else:
            print('Невозможно совершить поездку. Превышен лимит пробега')


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car.get_mileage())

car.drive(100)
print(car.get_mileage())

car.drive(300000)
