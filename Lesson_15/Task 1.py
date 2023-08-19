# Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.

def sum_digits(number):
    if number < 10:
        return number

    last_digit = number % 10
    remaining_digits = number // 10
    return last_digit + sum_digits(remaining_digits)


print(sum_digits(1234))
