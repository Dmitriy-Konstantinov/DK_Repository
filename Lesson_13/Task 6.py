# Напишіть генератор, який фільтрує непарні числа з заданої послідовності.

def even_number_filter(number_list):
    return (number for number in number_list if number % 2 == 0)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = even_number_filter(numbers)
for num in even_nums:
    print(num)
