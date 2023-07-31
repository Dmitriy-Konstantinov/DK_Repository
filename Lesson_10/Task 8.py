# Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст, виводячи рядки, які є у першому файлі,
# але відсутні у другому.

f = open('Lorem ipsum.txt', 'w')
f.write('Lorem\nipsum\ndolor\nsit\namet,\nconsectetur\nadipiscing\nelit.\nVestibulum\nbibe.')
f.close()

f = open('Comparison.txt', 'w')
f.write('Lorem\nipsum\ndolor\nsit\namet,\nconsectetur\nadipiscing\nelit.\nNullam\nmattis.')
f.close()

def file_to_list(filename):
    filename = open(filename, 'r', encoding='utf-8')
    list_of_rows = [row.strip() for row in filename.readlines()]
    return list_of_rows


list_1 = file_to_list('Lorem ipsum.txt')
list_2 = file_to_list('Comparison.txt')

for item in list_1:
    if item not in list_2:
        print(item)
