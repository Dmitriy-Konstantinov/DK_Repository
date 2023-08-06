# Реалізувати декоратор кешування memoize, який кешує результати декорованої функції для покращення продуктивності при
# повторних викликах з тими самими аргументами. Тобто він повинен запамʼятовувати аргументи з якими функція визивалась і
# результат роботи функції з цими аргументами. І у випадку, якщо ми вже маємо результат для цих аргументів, просто
# повернути закешований результат, замість виклику функції.

def memoize(func):
    cache = {}

    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return inner


@memoize
def add_numbers(a, b):
    return a+b


print(add_numbers(3, 5))
print(add_numbers(4, 7))
print(add_numbers(3, 5))
