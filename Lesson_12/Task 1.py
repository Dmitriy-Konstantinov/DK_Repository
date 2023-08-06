# Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду. Контекстний менеджер повинен виводити
# час, що минув, при виході з контексту. Використовуйте контекстний менеджер для вимірювання часу виконання певного
# фрагменту коду.
# Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.

from time import time, sleep
from contextlib import contextmanager


# Создание контекстного менеджера с помощью декоратора contextmanager
@contextmanager
def timer():
    start = time()
    yield
    end = time()
    print(end-start)


with timer():
    fruits_list = ['apple', 'banana', 'orange']
    fruits_string = '\n'.join(fruits_list)
    print(fruits_string)


# Создание контекстного менеджера с помощью класса
class Timer:
    def __enter__(self):
        start = time()
        return start

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        print(end-self.__enter__())


with Timer():
    fruits_list = ['apple', 'banana', 'orange']
    fruits_string = '\n'.join(fruits_list)
    print(fruits_string)
