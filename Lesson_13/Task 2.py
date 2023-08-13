# Напишіть генератор, який повертає послідовність чисел Фібоначчі.

def fibonacci_generator():
    first_number, second_number = 0, 1

    while True:
        yield first_number
        first_number, second_number = second_number, first_number + second_number
        

fib_gen = fibonacci_generator()
for i in range(10):
    print(next(fib_gen))
