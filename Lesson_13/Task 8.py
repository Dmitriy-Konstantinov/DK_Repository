# Напишіть генератор, який видає послідовність простих чисел.

def prime_generator():
    yield 2
    number = 3
    while True:
        is_prime = True
        for divisor in range(2, int(number / 2) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 2


prime_gen = prime_generator()
for i in range(10):
    print(next(prime_gen))
