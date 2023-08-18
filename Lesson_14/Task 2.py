# Розширте клас "Person" з попереднього завдання, додавши методи для зміни значень імені та віку. Зробіть так,
# щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120. При спробі встановити недійсне значення,
# виведіть повідомлення про помилку.

class Person:
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def set_name(self, new_name):
        if not any(char.isdigit() for char in new_name):
            self.__name = new_name
        else:
            print('Имя не может содержать цифры')

    def set_age(self, new_age):
        if 0 <= new_age <= 120:
            self.__age = new_age
        else:
            print('Возраст должен быть от 0 до 120')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())
print(person.get_age())

person.set_name("John123")
person.set_age(150)
