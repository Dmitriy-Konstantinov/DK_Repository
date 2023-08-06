# Створіть декоратор retry який приймає першим аргументом число - кількість разів, яку потрібно буде повторити виконання
# функції у разі викидання нею помилки.

def retry(quantity):
    def decorator(func):
        def inner(*args, **kwargs):
            for x in range(quantity):
                result = func(*args, **kwargs)
            return result
        return inner
    return decorator


@retry(3)
def greet(name):
    print(f'Hello, {name}!')


greet('Alex')
