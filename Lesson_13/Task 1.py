# Змініть функцію even_odd_generator так, щоб вона генерувала послідовність чисел від 1 до n з рядками "Fizz" для чисел,
# які діляться на 3, "Buzz" для чисел, які діляться на 5, і "FizzBuzz" для чисел, які діляться як на 3, так і на 5.

def even_odd_generator(n):
    number = 1
    while number <= n:
        if number % 3 == 0 and number % 5 == 0:
            yield 'FizzBuzz'
        elif number % 3 == 0:
            yield 'Fizz'
        elif number % 5 == 0:
            yield 'Buzz'
        else:
            yield number

        number += 1


even_odd = even_odd_generator(30)
for i in even_odd:
    print(i)
