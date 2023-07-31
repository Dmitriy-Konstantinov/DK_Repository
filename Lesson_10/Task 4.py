# Реалізуйте функцію, яка ділить два числа, але обробляє помилку **`ZeroDivisionError`**, якщо друге число дорівнює нулю.

def zero_division(a, b):

    try:
        print(a/b)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


zero_division(5, 0)
