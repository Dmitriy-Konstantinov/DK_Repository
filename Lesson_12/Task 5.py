# Створіть декоратор retry який приймає першим аргументом число - кількість разів, яку потрібно буде повторити виконання
# функції у разі викидання нею помилки.

def retry(quantity):
    def decorator(func):
        def inner(*args, **kwargs):
            for x in range(quantity):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(f'Attempt {x+1} failed.')
            raise Exception(f'Function {func.__name__} failed.')
        return inner
    return decorator


@retry(3)
def greet(name):
    raise ValueError
    return f'Hello, {name}!'


print(greet('Alex'))
