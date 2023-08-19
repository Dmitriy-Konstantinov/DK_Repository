# Створіть метаклас, який записує в консоль повідомлення, коли створюється новий клас.

class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f'Class "{name}" has been created')
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    pass
