# Створіть функцію, яка видаляє вказаний рядок з текстового файлу.

f = open('Lorem ipsum.txt', 'w')
f.write('Lorem\nipsum\ndolor\nsit\namet,\nconsectetur\nadipiscing\nelit.\nPhasellus\nvitae.')
f.close()

def delete_row(filename, row_number):
    f = open(filename)
    rows = f.readlines()
    f.close()

    if 0 < row_number <= len(rows):
        del rows[row_number - 1]
    else:
        print(f'Нет строки с таким номером. В файле только {len(rows)} строк')

    f = open(filename, 'w')
    for row in rows:
        f.write(row)
    f.close()


delete_row('Lorem ipsum.txt', 5)
