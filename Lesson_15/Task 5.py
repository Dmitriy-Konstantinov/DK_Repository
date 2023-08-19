# Створіть метаклас, який переконується, що назва класу задана у форматі CamelCase.
# Перевірки на те що перший символ заглавний вистачить.

class CamelCase(type):
    def __new__(cls, name, bases, attrs):
        if name[0].islower():
            raise NameError('Class name not in CamelCase')

        return super().__new__(cls, name, bases, attrs)


class notCamelCase(metaclass=CamelCase):
    pass