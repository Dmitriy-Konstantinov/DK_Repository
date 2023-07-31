# Створіть функцію, яка приймає рядок від користувача та записує його у файл.

f = open('Lorem ipsum.txt', 'w')
f.write('Lorem\nipsum\ndolor\nsit\namet,\nconsectetur\nadipiscing\nelit.\nPhasellus\nvitae.')
f.close()


def add_to_file():
    user_string = input('Введите ваш текст: ')

    file = open('Lorem ipsum.txt', 'a')
    file.write('\n' + user_string)
    file.close()


add_to_file()
