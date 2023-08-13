# Напишіть генератор, який видає послідовність квадратів чисел від 1 до N.

def square_generator(n):
    for number in range(1, n+1):
        yield number * number


for square in square_generator(5):
    print(square)
