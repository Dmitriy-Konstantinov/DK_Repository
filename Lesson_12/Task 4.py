# Реалізувати декоратор timeit, який вимірює час виконання декорованої функції і виводить його.
# Для отримання часу роботи скористуйтесь модулем time і функцією time.time()

import time


def timeit(func):

    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f'Function time: {end-start} seconds')

    return inner


def list_to_string():
    fruits_list = ['apple', 'banana', 'orange']
    fruits_string = '\n'.join(fruits_list)
    print(fruits_string)


timeit(list_to_string)()
