# Створіть контекстний менеджер DividerContext, який буде прінтити символ, який ми до нього передамо як розділитель для
# основного блоку коду до та після його виконання. Реалізувати контекстний менеджер потрібно 2 способами,
# за допомогою декоратора contextmanager та за допомогою класу.

from contextlib import contextmanager


# Создание контекстного менеджера с помощью декоратора contextmanager
@contextmanager
def divider_context(divider):
    print(divider * 100)
    yield
    print(divider * 100)


with divider_context('*'):
    print('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed accumsan sem nunc, sed euismod.')


# Создание контекстного менеджера с помощью класса
class DividerContext:
    def __init__(self, divider):
        self.divider = divider

    def __enter__(self):
        print(self.divider * 100)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.divider * 100)


with DividerContext(divider='*'):
    print('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed accumsan sem nunc, sed euismod.')
