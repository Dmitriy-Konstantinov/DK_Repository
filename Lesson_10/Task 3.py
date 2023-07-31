# Напишіть програму, яка відкриває файл для читання та обробляє помилку FileNotFoundError, якщо файл не знайдено.

try:
    f = open('example.txt', 'r')
    f.close()
except FileNotFoundError:
    print('Такого файла не существует')
